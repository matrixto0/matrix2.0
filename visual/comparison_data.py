"""
MATRIX2.0 Visual Comparison Data Generator

Compares baseline vs perturbed simulation trajectories and formats structured
comparison metrics connecting directly to Chaos Master Stroke analysis.
"""

import os
import sys
from typing import List, Dict, Any, Optional

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_core import MatrixState
from chaos.sensitivity import analyze_sensitivity, compute_trajectory_divergence


class ComparisonVisualization:
    """
    Generates comparison data between baseline and perturbed simulation runs.
    """

    def __init__(
        self,
        base_state: MatrixState,
        perturbed_state: MatrixState,
        steps: int = 50,
        dt: float = 0.01,
        seed: Optional[int] = 42,
    ):
        self.base_params = base_state.describe()
        self.perturbed_params = perturbed_state.describe()
        self.steps = steps
        self.dt = dt
        self.seed = seed

    def compare(self) -> Dict[str, Any]:
        """
        Computes matching parameters, changed parameters, trajectory differences,
        max divergence, average divergence, and final value difference.
        """
        keys = {"value", "frequency", "intensity", "phase", "chaos", "variation"}
        matching_params = {}
        changed_params = {}

        for k in keys:
            v_base = self.base_params.get(k, 0.0)
            v_pert = self.perturbed_params.get(k, 0.0)
            diff = abs(v_pert - v_base)
            if diff < 1e-7:
                matching_params[k] = v_base
            else:
                changed_params[k] = {
                    "baseline": round(v_base, 6),
                    "perturbed": round(v_pert, 6),
                    "delta": round(diff, 6),
                }

        # Analyze parameter perturbation using sensitivity engine
        # Find primary changed parameter key or default to frequency
        changed_key = next(iter(changed_params.keys()), "frequency")
        delta_val = changed_params.get(changed_key, {}).get("delta", 0.000001)

        sens_res = analyze_sensitivity(
            base_params=self.base_params,
            parameter=changed_key,
            delta=delta_val,
            iterations=self.steps,
            dt=self.dt,
            seed=self.seed,
        )

        metrics = sens_res["metrics"]
        base_traj = sens_res["baseline_trajectory"]
        pert_traj = sens_res["perturbed_trajectory"]

        trajectory_differences = [
            {
                "time": b["time"],
                "baseline_value": round(b["value"], 6),
                "perturbed_value": round(p["value"], 6),
                "difference": round(abs(p["value"] - b["value"]), 6),
            }
            for b, p in zip(base_traj, pert_traj)
        ]

        return {
            "matching_parameters": matching_params,
            "changed_parameters": changed_params,
            "maximum_divergence": metrics["max_diff"],
            "average_divergence": metrics["avg_diff"],
            "final_difference": metrics["final_diff"],
            "trajectory_differences": trajectory_differences,
        }
