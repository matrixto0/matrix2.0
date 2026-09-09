"""
Game 2: Phase Shift (arcade/games/phase_shift.py)

Gives the user two waves and allows phase changes to compare alignment/periodicity.
"""

import math
from typing import Dict, Any, Optional
from arcade.game import Game
from arcade.prediction import PredictionEvaluator
from arcade.scoring import ArcadeScoring
from matrix_core import MatrixState
from visual.comparison_data import ComparisonVisualization


class PhaseShiftGame(Game):
    def __init__(self):
        super().__init__(
            game_id="phase_shift",
            title="Phase Shift",
            description="Adjust phase shift between two waves and observe alignment changes.",
            learning_objective="Learn phase displacement, wave alignment, and constructive/destructive superposition.",
            difficulty_level=2,
        )

    def run(
        self,
        params: Dict[str, Any],
        prediction: Optional[str] = None,
        seed: Optional[int] = 42,
    ) -> Dict[str, Any]:
        shift = float(params.get("phase_shift", math.pi))
        freq = float(params.get("frequency", 1.0))

        s1 = MatrixState(frequency=freq, intensity=1.0, phase=0.0)
        s2 = MatrixState(frequency=freq, intensity=1.0, phase=shift)

        comp = ComparisonVisualization(s1, s2, steps=20, dt=0.01, seed=seed).compare()
        max_diff = comp["maximum_divergence"]

        pred_res = PredictionEvaluator.evaluate(prediction or "", "shift", max_diff)
        score = ArcadeScoring.calculate_score(pred_res["status"], difficulty_level=2)

        return {
            "game_id": self.game_id,
            "title": self.title,
            "phase_shift_applied": shift,
            "comparison": comp,
            "prediction_evaluation": pred_res,
            "score": score,
            "explanations": {
                "simple": f"Shifting phase by {shift:.2f} rad changed wave starting displacement, resulting in max difference {max_diff:.4f}.",
                "mathematical": f"W1(t) = sin(2*pi*{freq}*t), W2(t) = sin(2*pi*{freq}*t + {shift:.4f})",
                "research": {"phase_shift": shift, "metrics": comp},
            },
        }
