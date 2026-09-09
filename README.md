# MATRIX2.0

An Open-Source Complexity-to-Simplicity Mathematical Research Engine, Visual Universe, Simulation Arcade & Web Universe

---

> *MATRIX2.0 lets you turn simple inputs into experiments, games, and visualizations to explore complex mathematical behavior step by step.*

$$\text{PLAY} \rightarrow \text{PREDICT} \rightarrow \text{RUN} \rightarrow \text{OBSERVE} \rightarrow \text{EXPLAIN} \rightarrow \text{REPEAT}$$

---

## Scientific & Epistemological Disclaimer

> *MATRIX2.0 is an experimental computational framework. Its simulation arcade games, visual patterns, and trajectories represent plot-ready projections of mathematical state vectors, not physical particles, energy fields, or consciousness.*

---

## 1. Quick Start

Ensure Python 3.8+ is installed (uses only standard library):

```python
from matrix_lab import MatrixLab
from arcade.games import REGISTRY

# Initialize high-level public API
lab = MatrixLab(seed=42)

# Explore a word transformation
result = lab.explore("MOTHER")
print(result["beginner_mode"])

# Run an Arcade simulation game
game = REGISTRY.get_game("wave_runner")
res = game.run({"frequency": 2.0, "intensity": 1.5}, prediction="faster wave")
print(res["explanations"]["simple"])
```

Run terminal demonstration scripts:
```bash
python3 examples/matrix2_flagship.py
python3 examples/visual_universe_demo.py
python3 examples/arcade_demo.py
```

Launch the interactive **Web Simulation Universe**:
```bash
python3 -m http.server 8000 --directory web
```
Then open `http://localhost:8000` in your browser.

---

## 2. MATRIX2.0 Simulation Arcade (`arcade/`)

The **MATRIX2.0 Simulation Arcade** features 7 interactive simulation games:

1. **Wave Runner (`wave_runner`)**: Predict waveform changes across frequency, intensity, phase.
2. **Phase Shift (`phase_shift`)**: Compare two wave systems under phase displacement shifts.
3. **Chaos Race (`chaos_race`)**: Predict trajectory divergence from minute Master Stroke parameter perturbations.
4. **Particle Dance (`particle_dance`)**: Observe multi-particle field state evolution.
5. **Resonance Lab (`resonance_lab`)**: Align frequencies between two oscillating systems and measure correlation.
6. **Pattern Hunter (`pattern_hunter`)**: Discover periodic sequences and trends in dynamic wave step output.
7. **State Transformer (`state_transformer`)**: Transform text losslessly through text -> numbers -> state -> decode pipeline.

---

## 3. MATRIX2.0 Visual Universe (`visual/`)

Complex mathematical behavior becomes easier to understand when users can see how parameters change the system:

- **`WaveVisualization`**: Generates plot-ready points `[{"t": ..., "value": ...}, ...]`.
- **`ParticleVisualization`**: Formats 2D node projections `(x, y)` for particle field rendering.
- **`TrajectoryVisualization`**: Tracks state parameter evolution across time steps.
- **`ComparisonVisualization`**: Baseline vs perturbed trajectory differences.
- **Visual Presets**: `CALM_WAVE`, `FAST_WAVE`, `HIGH_INTENSITY`, `PHASE_SHIFT`, `CHAOS_EXPLORER`, `PARTICLE_FIELD`, `DOUBLE_WAVE`.

---

## 4. How It Works

The user never needs to understand complex mathematics prior to using the system:

$$\text{PLAY} \longrightarrow \text{SEE} \longrightarrow \text{ASK} \longrightarrow \text{PREDICT} \longrightarrow \text{EXPERIMENT} \longrightarrow \text{UNDERSTAND}$$

1. **Symbolic Encoding**: Input text maps to discrete Unicode integer codes.
2. **State Vector Creation**: Array length and values populate initial vector $M = (x, f, I, \phi, c, v)$.
3. **Wave Dynamics**: Continuous wave step evaluation $W(t) = I \cdot \sin(2\pi f t + \phi) + \text{Noise}(c) + \text{Shift}(v, t)$.
4. **Particle Fields**: Synchronous multi-particle state evolution.
5. **Chaos Master Stroke**: Controlled parameter perturbation $\delta$ measuring trajectory divergence.
6. **Aha Moment & Measurement**: Plain-English educational explanation and Discovery Score (0–100).

---

## 5. Three Output Modes

Every experiment result supports three distinct levels of understanding:

- **Beginner Mode**: Plain-English explanation of inputs, wave behavior, and insights.
- **Deep Mode**: Full mathematical state vectors $M = (x, f, I, \phi, c, v)$ and wave equations.
- **Research Mode**: Raw parameter arrays, trajectory points, seeds, and JSON/CSV reproducibility metadata.

---

## 6. Repository Architecture

```text
MATRIX2.0 Architecture
│
├── Core
├── Encoder
├── Decoder
├── Dynamics
├── Particles
├── Chaos Laboratory
├── Living Lab
├── Visual Universe
├── Simulation Arcade
├── Web Simulation Universe
└── Experiment Engine (`experiments/`)

The Experiment Engine is the layer that makes MATRIX2.0 experiments reproducible, sweepable, and comparable.
```

---

## 7. Research Philosophy & Integrity

We strictly differentiate:
- **MATHEMATICAL MODEL**: The written state equations.
- **EXPERIMENT**: Seed-deterministic simulation runs.
- **OBSERVATION**: Calculated wave value trajectories.
- **HYPOTHESIS**: Testable parameter sensitivity predictions.
- **INTERPRETATION**: Educational explanations explaining observed divergence.

---

## 8. Contributing & Sponsorship

- **Contributing**: Read [CONTRIBUTING.md](CONTRIBUTING.md) for bug reporting and experiment submission guidelines.
- **Sponsorship**: Read [SPONSORS.md](SPONSORS.md) and view `.github/FUNDING.yml` to learn how sponsorship supports ongoing open-source maintenance.
