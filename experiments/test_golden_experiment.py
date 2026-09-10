"""
Unit tests for experiments/golden_experiment.py.
"""

import unittest
from experiments.golden_experiment import execute_golden_experiment, GoldenExperiment
from matrix_core import MatrixState


class TestGoldenExperiment(unittest.TestCase):

    def test_golden_experiment_reproducibility(self):
        res1 = execute_golden_experiment()
        res2 = execute_golden_experiment()

        self.assertEqual(res1["experiment_id"], res2["experiment_id"])
        self.assertEqual(res1["metrics"], res2["metrics"])
        self.assertEqual(res1["seed"], res2["seed"])

    def test_golden_experiment_metrics(self):
        res = execute_golden_experiment()
        metrics = res["metrics"]

        self.assertIn("baseline_mean_energy", metrics)
        self.assertIn("matrix_mean_energy", metrics)
        self.assertIn("variance_ratio_matrix_to_baseline", metrics)
        self.assertIn("disclaimer", res)


if __name__ == "__main__":
    unittest.main()
