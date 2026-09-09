"""
MATRIX2.0 Public API: Complexity-to-Simplicity Engine

High-level MatrixLab API connecting all MATRIX2.0 modules:
matrix_encode, matrix_core, matrix_decode, matrix_dynamics, matrix_particles,
chaos, explorer, and lab.
"""

import os
import sys
import json
import random
import datetime
from typing import Dict, Any, List, Optional

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from matrix_encode import encode_text
from matrix_decode import decode_values
from matrix_core import MatrixState
from matrix_dynamics import step_dynamics
from matrix_particles import ParticleField
from chaos.experiment import master_stroke_experiment, calculate_surprise_score
from chaos.sensitivity import analyze_sensitivity
from lab.pipeline import MatrixPipeline
from lab.session import MatrixSession, save_experiment, load_experiment, reproduce_experiment
from lab.metrics import what_changed, DiscoveryResult
from lab.state_view import beginner_view, deep_view, generate_report
from lab.lessons import run_prediction_check


def calculate_discovery_score(
    max_diff: float,
    avg_diff: float,
    reproducible: bool = True,
    sensitivity_factor: float = 1.0,
) -> float:
    """
    Computes an experimental discovery/surprise score normalized to 0-100 range.

    Formula:
    discovery_score = min(100.0, (max_diff * 40.0) + (avg_diff * 30.0) + (sensitivity_factor * 20.0) + (10.0 if reproducible else 0.0))

    Note: This is purely a computational divergence/sensitivity metric.
    It is NOT a measure of consciousness, intelligence, or truth.
    """
    if not reproducible:
        return 0.0

    raw = (max_diff * 40.0) + (avg_diff * 30.0) + (sensitivity_factor * 20.0) + 10.0
    return max(0.0, min(100.0, round(raw, 2)))


def generate_aha_moment(parameter: str, max_diff: float, avg_diff: float) -> str:
    """Generates an educational insight based on calculated experimental results."""
    if max_diff < 1e-5:
        return f"The parameter '{parameter}' produced no observable trajectory divergence."
    elif parameter == "frequency":
        return f"Frequency directly altered cycle speed, causing a max wave trajectory deviation of {max_diff:.6f}."
    elif parameter == "intensity":
        return f"Intensity scaled amplitude peak height, causing a max wave trajectory deviation of {max_diff:.6f}."
    elif parameter == "phase":
        return f"Phase shifted cycle alignment at t=0, causing a max wave trajectory deviation of {max_diff:.6f}."
    elif parameter == "chaos":
        return f"Chaos introduced stochastic perturbations, causing a max wave trajectory deviation of {max_diff:.6f}."
    else:
        return f"Perturbing '{parameter}' generated a max trajectory divergence of {max_diff:.6f}."


