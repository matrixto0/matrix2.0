"""
Experiment comparison utilities for MATRIX2.0 Experiment Engine.
"""

from typing import Any, Dict, List
from experiments.experiment import Experiment


def compare_results(exp_a: Experiment, exp_b: Experiment) -> Dict[str, Any]:
    """Calculate numerical parameter and metric differences between two experiment results."""
    params_a = exp_a.parameters
    params_b = exp_b.parameters

    freq_diff = float(params_b.get("frequency", 0.0)) - float(params_a.get("frequency", 0.0))
    inten_diff = float(params_b.get("intensity", 0.0)) - float(params_a.get("intensity", 0.0))
    phase_diff = float(params_b.get("phase", 0.0)) - float(params_a.get("phase", 0.0))
    chaos_diff = float(params_b.get("chaos", 0.0)) - float(params_a.get("chaos", 0.0))

    metric_deltas = {}
    sum_a = exp_a.summary
    sum_b = exp_b.summary

    common_metrics = set(sum_a.keys()).intersection(set(sum_b.keys()))
    for metric in common_metrics:
        mean_a = sum_a[metric].get("mean", 0.0)
        mean_b = sum_b[metric].get("mean", 0.0)
        metric_deltas[metric] = {
            "mean_a": mean_a,
            "mean_b": mean_b,
            "mean_difference": round(mean_b - mean_a, 6)
        }

    return {
        "experiment_a_id": exp_a.experiment_id,
        "experiment_b_id": exp_b.experiment_id,
        "parameter_differences": {
            "frequency_difference": round(freq_diff, 6),
            "intensity_difference": round(inten_diff, 6),
            "phase_difference": round(phase_diff, 6),
            "chaos_difference": round(chaos_diff, 6)
        },
        "metric_differences": metric_deltas
    }


def compare_multiple(experiments: List[Experiment]) -> Dict[str, Any]:
    """Compare multiple experiment results in a structured matrix."""
    if not experiments:
        return {}

    summary_table = []
    for exp in experiments:
        row = {
            "experiment_id": exp.experiment_id,
            "model": exp.model,
            "parameters": exp.parameters,
            "seed": exp.seed,
            "iterations": exp.iterations,
            "metrics": {
                m: stats.get("mean", 0.0)
                for m, stats in exp.summary.items()
            }
        }
        summary_table.append(row)

    return {
        "total_experiments": len(experiments),
        "experiments": summary_table
    }
