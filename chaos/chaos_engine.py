"""
MATRIX2.0 Chaos Engine

Simulates state evolution over iterations and generates reproducible trajectories.
"""

import os
import sys
import random
from typing import List, Dict, Any, Optional

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_core import MatrixState
from matrix_dynamics import MatrixDynamics


class ChaosEngine:
    """
    Simulates reproducible state evolution over time steps for a given seed.
    """

    def __init__(
        self,
        value: float = 0.0,
        frequency: float = 1.0,
        intensity: float = 1.0,
        phase: float = 0.0,
        chaos: float = 0.0,
        variation: float = 0.0,
        seed: Optional[int] = None,
    ):
        self.initial_state = MatrixState(
            value=value,
            frequency=frequency,
            intensity=intensity,
            phase=phase,
            chaos=chaos,
            variation=variation,
        )
        self.seed = seed

    def generate_trajectory(
        self, iterations: int = 50, dt: float = 0.01
    ) -> List[Dict[str, float]]:
        """
        Evolve state over `iterations` steps and return list of state snapshot dictionaries.
        Guarantees seed determinism when `seed` is specified.
        """
        if iterations <= 0:
            raise ValueError("Iterations must be a positive integer.")

        if self.seed is not None:
            random.seed(self.seed)

        # Clone state so initial_state remains clean
        current_state = MatrixState(**self.initial_state.describe())
        dynamics = MatrixDynamics(current_state)

        trajectory = []
        for step in range(iterations):
            t = step * dt
            updated = dynamics.step(t=t, dt=dt)
            snapshot = updated.describe()
            snapshot["time"] = round(t, 6)
            trajectory.append(snapshot)

        return trajectory
