"""
Unit tests for research module (Hypothesis, Observation, Conclusion, Research Record).
"""

import unittest
import json
from research import Hypothesis, Observation, ObservationLogger, Conclusion


class TestResearchModule(unittest.TestCase):

    def test_hypothesis_serialization(self):
        hyp = Hypothesis(
            statement="Increasing frequency increases energy output.",
            variables={"frequency": 5.0, "intensity": 2.0},
            rationale="Higher frequency oscillations carry more kinetic energy."
        )
        data = hyp.to_dict()
        self.assertEqual(data["statement"], "Increasing frequency increases energy output.")
        self.assertEqual(data["variables"]["frequency"], 5.0)

        hyp_restored = Hypothesis.from_dict(data)
        self.assertEqual(hyp_restored.statement, hyp.statement)
        self.assertEqual(hyp_restored.variables, hyp.variables)
        self.assertEqual(hyp_restored.rationale, hyp.rationale)

    def test_observation_logger(self):
        logger = ObservationLogger()
        logger.record(step=1, data={"val": 1.5})
        logger.record(step=2, data={"val": 3.0})

        self.assertEqual(len(logger.observations), 2)
        summary = logger.get_summary()
        self.assertEqual(summary["count"], 2)
        self.assertEqual(summary["steps"], [1, 2])

        data = logger.to_dict()
        restored_logger = ObservationLogger.from_dict(data)
        self.assertEqual(len(restored_logger.observations), 2)
        self.assertEqual(restored_logger.observations[0].step, 1)
        self.assertEqual(restored_logger.observations[0].data["val"], 1.5)

    def test_conclusion_serialization(self):
        conc = Conclusion(
            validated=True,
            summary="Observed non-linear relationship consistent with hypothesis.",
            confidence_score=0.95,
            details={"metric_diff": 0.12}
        )
        data = conc.to_dict()
        self.assertTrue(data["validated"])
        self.assertEqual(data["confidence_score"], 0.95)

        conc_restored = Conclusion.from_dict(data)
        self.assertTrue(conc_restored.validated)
        self.assertEqual(conc_restored.summary, conc.summary)
        self.assertEqual(conc_restored.details, conc.details)

    def test_research_record_schema(self):
        record = {
            "hypothesis": "Test hypothesis",
            "experiment_id": "exp_001",
            "configuration": {"seed": 42, "iterations": 10},
            "seed": 42,
            "observations": [{"step": 1, "data": {"y": 0.5}}],
            "metrics": {"mean_y": 0.5},
            "interpretation": "Interpretation of model results.",
            "conclusion": "Hypothesis supported within model constraints."
        }
        serialized = json.dumps(record)
        deserialized = json.loads(serialized)
        self.assertEqual(deserialized["experiment_id"], "exp_001")
        self.assertEqual(deserialized["seed"], 42)


if __name__ == "__main__":
    unittest.main()
