from simulations.systems.spring_mass import SpringMassSystem, solve_spring_mass
from simulations.visualisations.spring_mass import create_spring_mass_visualisations

def test_spring_mass_visualisations_are_created(tmp_path):
    system = SpringMassSystem()
    solution = solve_spring_mass(system, duration=1.0, fps=10)

    output_paths = create_spring_mass_visualisations(
        system=system,
        solution=solution,
        output_dir=tmp_path,
        include_animation=False,
    )

    assert len(output_paths) == 3

    for output_path in output_paths:
        assert output_path.exists()
        assert output_path.suffix == ".png"
        assert output_path.stat().st_size > 0