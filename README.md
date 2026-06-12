# Interactive Physics Simulations

A growing collection of physics simulations and visualisations built with Python, exploring numerical methods, classical mechanics, chaos theory, and scientific visualisation through clean, reusable code.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Table of Contents

- [Overview](#overview)
- [Simulations](#simulations)
  - [Spring-Mass Oscillator](#spring-mass-oscillator)
- [Visualisations](#visualisations)
- [Installation](#installation)
- [Usage](#usage)
- [Project Goals](#project-goals)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository is a sandbox for building polished, well tested physics simulations from first principles, numerically solving differential equations and visualising the results with `scipy` and `matplotlib`.

## Simulations

### Spring-Mass Oscillator

A damped spring-mass system modelled as a second-order ODE and solved numerically. The simulation tracks position, velocity, and energy over time, and generates three plots.

**Example output:**

```bash
Spring-mass simulation complete.
Frames: 301
Final position: -0.4640 m
Final velocity: -0.0854 m/s
Equilibrium position: -0.4900 m

Generated visualisations:
- assets/spring_mass/time_domain.png
- assets/spring_mass/phase_space.png
- assets/spring_mass/energy.png
- assets/spring_mass/animation.gif
```

## Visualisations

Each simulation generates its own set of plots and animations. See the **[Simulation Gallery](docs/gallery.md)** for a full visual overview of all simulations.

## Installation

```bash
git clone https://github.com/sahilneela/simulations.git
cd simulations
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

Run the spring-mass demo:

```bash
python examples/spring_mass_demo.py
```

Outputs are saved to `assets/spring_mass/`.

Run the test suite:

```bash
pytest
```

## Project Goals

This repo aims to demonstrate:

- Scientific computing and numerical methods
- Classical mechanics and physics modelling
- Clean, Python project structure
- Data visualisation best practices
- Solid testing and documentation

## Roadmap

Planned simulations:

- [ ] Double pendulum
- [ ] Lorenz attractor
- [ ] N-body gravity simulation
- [ ] Wave equation
- [ ] Heat equation

## License

[MIT](LICENSE)