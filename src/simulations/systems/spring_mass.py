from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp


@dataclass(frozen=True)
class SpringMassSystem:
    """Damped vertical spring-mass oscillator.

    The model is:

        m q'' + b q' + k q = m g

    where:
        q   = displacement
        q'  = velocity
        m   = mass
        b   = damping coefficient
        k   = spring constant
        g   = gravitational acceleration
    """

    mass: float = 1.0
    spring_constant: float = 20.0
    damping: float = 0.55
    gravity: float = -9.8

    def derivative(self, _t: float, state: np.ndarray) -> list[float]:
        position, velocity = state

        acceleration = (
            self.mass * self.gravity - self.damping * velocity - self.spring_constant * position
        ) / self.mass

        return [velocity, acceleration]

    def equilibrium_position(self) -> float:
        return self.mass * self.gravity / self.spring_constant

    def kinetic_energy(self, velocity: np.ndarray) -> np.ndarray:
        return 0.5 * self.mass * velocity**2

    def spring_potential_energy(self, position: np.ndarray) -> np.ndarray:
        return 0.5 * self.spring_constant * position**2

    def gravitational_potential_energy(self, position: np.ndarray) -> np.ndarray:
        return -self.mass * self.gravity * position

    def total_energy(self, position: np.ndarray, velocity: np.ndarray) -> np.ndarray:
        return (
            self.kinetic_energy(velocity)
            + self.spring_potential_energy(position)
            + self.gravitational_potential_energy(position)
        )


def solve_spring_mass(
    system: SpringMassSystem,
    initial_position: float = 0.0,
    initial_velocity: float = 0.0,
    duration: float = 10.0,
    fps: int = 30,
):
    """Solve the spring-mass system over time."""

    t_eval = np.linspace(0, duration, int(duration * fps) + 1)

    return solve_ivp(
        fun=system.derivative,
        t_span=(0.0, duration),
        y0=[initial_position, initial_velocity],
        t_eval=t_eval,
        rtol=1e-9,
        atol=1e-9,
    )
