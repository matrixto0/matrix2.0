# Contributing to MATRIX2.0

Welcome! We are excited to collaborate with developers, mathematicians, AI researchers, data scientists, and visualization engineers.

## Development Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/matrixto0/matrix2.0.git
   cd matrix2.0
   ```

2. **Create a virtual environment and install in editable mode:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e .[dev]
   ```

3. **Run tests:**

   ```bash
   pytest
   ```

## Code Standards

- Write clean, readable Python with type hints and docstrings.
- Keep functions small and modular.
- Add unit tests for every new feature or bug fix.

## Research & Mathematical Contributions

- Clearly distinguish between model-dependent simulation outputs and physical facts.
- Include seed configurations for deterministic reproducibility.
