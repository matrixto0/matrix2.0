"""
MATRIX2.0 Wave Visualization Data Generator

Converts MatrixState and MatrixDynamics wave evaluations into plot-ready point arrays:
[{"t": float, "value": float}, ...]
"""

import os
import sys
from typing import List, Dict, Any, Optional

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_core import MatrixState
from matrix_dynamics import MatrixDynamics


class WaveVisualization:
    """
    Generates plot-ready time series point arrays for wave visualization.
    """

    def __init__(self, state: Optional[MatrixState] = None):
        self.state = state if state is not None else MatrixState()

    def generate_points(
        self, steps: int = 50, dt: float = 0.01
    ) -> List[Dict[str, float]]:
        """
        Generates list of plot-ready points: [{"t": round(t, 6), "value": round(val, 6)}, ...]
        """
        if steps <= 0:
            raise ValueError("Steps count must be a positive integer.")

        # Clone state so underlying instance remains clean
        current_state = MatrixState(**self.state.describe())
        dynamics = MatrixDynamics(current_state)

        points = []
        for step in range(steps):
            t = step * dt
            updated = dynamics.step(t=t, dt=dt)
            points.append({
                "t": round(t, 6),
                "value": round(updated.value, 6),
            })
        return points

    def to_dict(self, steps: int = 50, dt: float = 0.01) -> Dict[str, Any]:
        """Returns structured dictionary containing parameters and points."""
        return {
            "parameters": self.state.describe(),
            "steps": steps,
            "dt": dt,
            "points": self.generate_points(steps=steps, dt=dt),
        }
