"""
Game 5: Resonance Lab (arcade/games/resonance_lab.py)

Simulates two oscillating systems, allowing users to match frequencies and measure correlation.
"""

from typing import Dict, Any, Optional
from arcade.game import Game
from arcade.prediction import PredictionEvaluator
from arcade.scoring import ArcadeScoring
from matrix_core import MatrixState
from matrix_dynamics import MatrixDynamics


class ResonanceLabGame(Game):
    def __init__(self):
        super().__init__(
            game_id="resonance_lab",
            title="Resonance Lab",
            description="Align frequencies between two oscillating wave systems and measure correlation.",
            learning_objective="Learn frequency matching, periodicity, and computational correlation.",
            difficulty_level=3,
        )

    def run(
        self,
        params: Dict[str, Any],
        prediction: Optional[str] = None,
        seed: Optional[int] = 42,
    ) -> Dict[str, Any]:
        f1 = float(params.get("frequency_1", 1.0))
        f2 = float(params.get("frequency_2", 1.0))

        s1 = MatrixState(frequency=f1, intensity=1.0)
        s2 = MatrixState(frequency=f2, intensity=1.0)

        e1 = MatrixDynamics(s1)
        e2 = MatrixDynamics(s2)

        vals1 = [e1.step(t=t * 0.01).value for t in range(20)]
        vals2 = [e2.step(t=t * 0.01).value for t in range(20)]

        diffs = [abs(v1 - v2) for v1, v2 in zip(vals1, vals2)]
        avg_diff = sum(diffs) / len(diffs) if diffs else 0.0

        # Correlation proxy: 1.0 - normalized average difference
        correlation = max(0.0, 1.0 - (avg_diff / 2.0))
        freq_matched = abs(f1 - f2) < 1e-4

        pred_res = PredictionEvaluator.evaluate(prediction or "", "match" if freq_matched else "change", correlation)
        score = ArcadeScoring.calculate_score(pred_res["status"], difficulty_level=3)

        return {
            "game_id": self.game_id,
            "title": self.title,
            "frequency_1": f1,
            "frequency_2": f2,
            "frequency_matched": freq_matched,
            "correlation_score": round(correlation, 4),
            "prediction_evaluation": pred_res,
            "score": score,
            "explanations": {
                "simple": f"Matching frequencies ({f1} Hz vs {f2} Hz) produced correlation score of {correlation:.2f}.",
                "mathematical": f"Correlation metric C = max(0, 1 - avg|W1 - W2| / 2) = {correlation:.4f}",
                "research": {"f1": f1, "f2": f2, "correlation": correlation},
            },
        }
