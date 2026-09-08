"""
Unit tests for high-level matrix_lab.py public API.
"""

import os
import json
import shutil
import tempfile
import unittest

from matrix_lab import (
    MatrixLab,
    calculate_discovery_score,
    generate_aha_moment,
    save_experiment_data,
    load_experiment_data,
    reproduce_experiment_data,
)


class TestMatrixLabAPI(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.lab = MatrixLab(seed=42)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_explore_pipeline(self):
        res = self.lab.explore("MOTHER")
        self.assertEqual(res["input"], "MOTHER")
        self.assertEqual(res["encoded_values"], [77, 79, 84, 72, 69, 82])
        self.assertIn("discovery_score", res)
        self.assertIn("beginner_mode", res)
        self.assertIn("deep_mode", res)
        self.assertIn("research_mode", res)
        self.assertIn("visualization_data", res)
        self.assertIn("experiment_card", res)

    def test_ask_question(self):
        res = self.lab.ask("What happens if frequency increases?", base_text="MOTHER")
        self.assertEqual(res["parameter_tested"], "frequency")
        self.assertIn("max_trajectory_diff", res)
        self.assertIn("aha_moment", res)

    def test_ask_intensity_zero(self):
        res = self.lab.ask("What happens if intensity becomes zero?", base_text="MOTHER")
        self.assertEqual(res["parameter_tested"], "intensity")

    def test_predict(self):
        pred_res = self.lab.predict("I predict wave value will change", base_text="MOTHER")
        self.assertIn("prediction", pred_res)
        self.assertIn("result", pred_res)

    def test_save_load_reproduce(self):
        exp_dict = self.lab.explore("MOTHER")
        filepath = os.path.join(self.temp_dir, "test_exp.json")

        save_experiment_data(exp_dict, filepath)
        self.assertTrue(os.path.exists(filepath))

        loaded = load_experiment_data(filepath)
        self.assertEqual(loaded["input"], "MOTHER")

        repro_res = reproduce_experiment_data(filepath)
        self.assertTrue(repro_res["reproduced"])

    def test_discovery_score_calculation(self):
        score = calculate_discovery_score(max_diff=0.5, avg_diff=0.2, reproducible=True)
        self.assertGreater(score, 0.0)
        self.assertLessEqual(score, 100.0)

        unrepro_score = calculate_discovery_score(max_diff=0.5, avg_diff=0.2, reproducible=False)
        self.assertEqual(unrepro_score, 0.0)


if __name__ == "__main__":
    unittest.main()
