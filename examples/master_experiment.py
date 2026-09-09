"""
MATRIX2.0 Master Experiment Script

Executes the complete pipeline:
MOTHER -> encode -> state -> wave -> particles -> perturbation -> chaos -> measurement -> explanation
"""

import os
import sys

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lab.session import MatrixSession
from lab.state_view import generate_report


def main():
    word = "MOTHER"
    seed = 42

    print("==================================================")
    print("      MATRIX2.0 MASTER EXPERIMENT RUNNER          ")
    print("==================================================")
    print(f"Executing pipeline for word '{word}' with seed={seed}...\n")

    session = MatrixSession(input_text=word, seed=seed)
    report = generate_report(session.to_dict())

    print(report)


if __name__ == "__main__":
    main()
