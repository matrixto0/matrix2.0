"""
MATRIX2.0 Sensitivity Engine

Measures trajectory divergence resulting from small parameter perturbations.
Supported parameters: frequency, intensity, phase, chaos, variation.
"""

from typing import Dict, Any, List, Optional
from chaos.chaos_engine import ChaosEngine


SUPPORTED_PARAMETERS = {"frequency", "intensity", "phase", "chaos", "variation"}


def compute_trajectory_divergence(
    baseline_trajectory: List[Dict[str, float]],
    perturbed_trajectory: List[Dict[str, float]],
) -> Dict[str, float]:
    """
    Computes trajectory differences and divergence metrics.
    """
    if len(baseline_trajectory) != len(perturbed_trajectory):
        raise ValueError("Trajectories must have equal length.")

    diffs = [
        abs(p["value"] - b["value"])
        for b, p in zip(baseline_trajectory, perturbed_trajectory)
    ]

    initial_diff = diffs[0] if diffs else 0.0
    final_diff = diffs[-1] if diffs else 0.0
    max_diff = max(diffs) if diffs else 0.0
    avg_diff = sum(diffs) / len(diffs) if diffs else 0.0

    divergence_ratio = (final_diff / initial_diff) if initial_diff > 0 else (final_diff if final_diff > 0 else 1.0)

    return {
        "initial_diff": round(initial_diff, 8),
        "final_diff": round(final_diff, 8),
        "max_diff": round(max_diff, 8),
        "avg_diff": round(avg_diff, 8),
        "divergence_ratio": round(divergence_ratio, 6),
    }


def analyze_sensitivity(
    base_params: Dict[str, float],
    parameter: str,
    delta: float = 0.000001,
    iterations: int = 50,
    dt: float = 0.01,
    seed: Optional[int] = 42,
) -> Dict[str, Any]:
    """
    Runs baseline and perturbed simulation trajectories to analyze parameter sensitivity.
    """
    param_lower = parameter.lower().strip()
    if param_lower not in SUPPORTED_PARAMETERS:
        raise ValueError(
            f"Unsupported parameter '{parameter}'. Supported parameters: {sorted(SUPPORTED_PARAMETERS)}"
        )

    # Base engine
    engine_base = ChaosEngine(**base_params, seed=seed)
    base_traj = engine_base.generate_trajectory(iterations=iterations, dt=dt)

    # Perturbed engine
    perturbed_params = dict(base_params)
    perturbed_params[param_lower] = perturbed_params.get(param_lower, 0.0) + delta

    engine_pert = ChaosEngine(**perturbed_params, seed=seed)
    pert_traj = engine_pert.generate_trajectory(iterations=iterations, dt=dt)

    metrics = compute_trajectory_divergence(base_traj, pert_traj)

    return {
        "parameter": param_lower,
        "delta": delta,
        "base_params": base_params,
        "perturbed_params": perturbed_params,
        "metrics": metrics,
        "baseline_trajectory": base_traj,
        "perturbed_trajectory": pert_traj,
    }
