# MATRIX2.0

An experimental mathematical framework for symbolic encoding, decoding, dynamical systems, and reproducible computational research.

## System Architecture

```
MATRIX2.0
├── Mathematical Core
├── Encoder / Decoder
├── Dynamics
├── Particles
├── Chaos Laboratory
├── Living Lab
├── Visual Universe
├── Simulation Arcade
├── Experiment Engine
└── Research Dashboard
```

## Layers & Components

1. **Mathematical Core** (`matrix_core.py`): Vector state representations $M = (x, f, I, \phi, c, v)$.
2. **Encoder / Decoder** (`matrix_encode.py`, `matrix_decode.py`): Text-to-state mapping and decoding.
3. **Dynamics** (`matrix_dynamics.py`): State transitions, field equations, and numerical integration.
4. **Particles** (`matrix_particles.py`): Discrete state-to-particle field mappings.
5. **Chaos Laboratory** (`chaos/`): Non-linear perturbations and strange attractors.
6. **Living Lab** (`lab/`): Interactive lesson modules and metrics.
7. **Visual Universe** (`visual/`): Visual rendering state representations.
8. **Simulation Arcade** (`arcade/`): Interactive prediction games and scoring.
9. **Experiment Engine** (`experiments/`): Deterministic reproducible experiment runner and statistical comparisons.
10. **Research Dashboard** (`dashboard/`): Local visual dashboard for exploring states, running experiments, comparing metrics, and logging research records.

## Usage & Local Launch

Launch the Research Dashboard locally:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/dashboard/` in your browser.

Run tests:

```bash
pytest
```
