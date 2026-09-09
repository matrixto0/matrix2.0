"""
Game 6: Pattern Hunter (arcade/games/pattern_hunter.py)

Generates dynamic wave sequences and allows prediction/pattern discovery.
"""

from typing import Dict, Any, Optional
from arcade.game import Game
from arcade.prediction import PredictionEvaluator
from arcade.scoring import ArcadeScoring
from matrix_core import MatrixState
from matrix_dynamics import step_dynamics


class PatternHunterGame(Game):
    def __init__(self):
        super().__init__(
            game_id="pattern_hunter",
            title="Pattern Hunter",
            description="Discover periodic patterns and sequences in wave dynamics.",
            learning_objective="Explore numerical pattern recognition, sequence analysis, and wave trends.",
            difficulty_level=3,
        )

    def run(
        self,
        params: Dict[str, Any],
        prediction: Optional[str] = None,
        seed: Optional[int] = 42,
    ) -> Dict[str, Any]:
        freq = float(params.get("frequency", 1.5))
        state = MatrixState(frequency=freq, intensity=1.0)

        sequence = [round(step_dynamics(state, t=step * 0.05).value, 4) for step in range(10)]
        max_val = max(sequence)
        min_val = min(sequence)

        pred_res = PredictionEvaluator.evaluate(prediction or "", "pattern", max_val - min_val)
        score = ArcadeScoring.calculate_score(pred_res["status"], difficulty_level=3)

        return {
            "game_id": self.game_id,
            "title": self.title,
            "sequence": sequence,
            "sequence_range": round(max_val - min_val, 4),
            "prediction_evaluation": pred_res,
            "score": score,
            "explanations": {
                "simple": f"Wave dynamics generated sequence ranging between {min_val} and {max_val}.",
                "mathematical": f"Sequence generated via W(t_k) at t_k = k * 0.05s.",
                "research": {"sequence": sequence, "range": max_val - min_val},
            },
        }
