from pathlib import Path 
from typing import Any

import matplotlib.pyplot as plt
import numpy as np

from simulations.systems.spring_mass import SpringMassSystem

def _extract_solution_data(solution: Any) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Extract time, position, and velocity arrays from a SciPy solve_ivp result."""

    if not solution.success:
        raise ValueError(f"Cannot plot failed simulation: {solution.message}")
    
    if solution.y.shape[0] < 2:
        raise ValueError("Expected solution.y to contain position and velocity rows.")
    
    time = solution.t
    position = solution.y[0]
    velocity = solution.y[1]

    return time, position, velocity

def plot_time_domain(solution: Any, output_path: str | Path) -> Path:
    """Plot position and velocity against time."""

    time, position, velocity = _extract_solution_data(solution)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(2, 1, figsize=(10,7), sharex=True)

    axes[0].plot(time, position)
    axes[0].set_ylabel("Position [m]")
    axes[0].set_title("Spring-Mass Position Over Time")
    axes[0].grid(True)

    axes[1].plot(time, velocity)
    axes[1].set_xlabel("Time [s]")
    axes[1].set_ylabel("Velocity [m/s]")
    axes[1].set_title("Spring-Mass Velocity Over Time")
    axes[1].grid(True)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path

def plot_phase_space(solution: Any, output_path: str | Path) -> Path:
    """Plot the phase-space curve: position vs velocity."""

    _time, position, velocity = _extract_solution_data(solution)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8,6))

    ax.plot(position, velocity)
    ax.scatter(position[0], velocity[0], label="Start")
    ax.scatter(position[-1], velocity[-1], label="End")

    ax.set_xlabel("Position [m]")
    ax.set_ylabel("Velocity [m/s]")
    ax.set_title("Spring-Mass Phase Space")
    ax.grid(True)
    ax.legend()

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path

def plot_energy(
        system: SpringMassSystem,
        solution: Any,
        output_path: str | Path
    ) -> Path:
    """Plot kinetic, potential, and total energy over time."""

    time, position, velocity = _extract_solution_data(solution)

    kinetic_energy = system.kinetic_energy(velocity)
    spring_potential_energy = system.spring_potential_energy(position)
    gravitational_potential_energy = system.gravitational_potential_energy(position)
    total_energy = system.total_energy(position, velocity)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10,6))

    ax.plot(time, kinetic_energy, label = "Kinetic energy")
    ax.plot(time, spring_potential_energy, label = "Spring potential energy")
    ax.plot(time, gravitational_potential_energy, label = "Gravitational potential energy")
    ax.plot(time, total_energy, label = "Total energy")

    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Energy [J]")
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
        output_dir: str | Path = "assets",
) -> list[Path]:
    """Create all current spring-mass visualisations."""

    output_dir = Path(output_dir)

    return [
        plot_time_domain(solution, output_dir / "time_domain.png"),
        plot_phase_space(solution, output_dir / "phase_space.png"), 
        plot_energy(system, solution, output_dir / "energy.png"),
    ]
