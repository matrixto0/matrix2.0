"""
Game 1: Wave Runner (arcade/games/wave_runner.py)

Player controls frequency, intensity, phase to predict waveform changes.
"""

from typing import Dict, Any, Optional
from arcade.game import Game
from arcade.prediction import PredictionEvaluator
from arcade.scoring import ArcadeScoring
from arcade.missions import validate_mission
from matrix_core import MatrixState
from matrix_dynamics import step_dynamics
from visual.wave_data import WaveVisualization


class WaveRunnerGame(Game):
    def __init__(self):
        super().__init__(
            game_id="wave_runner",
            title="Wave Runner",
            description="Predict how modifying frequency, intensity, and phase changes the waveform.",
            learning_objective="Understand frequency oscillation rate, amplitude intensity, and phase shift.",
            difficulty_level=1,
        )

    def run(
        self,
        params: Dict[str, Any],
        prediction: Optional[str] = None,
        seed: Optional[int] = 42,
    ) -> Dict[str, Any]:
        freq = float(params.get("frequency", 1.0))
        inten = float(params.get("intensity", 1.0))
        ph = float(params.get("phase", 0.0))

        state = MatrixState(frequency=freq, intensity=inten, phase=ph)
        wave_vis = WaveVisualization(state).to_dict(steps=20, dt=0.01)

        val_delta = wave_vis["points"][-1]["value"] - wave_vis["points"][0]["value"]
        pred_res = PredictionEvaluator.evaluate(prediction or "", "change", val_delta)

        m_context = {
            "prediction": prediction,
            "max_divergence": abs(val_delta),
        }
        mission_completed = validate_mission("predict_before_run", m_context)
        score = ArcadeScoring.calculate_score(pred_res["status"], mission_completed=mission_completed)

        return {
            "game_id": self.game_id,
            "title": self.title,
            "parameters": state.describe(),
            "prediction_evaluation": pred_res,
            "wave_points": wave_vis["points"],
            "score": score,
            "explanations": {
                "simple": f"Wave oscillates at frequency {freq:.2f} Hz with peak intensity {inten:.2f}.",
                "mathematical": f"W(t) = {inten:.4f} * sin(2*pi*{freq:.4f}*t + {ph:.4f})",
                "research": {"state": state.describe(), "seed": seed, "dt": 0.01},
            },
        }
