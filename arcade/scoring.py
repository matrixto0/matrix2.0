"""
MATRIX2.0 Arcade Scoring System

Calculates transparent educational scores based on prediction accuracy,
reproducibility, mission completion, and understanding.

Note: No fake activity, spam, or competitive manipulation.
"""

from typing import Dict, Any


class ArcadeScoring:
    """
    Computes transparent educational scores.
    """

    @staticmethod
    def calculate_score(
        prediction_status: str,
        reproducible: bool = True,
        mission_completed: bool = False,
        difficulty_level: int = 1,
    ) -> Dict[str, Any]:
        base_points = 10 * difficulty_level

        # Prediction points
        if prediction_status == "confirmed":
            pred_points = 30
        elif prediction_status == "partially confirmed":
            pred_points = 20
        else:
            # Incorrect/failed predictions receive learning points
            pred_points = 10

        repro_points = 20 if reproducible else 0
        mission_points = 40 if mission_completed else 0

        total = base_points + pred_points + repro_points + mission_points

        return {
            "total_score": total,
            "breakdown": {
                "difficulty_base": base_points,
                "prediction_points": pred_points,
                "reproducibility_points": repro_points,
                "mission_points": mission_points,
            },
            "formula_explanation": (
                f"Score = Base({base_points}) + Prediction({pred_points}) + "
                f"Reproducibility({repro_points}) + Mission({mission_points}) = {total}"
            ),
        }
