# MATRIX2.0 Project Roadmap

## Phase 1 — Foundation & Core Architecture
- [x] Core architecture
- [x] Encoder / Decoder
- [x] Packaging
- [x] Contribution guide
- [x] Documentation foundation

## Phase 2 — Experimental Validation & Reproducibility
- [ ] Golden Experiment
- [ ] Baseline comparison
- [ ] Independent replication
- [ ] Formal mathematical specification
- [ ] External review

## Milestone Details

### Phase 1 — Foundation & Core API
- Canonical 6D MatrixState vector representation $M = (x, f, I, \phi, c, v)$.
- Deterministic encoder/decoder with round-trip reconstruction tests.
- Package installation support (`pip install -e .`).

### Phase 2 — Dynamics & Particle Field Models
- State transition integrators (`step()`, `evolve()`).
- Computational particle field mappings.

### Phase 3 — Reproducible Experiment Engine
- Deterministic experiment runner with seed tracking.
- Statistical metrics calculation (energy, variance, entropy).

### Phase 4 — Local Research API & Research Dashboard
- Local REST API server (`api/server.py`).
- Browser-based Research Dashboard (`dashboard/index.html`).

### Phase 5 — Knowledge Graph & Discovery Engine
- Artifact graph network (nodes, relationships, provenance).
- Computational pattern discovery and ranking engine.
