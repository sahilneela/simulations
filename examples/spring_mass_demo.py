from simulations.visualisations.spring_mass import create_spring_mass_visualisations
from simulations.systems.spring_mass import SpringMassSystem, solve_spring_mass

def main() -> None:
    system = SpringMassSystem(
        mass = 1.0,
        spring_constant=20.0,
        damping=0.55,
        gravity=-9.8
    )

    solution = solve_spring_mass(
        system=system,
        initial_position=0.0,
        initial_velocity=0.0,
        duration=10.0,
        fps=30,
    )

    position = solution.y[0]
    velocity = solution.y[1]

    output_paths = create_spring_mass_visualisations(
        system=system,
        solution=solution,
        output_dir="assets/spring_mass",
    )

    print("Spring-mass simulation complete.")
    print(f"Frames: {len(solution.t)}")
    print(f"Final position: {position[-1]:.4f} m")
    print(f"Final velocity: {velocity[-1]:.4f} m/s")
    print(f"Equilibrium position: {system.equilibrium_position():.4f}")

    print("\nGenerated visualisations:")
    for output_path in output_paths:
        print(f"- {output_path}")

if __name__ == "__main__":
    main()
