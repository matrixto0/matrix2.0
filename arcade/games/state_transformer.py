"""
Game 7: State Transformer (arcade/games/state_transformer.py)

Preserves information through text -> numbers -> state -> transformation -> numbers -> text pipeline.
"""

from typing import Dict, Any, Optional
from arcade.game import Game
from arcade.prediction import PredictionEvaluator
from arcade.scoring import ArcadeScoring
from matrix_encode import encode_text
from matrix_decode import decode_values
from matrix_core import MatrixState


class StateTransformerGame(Game):
    def __init__(self):
        super().__init__(
            game_id="state_transformer",
            title="State Transformer",
            description="Transform text through encoding, state vector creation, and lossless decoding.",
            learning_objective="Learn text encoding, state representation, and lossless symbolic decoding.",
            difficulty_level=1,
        )

    def run(
        self,
        params: Dict[str, Any],
        prediction: Optional[str] = None,
        seed: Optional[int] = 42,
    ) -> Dict[str, Any]:
        text = str(params.get("text", "MOTHER")).strip() or "MOTHER"

        encoded = encode_text(text)
        decoded = decode_values(encoded)

        state = MatrixState(
            value=sum(encoded) / len(encoded) / 100.0 if encoded else 0.0,
            frequency=len(text) / 5.0 if text else 1.0,
            intensity=max(encoded) / 100.0 if encoded else 1.0,
        )

        lossless = text == decoded
        pred_res = PredictionEvaluator.evaluate(prediction or "", "match", 0.0 if lossless else 1.0)
        score = ArcadeScoring.calculate_score(pred_res["status"], difficulty_level=1)

        return {
            "game_id": self.game_id,
            "title": self.title,
            "original_text": text,
            "encoded_numbers": encoded,
            "constructed_state": state.describe(),
            "decoded_text": decoded,
            "lossless_reconstruction": lossless,
            "prediction_evaluation": pred_res,
            "score": score,
            "explanations": {
                "simple": f"The text '{text}' was encoded into ASCII codes {encoded}, mapped into a MatrixState vector, and decoded back into '{decoded}'.",
                "mathematical": f"T_encode: String -> ASCII Array {encoded} -> MatrixState tuple M.",
                "research": {"input": text, "encoded": encoded, "reconstructed": decoded, "lossless": lossless},
            },
        }
