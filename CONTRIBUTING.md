# Contributing to MATRIX2.0

Thank you for your interest in contributing to MATRIX2.0! We welcome contributions from developers, researchers, and open-source enthusiasts.

## Code of Conduct & Integrity

MATRIX2.0 is an experimental mathematical and computational project. We prioritize:
- **REAL BUGS**: Focus on genuine technical defects and edge cases.
- **REPRODUCIBLE RESULTS**: All bug reports and feature proposals must include reproducible code examples and minimal steps.
- **USEFUL CODE & GOOD DOCUMENTATION**: Write clean Python standard-library code with accurate docstrings.
- **RESPONSIBLE DISCLOSURE**: Report security vulnerabilities responsibly.

---

## How to Contribute

You can contribute in several ways:
1. **Code**: Add tests, improve performance, or fix bugs.
2. **Documentation**: Clarify mathematical docs, theory guides, or docstrings.
3. **Experiments**: Create reproducible experiment scripts under `experiments/`.
4. **Bug Reports**: Open an issue using the Bug Report template with complete reproduction steps.

---

## Development & Testing Workflow

1. Fork and clone the repository.
2. Run unit tests before making changes:
   ```bash
   python3 -m unittest discover
   pytest
   ```
3. Ensure no external dependencies are added without prior discussion.
4. Verify all tests pass before opening a Pull Request.
