# MATRIX2.0 Reproducible Experiment Engine (`experiments/`)

The **MATRIX2.0 Experiment Engine** elevates MATRIX2.0 from a collection of mathematical simulations into a structured, seed-deterministic scientific experiment platform.

---

## 🌟 Key Features

1. **Seed-Deterministic Execution**:
   - Fixed parameters, seed, and iteration count guarantee exact bitwise/numerical equivalency across independent runs.
2. **Reproducibility Engine (`reproducibility.py`)**:
   - Automated verification check (`check_reproducibility`) comparing parameter configurations, iteration counts, and numerical measurement trajectories.
3. **Parameter Sweeps (`runner.py`)**:
   - Automated grid search across parameter spaces (e.g. $f \in \{0.05, 0.08, 0.10\}$, $c \in \{0.00, 0.01, 0.05\}$) generating hundreds of local experiment runs cleanly.
4. **Experiment Comparison (`comparison.py`)**:
   - Single-pair and multi-experiment comparison calculating delta metrics ($\Delta f$, $\Delta I$, $\Delta \phi$, $\Delta \text{stability}$).
5. **Pure Python Statistics (`statistics.py`)**:
   - Dependency-free implementations of mean, median, min, max, variance, standard deviation, and range.
6. **Preset Experiments & Registry (`registry.py`)**:
   - Preset configurations: `wave_stability`, `phase_sensitivity`, `chaos_divergence`, `particle_response`, and `encoding_transformation`.

---

## 📁 File Structure

```text
experiments/
├── README.md                  # Module documentation & interpretation guidelines
├── configuration.py           # ExperimentConfig class & JSON serialization
├── experiment.py              # Experiment container class
├── runner.py                  # Deterministic model runner & parameter sweep engine
├── results.py                 # Structured report generator
├── reproducibility.py         # Exact numerical reproducibility verification
├── comparison.py              # Single/multi experiment comparison utilities
├── statistics.py             # Dependency-free statistical functions
├── registry.py                # Preset registry and lookup API
├── cli.py                     # Command-line interface
├── data/                      # Example deterministic JSON datasets
│   ├── wave_stability_example.json
│   └── chaos_divergence_example.json
└── test_experiments.py        # Comprehensive unit test suite
```

---

## 💻 CLI Usage

```bash
# List registered experiment presets
python3 -m experiments.cli list

# Run a registered experiment
python3 -m experiments.cli run wave_stability --seed 42 --iterations 100

# Run a parameter sweep
python3 -m experiments.cli sweep wave_stability

# Compare two result JSON files
python3 -m experiments.cli compare file_a.json file_b.json
```

---

## 🔬 How to Interpret Results (Scientific Epistemology)

To maintain strict scientific integrity, all users and researchers using MATRIX2.0 must adhere to the following epistemological guidelines:

1. **Simulation ≠ Physical Proof**:
   - MATRIX2.0 outputs represent dynamic state vector trajectories calculated by numerical algorithms, not physical matter or real-world energy fields.
2. **Numerical Correlation ≠ Physical Causation**:
   - Mathematical relationships between frequency, intensity, and chaos reflect model design assumptions, not physical laws.
3. **Visualization ≠ Natural Observation**:
   - Canvas wave profiles and particle projections are plot-ready graphical renderings, not atomic or subatomic observations.
4. **Symbolic Encoding ≠ Physical Materialization**:
   - Converting text into state vectors maps discrete Unicode integers to parameters; it does not materialize physical substance.
5. **Reproducibility ≠ Universal Truth**:
   - Demonstrating that `run A == run B` under fixed seed $S$ proves algorithm determinism, not universal ontological reality.
