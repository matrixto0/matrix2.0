"""
MATRIX2.0 Trajectory Visualization Data Generator

Records time-series parameter evolution (time, value, frequency, intensity, phase, chaos, variation)
enabling frontends to render STATE -> STATE -> STATE -> STATE state space transitions.
"""

import os
import sys
from typing import List, Dict, Any, Optional

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_core import MatrixState
from matrix_dynamics import MatrixDynamics


class TrajectoryVisualization:
    """
    Generates time-series state parameter evolution data.
    """

    def __init__(self, state: Optional[MatrixState] = None):
        self.state = state if state is not None else MatrixState()

    def generate_trajectory(
        self, steps: int = 50, dt: float = 0.01
    ) -> List[Dict[str, float]]:
        """
        Generates list of time-series state snapshots across steps.
        """
        if steps <= 0:
            raise ValueError("Steps count must be a positive integer.")

        current_state = MatrixState(**self.state.describe())
        dynamics = MatrixDynamics(current_state)

        trajectory = []
        for step in range(steps):
            t = step * dt
            updated = dynamics.step(t=t, dt=dt)
            snap = updated.describe()
            snap["time"] = round(t, 6)
            snap["value"] = round(snap["value"], 6)
            snap["frequency"] = round(snap["frequency"], 6)
            snap["intensity"] = round(snap["intensity"], 6)
            snap["phase"] = round(snap["phase"], 6)
            snap["chaos"] = round(snap["chaos"], 6)
            snap["variation"] = round(snap["variation"], 6)
            trajectory.append(snap)
        return trajectory

    def to_dict(self, steps: int = 50, dt: float = 0.01) -> Dict[str, Any]:
        """Returns structured dictionary containing initial parameters, steps count, and trajectory snapshots."""
        return {
            "initial_parameters": self.state.describe(),
            "steps": steps,
            "dt": dt,
            "trajectory": self.generate_trajectory(steps=steps, dt=dt),
        }
