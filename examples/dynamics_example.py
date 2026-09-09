"""
Minimal example demonstrating MATRIX2.0 wave state dynamics over time.
"""

import os
import sys

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_core import MatrixState
from matrix_dynamics import MatrixDynamics


def main():
    state = MatrixState(
        frequency=1.0,
        intensity=2.0,
        phase=0.0,
        chaos=0.01,
        variation=0.01,
    )
    engine = MatrixDynamics(state)

    print("Initial State:", state.describe())
    print("\nStepping wave dynamics over time:")

    dt = 0.05
    for step in range(5):
        t = step * dt
        updated_state = engine.step(t=t, dt=dt)
        print(f"t={t:.2f}s | value={updated_state.value:.4f} | phase={updated_state.phase:.4f} rad")


if __name__ == "__main__":
    main()
