# MATRIX2.0 Architecture Overview

MATRIX2.0 is modularly structured to separate core mathematical models, transformation encoders, dynamic simulation engines, particle systems, and open-source contribution tools.

```
matrix2.0/
├── matrix_core.py            # MatrixState class (value, frequency, intensity, phase, chaos, variation)
├── matrix_encode.py          # Text-to-MatrixState encoder
├── matrix_decode.py          # MatrixState-to-text decoder
├── matrix_dynamics.py        # MatrixDynamics engine and wave computation
├── matrix_particles.py       # MatrixParticle and ParticleField classes
│
├── experiments/              # Reproducible experiment scripts
│   ├── README.md
│   └── experiment_001.py     # "MOTHER" symbolic transformation experiment
│
├── opensource/               # Open-source contribution engine
│   ├── README.md
│   ├── bug_scanner.py
│   ├── contribution_tracker.py
│   ├── opportunity_score.py
│   └── test_opensource.py
│
├── docs/                     # Documentation
│   ├── THEORY.md
│   ├── MATHEMATICS.md
│   ├── ARCHITECTURE.md
│   └── ROADMAP.md
│
├── examples/                 # Minimal runnable examples
│   ├── encode_decode_example.py
│   └── dynamics_example.py
│
└── tests/                    # Unit testing suite
    ├── test_matrix.py
    ├── test_encoder_decoder.py
    ├── test_dynamics.py
    └── test_particles.py
```
