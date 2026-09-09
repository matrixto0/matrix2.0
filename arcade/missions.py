"""
MATRIX2.0 Arcade Mission Manager

Defines and validates measurable educational learning missions.
"""

from typing import Dict, Any, List, Optional


class Mission:
    """Represents a measurable learning mission."""

    def __init__(
        self,
        mission_id: str,
        title: str,
        objective: str,
        hint: str,
    ):
        self.mission_id = mission_id
        self.title = title
        self.objective = objective
        self.hint = hint

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.mission_id,
            "title": self.title,
            "objective": self.objective,
            "hint": self.hint,
        }


ARCADE_MISSIONS: List[Mission] = [
    Mission(
        mission_id="predict_before_run",
        title="Predict before you run",
        objective="Provide a non-empty prediction before launching the experiment.",
        hint="Enter your prediction in the prediction text field.",
    ),
    Mission(
        mission_id="sensitive_parameter",
        title="Find the most sensitive parameter",
        objective="Run a Master Stroke experiment producing max divergence > 0.0001.",
        hint="Perturb frequency or phase slightly.",
    ),
    Mission(
        mission_id="different_trajectories",
        title="Create two different trajectories",
        objective="Produce an average trajectory divergence > 0.01.",
        hint="Increase chaos parameter or frequency delta.",
    ),
    Mission(
        mission_id="similar_waves",
        title="Make two waves as similar as possible",
        objective="Run a comparison with divergence delta < 0.0001.",
        hint="Use a very tiny perturbation delta.",
    ),
    Mission(
        mission_id="different_waves",
        title="Make two waves as different as possible",
        objective="Run a comparison with max divergence > 0.5.",
        hint="Increase frequency or intensity significantly.",
    ),
    Mission(
        mission_id="reproduce_experiment",
        title="Reproduce your previous experiment",
        objective="Successfully reproduce a saved experiment JSON file.",
        hint="Use reproduce_experiment_data().",
    ),
    Mission(
        mission_id="failed_prediction_learning",
        title="Explain why your prediction failed",
        objective="Evaluate an incorrect prediction and review the mathematical explanation.",
        hint="Failed predictions provide valuable learning insights.",
    ),
    Mission(
        mission_id="surprising_result",
        title="Find a surprising but reproducible result",
        objective="Achieve a surprise score > 50.0.",
        hint="Combine non-zero phase and high chaos.",
    ),
]


def list_missions() -> List[Dict[str, Any]]:
    """List all available Arcade missions."""
    return [m.to_dict() for m in ARCADE_MISSIONS]


def validate_mission(mission_id: str, context: Dict[str, Any]) -> bool:
    """Validate whether a mission objective has been met based on experiment context."""
    m_id = mission_id.lower().strip()

    if m_id == "predict_before_run":
        pred = context.get("prediction", "")
        return bool(pred and pred != "No prediction provided.")

    elif m_id == "sensitive_parameter":
        max_div = context.get("max_divergence", 0.0)
        return max_div > 0.0001

    elif m_id == "different_trajectories":
        avg_div = context.get("avg_divergence", 0.0)
        return avg_div > 0.01

    elif m_id == "similar_waves":
        max_div = context.get("max_divergence", 1.0)
        return max_div < 0.0001

    elif m_id == "different_waves":
        max_div = context.get("max_divergence", 0.0)
        return max_div > 0.5

    elif m_id == "reproduce_experiment":
        return bool(context.get("reproduced", False))

    elif m_id == "failed_prediction_learning":
        return context.get("prediction_status") == "not confirmed"

    elif m_id == "surprising_result":
        score = context.get("surprise_score", 0.0)
        return score > 50.0

    return False
