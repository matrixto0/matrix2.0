# MATRIX2.0

An Open-Source Complexity-to-Simplicity Mathematical Research Engine

---

> *MATRIX2.0 lets you turn simple inputs into experiments and explore complex mathematical behavior step by step.*

$$\text{HUMAN INPUT} \rightarrow \text{SYMBOL} \rightarrow \text{NUMBER} \rightarrow \text{STATE} \rightarrow \text{WAVE} \rightarrow \text{PARTICLES} \rightarrow \text{DYNAMICS} \rightarrow \text{CHAOS} \rightarrow \text{MEASUREMENT} \rightarrow \text{EXPLANATION} \rightarrow \text{DISCOVERY}$$

---

## Scientific & Epistemological Disclaimer

> *MATRIX2.0 is an experimental computational framework. Its hypotheses should be evaluated through reproducible experiments rather than treated as established physical facts or claims of consciousness.*

---

## 1. Quick Start

Ensure Python 3.8+ is installed (uses only standard library):

```python
from matrix_lab import MatrixLab

# Initialize high-level API
lab = MatrixLab(seed=42)

# Explore a word transformation
result = lab.explore("MOTHER")
print(result["beginner_mode"])
print(result["experiment_card"])

# Ask parameter questions
ask_res = lab.ask("What happens if frequency increases?", base_text="MOTHER")
print(ask_res["aha_moment"])
```

Run flagship command-line demonstration:
```bash
python3 examples/matrix2_flagship.py
```

---

## 2. How It Works

The user never needs to understand complex mathematics prior to using the system:

$$\text{PLAY} \longrightarrow \text{SEE} \longrightarrow \text{ASK} \longrightarrow \text{PREDICT} \longrightarrow \text{EXPERIMENT} \longrightarrow \text{UNDERSTAND}$$

1. **Symbolic Encoding**: Input text maps to discrete Unicode integer codes.
2. **State Vector Creation**: Array length and values populate initial vector $M = (x, f, I, \phi, c, v)$.
3. **Wave Dynamics**: Continuous wave step evaluation $W(t) = I \cdot \sin(2\pi f t + \phi) + \text{Noise}(c) + \text{Shift}(v, t)$.
4. **Particle Fields**: Synchronous multi-particle state evolution.
5. **Chaos Master Stroke**: Controlled parameter perturbation $\delta$ measuring trajectory divergence.
6. **Aha Moment & Measurement**: Plain-English educational explanation and Discovery Score (0–100).

---

## 3. Three Output Modes

Every experiment result supports three distinct levels of understanding:

- **Beginner Mode**: Plain-English explanation of inputs, wave behavior, and insights.
- **Deep Mode**: Full mathematical state vectors $M = (x, f, I, \phi, c, v)$ and wave equations.
- **Research Mode**: Raw parameter arrays, trajectory points, seeds, and JSON/CSV reproducibility metadata.

---

## 4. Supported Parameter Questions (`lab.ask`)

- *"What happens if frequency increases?"*
- *"What happens if intensity becomes zero?"*
- *"What happens if frequency doubles?"*
- *"What happens if chaos increases?"*
- *"What happens if phase changes?"*

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
├── chaos/                    # Chaos Master Stroke engine & sensitivity analysis
├── explorer/                 # 12 core concepts, challenges, and what-if engine
├── lab/                      # Living lab pipeline, session serialization, report generator
├── opensource/               # Local bug scanner, opportunity score, tracker
├── docs/                     # Theory, Mathematics, Architecture, Roadmap docs
├── experiments/              # Reproducible experiment scripts (experiment_001.py)
├── examples/                 # Minimal & flagship demonstrations
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
