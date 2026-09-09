"""
Game 3: Chaos Race (arcade/games/chaos_race.py)

Player predicts whether a tiny parameter perturbation will cause trajectories to remain close or diverge.
Connected directly to Chaos Master Stroke.
"""

from typing import Dict, Any, Optional
from arcade.game import Game
from arcade.prediction import PredictionEvaluator
from arcade.scoring import ArcadeScoring
from chaos.experiment import master_stroke_experiment


class ChaosRaceGame(Game):
    def __init__(self):
        super().__init__(
            game_id="chaos_race",
            title="Chaos Race",
            description="Predict whether a tiny parameter perturbation will diverge over time.",
            learning_objective="Explore sensitivity to initial conditions and trajectory divergence.",
            difficulty_level=2,
        )

    def run(
        self,
        params: Dict[str, Any],
        prediction: Optional[str] = None,
        seed: Optional[int] = 42,
    ) -> Dict[str, Any]:
        param_name = str(params.get("parameter", "frequency"))
        delta = float(params.get("delta", 0.000001))
        freq = float(params.get("frequency", 1.0))

        base_params = {"frequency": freq, "intensity": 1.0, "chaos": 0.01}
        exp_res = master_stroke_experiment(
            base_params=base_params,
            parameter=param_name,
            delta=delta,
            iterations=30,
            seed=seed,
        )

        max_diff = exp_res["metrics"]["max_diff"]
        pred_res = PredictionEvaluator.evaluate(prediction or "", "diverge", max_diff)
        score = ArcadeScoring.calculate_score(pred_res["status"], difficulty_level=2)

        return {
            "game_id": self.game_id,
            "title": self.title,
            "master_stroke_data": exp_res,
            "prediction_evaluation": pred_res,
            "score": score,
            "explanations": {
                "simple": f"Perturbing '{param_name}' by +{delta:.8f} caused max trajectory divergence of {max_diff:.6f}.",
                "mathematical": f"delta_{param_name} = {delta} => max|W_base - W_pert| = {max_diff:.6f}",
                "research": exp_res["metrics"],
            },
        }
