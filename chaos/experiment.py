"""
MATRIX2.0 Master Stroke Experiment Engine

Runs single-parameter perturbation experiments ("Master Stroke"), calculates
experimental surprise scores, generates educational explanations, and supports JSON/CSV data export.
"""

import csv
import datetime
import json
from typing import Dict, Any, List, Optional
from chaos.sensitivity import analyze_sensitivity, compute_trajectory_divergence


def calculate_surprise_score(metrics: Dict[str, float], delta: float) -> float:
    """
    Computes an experimental divergence/surprise score normalized to 0-100 range.
    Measures how strongly trajectory diverges relative to the size of initial perturbation delta.

    Note: This is an experimental computational divergence metric, NOT a measure of consciousness or intelligence.
    """
    max_diff = metrics.get("max_diff", 0.0)
    avg_diff = metrics.get("avg_diff", 0.0)

    if delta <= 0:
        return 0.0

    # Amplification factor = max divergence / perturbation delta
    amplification = max_diff / delta if delta > 0 else 0.0

    # Scale linearly and bound strictly between 0.0 and 100.0
    raw_score = (amplification * 0.1) + (avg_diff * 10.0)
    normalized_score = max(0.0, min(100.0, round(raw_score, 2)))
    return normalized_score


def generate_educational_explanation(
    parameter: str,
    delta: float,
    metrics: Dict[str, float],
    surprise_score: float,
) -> Dict[str, str]:
    """
    Generates structured educational explanations for experiment outcomes.
    """
    what_changed = f"Perturbed '{parameter}' by +{delta:.8f}."
    what_expected = "A smooth, deterministic wave trajectory close to baseline."
    what_happened = (
        f"Maximum trajectory deviation reached {metrics['max_diff']:.6f} "
        f"with average difference {metrics['avg_diff']:.6f}."
    )
    how_large_diff = f"Surprise/divergence score computed at {surprise_score}/100."
    why_sensitive = (
        f"The wave dynamics function is sensitive to '{parameter}' because phase accumulation "
        "and chaotic perturbations amplify initial parameter differences over time."
    )
    math_view = (
        f"delta_{parameter} = {delta:.8f} => Delta W(t) = max|W_base(t) - W_pert(t)| = {metrics['max_diff']:.6f}."
    )

    return {
        "what_changed": what_changed,
        "what_expected": what_expected,
        "what_happened": what_happened,
        "how_large_difference": how_large_diff,
        "why_sensitive": why_sensitive,
        "mathematical_view": math_view,
    }


def master_stroke_experiment(
    base_params: Dict[str, float],
    parameter: str = "frequency",
    delta: float = 0.000001,
    iterations: int = 50,
    dt: float = 0.01,
    seed: Optional[int] = 42,
) -> Dict[str, Any]:
    """
    Executes a Master Stroke experiment: changes ONE parameter slightly and compares resulting trajectories.
    """
    sensitivity_data = analyze_sensitivity(
        base_params=base_params,
        parameter=parameter,
        delta=delta,
        iterations=iterations,
        dt=dt,
        seed=seed,
    )

    metrics = sensitivity_data["metrics"]
    surprise_score = calculate_surprise_score(metrics, delta)
    explanation = generate_educational_explanation(
        parameter=parameter, delta=delta, metrics=metrics, surprise_score=surprise_score
    )

    experiment_data = {
        "experiment_title": "MATRIX2.0 Master Stroke Experiment",
        "timestamp": datetime.datetime.now().isoformat(),
        "software_version": "2.0.0-experimental",
        "seed": seed,
        "parameter_perturbed": parameter,
        "delta": delta,
        "iterations": iterations,
        "dt": dt,
        "base_params": base_params,
        "perturbed_params": sensitivity_data["perturbed_params"],
        "metrics": metrics,
        "surprise_score": surprise_score,
        "explanation": explanation,
        "baseline_trajectory": sensitivity_data["baseline_trajectory"],
        "perturbed_trajectory": sensitivity_data["perturbed_trajectory"],
    }

    return experiment_data


def export_experiment_json(experiment_data: Dict[str, Any], filepath: str) -> None:
    """Export experiment data to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(experiment_data, f, indent=2)


def export_experiment_csv(experiment_data: Dict[str, Any], filepath: str) -> None:
    """Export trajectory comparison comparison rows to a CSV file."""
    base_traj = experiment_data.get("baseline_trajectory", [])
    pert_traj = experiment_data.get("perturbed_trajectory", [])

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["step", "time", "baseline_value", "perturbed_value", "difference"])

        for idx, (b, p) in enumerate(zip(base_traj, pert_traj)):
            diff = abs(p["value"] - b["value"])
            writer.writerow([idx, b["time"], b["value"], p["value"], diff])
