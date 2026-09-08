"""
MATRIX2.0 Computational Attractor Representation

Stores computational state trajectories, parameter configurations, and summary statistics.
"""

from typing import List, Dict, Any, Optional


class ComputationalAttractor:
    """
    Represents an observed computational trajectory pattern in state space.
    """

    def __init__(
        self,
        trajectory: List[Dict[str, float]],
        parameters: Dict[str, float],
        seed: Optional[int] = None,
    ):
        self.trajectory = trajectory
        self.parameters = dict(parameters)
        self.iterations = len(trajectory)
        self.seed = seed
        self.summary_statistics = self._compute_summary()

    def _compute_summary(self) -> Dict[str, float]:
        if not self.trajectory:
            return {"min_value": 0.0, "max_value": 0.0, "avg_value": 0.0, "range": 0.0}

        values = [point["value"] for point in self.trajectory]
        min_v = min(values)
        max_v = max(values)
        avg_v = sum(values) / len(values)

        return {
            "min_value": round(min_v, 6),
            "max_value": round(max_v, 6),
            "avg_value": round(avg_v, 6),
            "range": round(max_v - min_v, 6),
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "parameters": self.parameters,
            "iterations": self.iterations,
            "seed": self.seed,
            "summary_statistics": self.summary_statistics,
            "trajectory": self.trajectory,
        }
