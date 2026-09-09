"""
MATRIX2.0 Arcade Prediction Evaluator

Evaluates user predictions against simulation observations.
Statuses: confirmed, partially confirmed, not confirmed.
"""

from typing import Dict, Any, Optional


class PredictionEvaluator:
    """
    Evaluates predictions against simulation results.
    """

    @staticmethod
    def evaluate(
        prediction_text: str,
        expected_trend: str,
        actual_value_delta: float,
    ) -> Dict[str, Any]:
        if not prediction_text or not isinstance(prediction_text, str):
            prediction_text = "No prediction provided."

        text_lower = prediction_text.lower()
        trend_lower = expected_trend.lower()

        # Check keyword matches
        match_keywords = ["increase", "faster", "stronger", "diverge", "shift", "change", "match", "higher", "more"]
        user_expected_change = any(kw in text_lower for kw in match_keywords)

        actual_did_change = abs(actual_value_delta) > 1e-5

        if user_expected_change and actual_did_change:
            status = "confirmed"
            explanation = "Your prediction correctly identified parameter impact on trajectory evolution."
        elif not user_expected_change and not actual_did_change:
            status = "confirmed"
            explanation = "Your prediction correctly anticipated trajectory stability."
        elif actual_did_change:
            status = "partially confirmed"
            explanation = "System state evolved as predicted, but magnitude differed from baseline."
        else:
            status = "not confirmed"
            explanation = "Observed trajectory did not exhibit predicted trend. Treat as a valuable learning event!"

        return {
            "prediction": prediction_text,
            "status": status,
            "actual_delta": round(actual_value_delta, 6),
            "explanation": explanation,
        }