class MatrixLab:
    """
    High-level public API for MATRIX2.0 Complexity-to-Simplicity Engine.
    """

    def __init__(self, seed: Optional[int] = 42):
        self.seed = seed
        self.pipeline = MatrixPipeline(seed=seed)

    def explore(self, text: str = "MOTHER") -> Dict[str, Any]:
        """
        Executes a complete journey: WORD -> SYMBOL -> NUMBER -> STATE -> WAVE -> PARTICLES -> DYNAMICS -> CHAOS -> MEASUREMENT -> EXPLANATION -> DISCOVERY.
        Returns Beginner, Deep, and Research views, visualization-ready data, experiment card, discovery score, and AhaMoment.
        """
        if self.seed is not None:
            random.seed(self.seed)

        encoded = self.pipeline.encode(text)
        initial_state = self.pipeline.create_state(text)
        trajectory = self.pipeline.simulate(initial_state, steps=30, dt=0.01)

        field = self.pipeline.create_particles(initial_state, count=5, seed=self.seed)
        field.step_field(t=0.3, dt=0.01)

        chaos_exp = self.pipeline.run_chaos_test(
            initial_state, parameter="frequency", delta=0.000001, iterations=30, seed=self.seed
        )

        max_diff = chaos_exp["metrics"]["max_diff"]
        avg_diff = chaos_exp["metrics"]["avg_diff"]
        discovery_score = calculate_discovery_score(max_diff, avg_diff, reproducible=True)
        aha_moment = generate_aha_moment("frequency", max_diff, avg_diff)

        final_state_dict = trajectory[-1] if trajectory else initial_state.describe()
        diff_analysis = what_changed(initial_state.describe(), final_state_dict)

        # Mode views
        beg_view = (
            f"Input word '{text}' was encoded into ASCII codes {encoded}. "
            f"Wave started at value {initial_state.value:.4f} with frequency {initial_state.frequency:.2f} and intensity {initial_state.intensity:.2f}. "
            f"Evolved over 30 time steps and achieved a Discovery Score of {discovery_score}/100."
        )

        dp_view = (
            f"M_initial = {deep_view(initial_state.describe())}\n"
            f"M_final   = {deep_view(final_state_dict)}\n"
            f"Wave Eq: W(t) = {initial_state.intensity:.6f} * sin(2*pi*{initial_state.frequency:.6f}*t + {initial_state.phase:.6f})\n"
            f"Max Trajectory Deviation: {max_diff:.8f}"
        )

        res_view = {
            "timestamp": datetime.datetime.now().isoformat(),
            "seed": self.seed,
            "software_version": "2.0.0-lab-engine",
            "input_text": text,
            "encoded_values": encoded,
            "initial_state": initial_state.describe(),
            "final_state": final_state_dict,
            "particle_count": len(field.particles),
            "average_particle_value": round(field.get_average_value(), 6),
            "chaos_metrics": chaos_exp["metrics"],
            "discovery_score": discovery_score,
            "reproducible": True,
        }

        # Visualization-ready data
        vis_data = {
            "time_series": [p["time"] for p in trajectory],
            "wave_points": [p["value"] for p in trajectory],
            "particle_states": field.get_states(),
            "parameters": initial_state.describe(),
            "baseline_trajectory": chaos_exp["baseline_trajectory"],
            "perturbed_trajectory": chaos_exp["perturbed_trajectory"],
            "discovery_score": discovery_score,
        }

        # Experiment Card
        card = (
            "--------------------------------------\n"
            "MATRIX2.0 EXPERIMENT CARD\n"
            "--------------------------------------\n"
            f"Input:       {text}\n"
            f"Encoding:    {encoded}\n"
            f"Initial M:   {deep_view(initial_state.describe())}\n"
            f"Discovery:   {discovery_score}/100\n"
            f"Aha Insight: {aha_moment}\n"
            f"Reproduce:   Seed={self.seed}\n"
            "--------------------------------------"
        )

        return {
            "input": text,
            "encoded_values": encoded,
            "initial_state": initial_state.describe(),
            "final_state": final_state_dict,
            "discovery_score": discovery_score,
            "aha_moment": aha_moment,
            "beginner_mode": beg_view,
            "deep_mode": dp_view,
            "research_mode": res_view,
            "visualization_data": vis_data,
            "experiment_card": card,
            "what_changed": diff_analysis,
        }

    def ask(self, question: str, base_text: str = "MOTHER") -> Dict[str, Any]:
        """
        Interprets documented parameter questions, executes controlled experiments, and explains differences.
        Supported questions:
        - "What happens if frequency increases?"
        - "What happens if intensity becomes zero?"
        - "What happens if frequency doubles?"
        - "What happens if chaos increases?"
        - "What happens if phase changes?"
        """
        q_lower = question.lower().strip()
        state = self.pipeline.create_state(base_text)

        if "frequency increases" in q_lower or "frequency doubles" in q_lower:
            param = "frequency"
            delta = state.frequency * (1.0 if "doubles" in q_lower else 0.5)
            exp_explanation = f"Increasing frequency by +{delta:.4f} doubles or increases oscillation velocity."
        elif "intensity becomes zero" in q_lower or "intensity zero" in q_lower:
            param = "intensity"
            delta = -state.intensity
            exp_explanation = "Setting intensity to zero flattens wave amplitude to zero."
        elif "chaos increases" in q_lower:
            param = "chaos"
            delta = 0.05
            exp_explanation = "Increasing chaos parameter introduces larger stochastic noise fluctuations."
        elif "phase changes" in q_lower:
            param = "phase"
            delta = 1.5707963  # pi/2
            exp_explanation = "Shifting phase offsets initial wave position at t=0."
        else:
            param = "frequency"
            delta = 0.1
            exp_explanation = f"Question '{question}' evaluated as parameter adjustment on '{param}'."

        res = analyze_sensitivity(
            base_params=state.describe(),
            parameter=param,
            delta=delta,
            iterations=30,
            seed=self.seed,
        )

        metrics = res["metrics"]
        score = calculate_surprise_score(metrics, abs(delta))
        aha = generate_aha_moment(param, metrics["max_diff"], metrics["avg_diff"])

        return {
            "question": question,
            "parameter_tested": param,
            "delta_applied": delta,
            "baseline_value": state.value,
            "perturbed_value": res["perturbed_params"]["value"],
            "max_trajectory_diff": metrics["max_diff"],
            "surprise_score": score,
            "aha_moment": aha,
            "explanation": exp_explanation,
            "metrics": metrics,
        }

    def predict(
        self, prediction_statement: str, base_text: str = "MOTHER"
    ) -> Dict[str, Any]:
        """
        Evaluates user prediction against a deterministic simulation run.
        """
        state = self.pipeline.create_state(base_text)
        traj = self.pipeline.simulate(state, steps=30, dt=0.01)

        final_val = traj[-1]["value"]
        pred_check = run_prediction_check(prediction_statement, "frequency", final_val)

        return {
            "prediction": prediction_statement,
            "observation": f"Final wave value observed at {final_val:.6f} over {len(traj)} steps.",
            "difference": round(abs(final_val - state.value), 6),
            "result": pred_check["status"],
            "explanation": pred_check["explanation"],
        }


def save_experiment_data(experiment_dict: Dict[str, Any], filepath: str) -> None:
    """Save experiment dictionary to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(experiment_dict, f, indent=2)


def load_experiment_data(filepath: str) -> Dict[str, Any]:
    """Load experiment dictionary from a JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def reproduce_experiment_data(filepath: str) -> Dict[str, Any]:
    """
    Reproduces an experiment from a saved JSON file and verifies determinism.
    """
    data = load_experiment_data(filepath)
    res = data.get("research_mode", {})
    text = res.get("input_text", "MOTHER")
    seed = res.get("seed", 42)

    lab = MatrixLab(seed=seed)
    new_exp = lab.explore(text)

    orig_score = data.get("discovery_score", 0.0)
    new_score = new_exp["discovery_score"]
    diff = abs(new_score - orig_score)

    return {
        "reproduced": diff < 1e-6,
        "original_discovery_score": orig_score,
        "reproduced_discovery_score": new_score,
        "difference": round(diff, 6),
        "new_experiment": new_exp,
    }
