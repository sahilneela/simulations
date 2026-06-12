from pathlib import Path
from matplotlib.animation import FuncAnimation, PillowWriter
from typing import Any

import matplotlib.pyplot as plt
import numpy as np

from simulations.systems.spring_mass import SpringMassSystem


def _extract_solution_data(solution: Any) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not solution.success:
        raise ValueError(f"Cannot plot failed simulation: {solution.message}")

    if solution.y.shape[0] < 2:
        raise ValueError("Expected solution.y to contain position and velocity rows.")

    return solution.t, solution.y[0], solution.y[1]


def _prepare_output_path(output_path: str | Path) -> Path:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    return output_path


def plot_spring_mass_time_domain(solution: Any, output_path: str | Path) -> Path:
    time, position, velocity = _extract_solution_data(solution)
    output_path = _prepare_output_path(output_path)

    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    axes[0].plot(time, position)
    axes[0].set_ylabel("Position (m)")
    axes[0].set_title("Position Over Time")
    axes[0].grid(True)

    axes[1].plot(time, velocity)
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Velocity (m/s)")
    axes[1].set_title("Velocity Over Time")
    axes[1].grid(True)

    fig.suptitle("Spring-Mass Time-Domain Response")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_spring_mass_phase_space(solution: Any, output_path: str | Path) -> Path:
    _time, position, velocity = _extract_solution_data(solution)
    output_path = _prepare_output_path(output_path)

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(position, velocity)
    ax.scatter(position[0], velocity[0], label="Start")
    ax.scatter(position[-1], velocity[-1], label="End")

    ax.set_xlabel("Position (m)")
    ax.set_ylabel("Velocity (m/s)")
    ax.set_title("Spring-Mass Phase Space")
    ax.grid(True)
    ax.legend()

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_spring_mass_energy(
    system: SpringMassSystem,
    solution: Any,
    output_path: str | Path,
) -> Path:
    time, position, velocity = _extract_solution_data(solution)
    output_path = _prepare_output_path(output_path)

    kinetic_energy = system.kinetic_energy(velocity)
    spring_potential_energy = system.spring_potential_energy(position)
    gravitational_potential_energy = system.gravitational_potential_energy(position)
    total_energy = system.total_energy(position, velocity)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(time, kinetic_energy, label="Kinetic energy")
    ax.plot(time, spring_potential_energy, label="Spring potential energy")
    ax.plot(time, gravitational_potential_energy, label="Gravitational potential energy")
    ax.plot(time, total_energy, label="Total energy")

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Energy (J)")
    ax.set_title("Spring-Mass Energy Over Time")
    ax.grid(True)
    ax.legend()

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def create_spring_mass_visualisations(
    system: SpringMassSystem,
    solution: Any,
    output_dir: str | Path = "assets/spring_mass",
    include_animation: bool = True,
) -> list[Path]:
    """Create all current spring-mass visualisations."""

    output_dir = Path(output_dir)

    output_paths = [
        plot_spring_mass_time_domain(solution, output_dir / "time_domain.png"),
        plot_spring_mass_phase_space(solution, output_dir / "phase_space.png"),
        plot_spring_mass_energy(system, solution, output_dir / "energy.png"),
    ]

    if include_animation:
        output_paths.append(animate_spring_mass(solution, output_dir / "animation.gif"))

    return output_paths


def animate_spring_mass(
    solution: Any,
    output_path: str | Path,
    fps: int = 30,
) -> Path:
    """Create a GIF animation of the spring-mass motion."""

    time, position, _velocity = _extract_solution_data(solution)
    output_path = _prepare_output_path(output_path)

    min_position = float(position.min())
    max_position = float(position.max())
    padding = 0.2 * max(abs(min_position), abs(max_position), 1.0)

    fig, ax = plt.subplots(figsize=(5, 7))

    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(min_position - padding, max_position + padding)
    ax.set_xlabel("Horizontal position")
    ax.set_ylabel("Vertical displacement [m]")
    ax.set_title("Spring-Mass Oscillator")
    ax.grid(True)

    ceiling_y = max_position + padding * 0.5
    (mass_marker,) = ax.plot([], [], marker="o", markersize=10, zorder=2.5)
    (spring_line,) = ax.plot([], [], linewidth=2, color="red")
    time_text = ax.text(
        0.05,
        0.95,
        "",
        transform=ax.transAxes,
        va="top",
    )

    def update(frame: int):
        y = position[frame]

        spring_line.set_data([0.0, 0.0], [ceiling_y, y])
        mass_marker.set_data([0.0], [y])
        time_text.set_text(f"t = {time[frame]:.2f} s")

        return spring_line, mass_marker, time_text

    animation = FuncAnimation(
        fig,
        update,
        frames=len(time),
        interval=1000 / fps,
        blit=True,
    )

    animation.save(output_path, writer=PillowWriter(fps=fps))
    plt.close(fig)

    return output_path
