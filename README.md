# MATRIX2.0

An Open-Source Complexity-to-Simplicity Mathematical Research Engine & Visual Universe

---

> *MATRIX2.0 lets you turn simple inputs into experiments and explore complex mathematical behavior step by step.*

$$\text{INPUT} \rightarrow \text{STATE} \rightarrow \text{WAVE} \rightarrow \text{PARTICLES} \rightarrow \text{DYNAMICS} \rightarrow \text{CHAOS} \rightarrow \text{VISUALIZATION} \rightarrow \text{LEARNING}$$

---

## Scientific & Epistemological Disclaimer

> *MATRIX2.0 is an experimental computational framework. Its visual patterns and trajectories represent plot-ready projections of mathematical state vectors, not physical particles, energy fields, or consciousness.*

---

## 1. Quick Start

Ensure Python 3.8+ is installed (uses only standard library):

```python
from matrix_lab import MatrixLab
from visual.visual_state import change_one_parameter, get_visual_preset
from matrix_core import MatrixState

# Initialize high-level API
lab = MatrixLab(seed=42)

# Explore a word transformation
result = lab.explore("MOTHER")
print(result["beginner_mode"])
print(result["experiment_card"])

# Visual change-one-parameter experiment
preset = get_visual_preset("CALM_WAVE")
state = MatrixState(**preset["params"])
vis_exp = change_one_parameter(state, parameter="frequency", delta=0.5)
print(vis_exp["explanations"]["beginner"])
```

Run flagship visual demonstration:
```bash
python3 examples/visual_universe_demo.py
```

---

## 2. MATRIX2.0 Visual Universe (`visual/`)

Complex mathematical behavior becomes easier to understand when users can see how parameters change the system:

- **`WaveVisualization`**: Generates plot-ready points `[{"t": ..., "value": ...}, ...]`.
- **`ParticleVisualization`**: Formats 2D node projections `(x, y)` for particle field rendering.
- **`TrajectoryVisualization`**: Tracks state parameter evolution across time steps.
- **`ComparisonVisualization`**: Baseline vs perturbed trajectory differences.
- **Visual Presets**: `CALM_WAVE`, `FAST_WAVE`, `HIGH_INTENSITY`, `PHASE_SHIFT`, `CHAOS_EXPLORER`, `PARTICLE_FIELD`, `DOUBLE_WAVE`.

---

## 3. How It Works

The user never needs to understand complex mathematics prior to using the system:

$$\text{PLAY} \longrightarrow \text{SEE} \longrightarrow \text{ASK} \longrightarrow \text{PREDICT} \longrightarrow \text{EXPERIMENT} \longrightarrow \text{UNDERSTAND}$$

1. **Symbolic Encoding**: Input text maps to discrete Unicode integer codes.
2. **State Vector Creation**: Array length and values populate initial vector $M = (x, f, I, \phi, c, v)$.
3. **Wave Dynamics**: Continuous wave step evaluation $W(t) = I \cdot \sin(2\pi f t + \phi) + \text{Noise}(c) + \text{Shift}(v, t)$.
4. **Particle Fields**: Synchronous multi-particle state evolution.
5. **Chaos Master Stroke**: Controlled parameter perturbation $\delta$ measuring trajectory divergence.
6. **Aha Moment & Measurement**: Plain-English educational explanation and Discovery Score (0–100).

---

## 4. Three Output Modes

Every experiment result supports three distinct levels of understanding:

- **Beginner Mode**: Plain-English explanation of inputs, wave behavior, and insights.
- **Deep Mode**: Full mathematical state vectors $M = (x, f, I, \phi, c, v)$ and wave equations.
- **Research Mode**: Raw parameter arrays, trajectory points, seeds, and JSON/CSV reproducibility metadata.

---

## 5. Repository Architecture

```text
matrix2.0/
├── matrix_lab.py             # High-level public API (MatrixLab)
├── matrix_core.py            # Core MatrixState vector tuple
├── matrix_encode.py          # Symbol encoder
├── matrix_decode.py          # Symbol decoder
├── matrix_dynamics.py        # Wave dynamics engine
├── matrix_particles.py       # MatrixParticle and ParticleField
│
├── visual/                   # Visual Universe data layer (Wave, Particles, Trajectory, Comparison)
├── chaos/                    # Chaos Master Stroke engine & sensitivity analysis
├── explorer/                 # 12 core concepts, challenges, and what-if engine
├── lab/                      # Living lab pipeline, session serialization, report generator
├── opensource/               # Local bug scanner, opportunity score, tracker
├── docs/                     # Theory, Mathematics, Architecture, Roadmap docs
├── experiments/              # Reproducible experiment scripts (experiment_001.py)
├── examples/                 # Minimal, visual & flagship demonstrations
└── tests/                    # Comprehensive unit test suites
```

---

## 6. Research Philosophy & Integrity

We strictly differentiate:
- **MATHEMATICAL MODEL**: The written state equations.
- **EXPERIMENT**: Seed-deterministic simulation runs.
- **OBSERVATION**: Calculated wave value trajectories.
- **HYPOTHESIS**: Testable parameter sensitivity predictions.
- **INTERPRETATION**: Educational explanations explaining observed divergence.

---

## 7. Contributing & Sponsorship

- **Contributing**: Read [CONTRIBUTING.md](CONTRIBUTING.md) for bug reporting and experiment submission guidelines.
- **Sponsorship**: Read [SPONSORS.md](SPONSORS.md) and view `.github/FUNDING.yml` to learn how sponsorship supports ongoing open-source maintenance.
