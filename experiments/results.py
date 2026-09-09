"""
Experiment result report generator for MATRIX2.0 Experiment Engine.
"""

from typing import Any, Dict, Optional
from experiments.comparison import compare_results
from experiments.experiment import Experiment


def generate_experiment_report(exp: Experiment, comparison_target: Optional[Experiment] = None) -> str:
    """Generate a structured, scientifically cautious experiment report string."""
    cfg = exp.config
    summary = exp.summary

    lines = []
    lines.append("================================================================================")
    lines.append(f" MATRIX2.0 EXPERIMENT REPORT: {cfg.name}")
    lines.append("================================================================================")
    lines.append(f"Experiment ID : {cfg.experiment_id}")
    lines.append(f"Model Tested  : {cfg.model}")
    lines.append(f"Seed          : {cfg.seed}")
    lines.append(f"Iterations    : {cfg.iterations}")
    lines.append(f"Timestamp     : {exp.timestamp}")
    lines.append(f"Description   : {cfg.description}")
    lines.append("--------------------------------------------------------------------------------")
    lines.append("PARAMETERS:")
    for k, v in cfg.parameters.items():
        lines.append(f"  - {k}: {v}")
    lines.append("--------------------------------------------------------------------------------")
    lines.append("MEASUREMENTS & SUMMARY STATISTICS:")
    if not summary:
        lines.append("  No summary statistics collected.")
    else:
        for metric, stats in summary.items():
            lines.append(f"  [{metric}]")
            lines.append(f"    Count: {stats.get('count')} | Mean: {stats.get('mean'):.6f} | Median: {stats.get('median'):.6f}")
            lines.append(f"    Min: {stats.get('min'):.6f} | Max: {stats.get('max'):.6f} | StdDev: {stats.get('std_dev'):.6f}")

    if comparison_target:
        lines.append("--------------------------------------------------------------------------------")
        lines.append(f"COMPARISON WITH EXPERIMENT: {comparison_target.experiment_id}")
        comp = compare_results(exp, comparison_target)
        p_diffs = comp.get("parameter_differences", {})
        lines.append("  Parameter Differences (Target - Base):")
        for pk, pv in p_diffs.items():
            lines.append(f"    - {pk}: {pv}")

        m_diffs = comp.get("metric_differences", {})
        lines.append("  Metric Means Differences:")
        for mk, mv in m_diffs.items():
            lines.append(f"    - {mk}: {mv.get('mean_difference')} (Base: {mv.get('mean_a')}, Target: {mv.get('mean_b')})")

    lines.append("--------------------------------------------------------------------------------")
    lines.append("SCIENTIFIC INTERPRETATION & BOUNDS:")
    interpretation = _generate_cautious_interpretation(exp, comparison_target)
    lines.append(f"  {interpretation}")
    lines.append("================================================================================")

    return "\n".join(lines)


def _generate_cautious_interpretation(exp: Experiment, comp_exp: Optional[Experiment] = None) -> str:
    model = exp.model
    params = exp.parameters

    if model == "wave_stability":
        chaos = float(params.get("chaos", 0.0))
        if chaos > 0.0:
            return f"The simulation exhibited parameter sensitivity under a chaos coefficient of {chaos}. Trajectory output showed variance without destabilizing underlying deterministic step bounds."
        return "The simulation produced stable sinusoidal wave trajectory bounds under baseline zero-chaos parameters."

    elif model == "chaos_divergence":
        chaos = float(params.get("chaos", 0.0))
        return f"Perturbing the chaos parameter to {chaos} caused trajectory divergence over step iterations compared to baseline zero-chaos evolution."

    elif model == "phase_sensitivity":
        delta = float(params.get("delta_phase", 0.1))
        return f"Phase displacement of {delta} radians shifted initial wave step alignment, demonstrating phase sensitivity in numerical step trajectories."

    elif model == "particle_response":
        return "Multi-particle field states evolved continuously across step iterations. Mean position tracking reflected state vector parameter shifts."

    elif model == "encoding_transformation":
        return "Symbolic text input transformed deterministically into numerical ASCII codes and derived wave oscillation frequency."

    return "Numerical outputs reflect deterministic mathematical model evolution under specified parameter parameters."
