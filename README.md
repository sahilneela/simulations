# Interactive Physics Simulations

A collection of physics simulations and visualisations built with Python.

This project explores numerical methods, classical mechanics, chaos, and scientific visualisation through clean, reusable simulation code.

## Current Simulations

### Spring-Mass Oscillator

A damped spring-mass system modelled as a second-order ordinary differential equation and solved numerically

The current implementation simulates the motion of a mass attached to a spring and prints a short summary of the result to the console.

Current output includes:
- Number of simulation frames
- Final position 
- Final velocity
- Equilibrium position

#### Example Output
```bash
Spring-mass simulation complete.
Frames: 301
Final position: -0.4640 m
Final velocity: -0.0854 m/s
Equilibrium position: -0.4900
```

#### Planned Visualisations
The spring-mass oscillator will be expanded with:

- Spring-mass animation
- Phase-space diagram showing position vs velocity
- Time-domain plot showing displacement and velocity over time
- Energy plot showing kinetic, potential, and total energy 

## Planned Simulations

- Double pendulum
- Lorenz attractor
- N-body gravity simulation
- Wave equation visualisation
- Heat equation visualisation

## Project Goals

The goal of this repository is to build a polished collection of simulations that demonstrate:

- Scientific computing
- Numerical methods
- Physics modelling
- Data visualisation
- Clean Python project structure
- Testing and documentation

## Installation

Clone the repository:

```bash
git clone https://github.com/sahilneela/simulations.git
cd simulations
```
Install the project:
```bash
pip install -e ".[dev]"
```

## Usage
Run the spring-mass demo:
```bash
python examples/spring_mass_demo.py
```

