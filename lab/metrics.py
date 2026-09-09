"""
MATRIX2.0 Living Lab Metrics & Discovery Result

Calculates computational state discovery metrics and parameter diffs.
"""

from typing import Dict, Any, List, Optional
from matrix_core import MatrixState


class DiscoveryResult:
    """
    Measures and compares initial vs final state trajectories.
    """

    def __init__(
        self,
        initial_state: MatrixState,
        final_state: MatrixState,
        trajectory: List[Dict[str, float]],
        divergence_metric: float = 0.0,
    ):
        self.initial_params = initial_state.describe()
        self.final_params = final_state.describe()
        self.trajectory = trajectory
        self.divergence_metric = divergence_metric

        self.metrics = self._compute_metrics()

    def _compute_metrics(self) -> Dict[str, float]:
        val_initial = self.initial_params["value"]
        val_final = self.final_params["value"]
        abs_change = abs(val_final - val_initial)

        rel_change = (
            (abs_change / abs(val_initial)) if abs(val_initial) > 0 else abs_change
        )

        values = [p["value"] for p in self.trajectory] if self.trajectory else [val_initial]
        avg_val = sum(values) / len(values) if values else val_initial
        max_val = max(values) if values else val_initial

        return {
            "absolute_change": round(abs_change, 6),
            "relative_change": round(rel_change, 6),
            "average_value": round(avg_val, 6),
            "maximum_value": round(max_val, 6),
            "trajectory_length": len(self.trajectory),
            "divergence_metric": round(self.divergence_metric, 6),
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "initial_params": self.initial_params,
            "final_params": self.final_params,
            "metrics": self.metrics,
        }


def what_changed(before: Dict[str, float], after: Dict[str, float]) -> Dict[str, Any]:
    """
    Identifies parameter changes between two state parameter dictionaries.
    """
    keys = {"value", "frequency", "intensity", "phase", "chaos", "variation"}
    diffs = {}
    max_diff_key = None
    max_diff_val = -1.0

    for k in keys:
        v_before = before.get(k, 0.0)
        v_after = after.get(k, 0.0)
        diff = abs(v_after - v_before)
        diffs[k] = round(diff, 6)

        if diff > max_diff_val:
            max_diff_val = diff
            max_diff_key = k

    if max_diff_key is None or max_diff_val < 1e-6:
        summary = "Parameters remained approximately constant."
    else:
        summary = f"'{max_diff_key.capitalize()}' changed the most (difference: {max_diff_val:.6f})."

    return {
        "summary": summary,
        "most_changed_parameter": max_diff_key,
        "max_difference": round(max_diff_val, 6),
        "parameter_differences": diffs,
    }
