"""
MATRIX2.0 Living Lab State View & Report Generator

Provides Beginner plain-English views, Deep mathematical views,
and formatted experiment reports distinguishing DATA from INTERPRETATION.
"""

from typing import Dict, Any, Optional


def beginner_view(state_dict: Dict[str, float]) -> str:
    """Format a beginner-friendly plain-English description of a state."""
    freq = state_dict.get("frequency", 1.0)
    inten = state_dict.get("intensity", 1.0)
    val = state_dict.get("value", 0.0)

    return (
        f"The system wave is currently at value {val:.4f}. "
        f"It repeats at speed {freq:.2f} (frequency) and has a peak strength of {inten:.2f} (intensity)."
    )


def deep_view(state_dict: Dict[str, float]) -> str:
    """Format a deep mathematical vector description of a state."""
    return (
        f"M = (x={state_dict.get('value', 0.0):.6f}, "
        f"f={state_dict.get('frequency', 0.0):.6f}, "
        f"I={state_dict.get('intensity', 0.0):.6f}, "
        f"phi={state_dict.get('phase', 0.0):.6f}, "
        f"c={state_dict.get('chaos', 0.0):.6f}, "
        f"v={state_dict.get('variation', 0.0):.6f})"
    )


def generate_report(session_data: Dict[str, Any]) -> str:
    """
    Generates a clean, readable text report for an experiment session.
    Strictly distinguishes DATA from INTERPRETATION.
    """
    inp = session_data.get("input_text", "MOTHER")
    enc = session_data.get("encoded_values", [])
    params = session_data.get("parameters", {})
    meas = session_data.get("measurements", {})
    seed = session_data.get("seed", 42)
    chaos_exp = session_data.get("chaos_experiment", {})

    report = []
    report.append("========================================")
    report.append("     MATRIX2.0 EXPERIMENT REPORT        ")
    report.append("========================================")
    report.append("")
    report.append("[DATA - INPUT & ENCODING]")
    report.append(f"Input Word: {inp}")
    report.append(f"Unicode ASCII: {enc}")
    report.append("")
    report.append("[DATA - INITIAL STATE VECTOR]")
    report.append(deep_view(params))
    report.append("")
    report.append("[DATA - SIMULATION MEASUREMENTS]")
    report.append(f"Initial Value: {meas.get('initial_value', 0.0):.6f}")
    report.append(f"Final Value:   {meas.get('final_value', 0.0):.6f}")
    report.append(f"Absolute Change: {meas.get('absolute_change', 0.0):.6f}")
    report.append(f"Surprise Score:  {meas.get('surprise_score', 0.0)}/100")
    report.append("")
    report.append("[DATA - REPRODUCIBILITY]")
    report.append(f"Seed: {seed}")
    report.append(f"Software Version: {session_data.get('software_version', '2.0.0')}")
    report.append("")
    report.append("[INTERPRETATION & EXPLANATION]")
    report.append(session_data.get("explanation", "No explanation available."))
    report.append(session_data.get("conclusion", "No conclusion available."))
    report.append("========================================")

    return "\n".join(report)
