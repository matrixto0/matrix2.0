"""
Game 4: Particle Dance (arcade/games/particle_dance.py)

Generates particle fields and visualizes state evolution.
"""

from typing import Dict, Any, Optional
from arcade.game import Game
from arcade.prediction import PredictionEvaluator
from arcade.scoring import ArcadeScoring
from matrix_core import MatrixState
from lab.pipeline import MatrixPipeline
from visual.particle_data import ParticleVisualization


class ParticleDanceGame(Game):
    def __init__(self):
        super().__init__(
            game_id="particle_dance",
            title="Particle Dance",
            description="Observe multi-particle field evolution under frequency, intensity, and chaos settings.",
            learning_objective="Understand collective particle state evolution and field aggregation.",
            difficulty_level=2,
        )

    def run(
        self,
        params: Dict[str, Any],
        prediction: Optional[str] = None,
        seed: Optional[int] = 42,
    ) -> Dict[str, Any]:
        count = int(params.get("particle_count", 5))
        freq = float(params.get("frequency", 1.2))

        pipeline = MatrixPipeline(seed=seed)
        state = MatrixState(frequency=freq, intensity=1.0, chaos=0.01)

        field = pipeline.create_particles(state, count=count, seed=seed)
        initial_avg = field.get_average_value()
        field.step_field(t=0.2, dt=0.01)
        evolved_avg = field.get_average_value()

        part_vis = ParticleVisualization(field).to_dict()
        pred_res = PredictionEvaluator.evaluate(prediction or "", "shift", abs(evolved_avg - initial_avg))
        score = ArcadeScoring.calculate_score(pred_res["status"], difficulty_level=2)

        return {
            "game_id": self.game_id,
            "title": self.title,
            "particle_count": count,
            "initial_average_value": initial_avg,
            "evolved_average_value": evolved_avg,
            "particle_visualization": part_vis,
            "prediction_evaluation": pred_res,
            "score": score,
            "explanations": {
                "simple": f"A field of {count} particles evolved smoothly, shifting mean value from {initial_avg:.4f} to {evolved_avg:.4f}.",
                "mathematical": f"Field mean W_avg(t=0.2) = {evolved_avg:.6f}",
                "research": part_vis,
            },
        }
