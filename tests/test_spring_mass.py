import numpy as np

from simulations.systems.spring_mass import SpringMassSystem, solve_spring_mass

def test_equilibrium_position_matches_mg_over_k():
    system = SpringMassSystem(
        mass = 1.0,
        spring_constant=20.0,
        damping=0.55,
        gravity=-9.8,
    )

    assert system.equilibrium_position() == -9.8/20.0

def test_solution_has_expected_number_of_frames():
    system = SpringMassSystem()
    solution = solve_spring_mass(system, duration=10.0, fps=30)

    assert len(solution.t) == 301

def test_undamped_energy_is_approximately_conserved():
    system = SpringMassSystem(
        mass = 1.0,
        spring_constant = 20.0,
        damping = 0.0,
        gravity = -9.8,
    )

    solution = solve_spring_mass(
        system = system,
        initial_position = 0.2,
        initial_velocity = 0.0,
        duration = 5.0,
        fps = 60,
    )

    position = solution.y[0]
    velocity = solution.y[1]

    energy = system.total_energy(position, velocity)
    energy_drift = np.abs(energy[-1] - energy[0])

    assert energy_drift < 1e-5