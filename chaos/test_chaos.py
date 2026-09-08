"""
Unit tests for MATRIX2.0 Chaos Master Stroke module:
- presets.py
- chaos_engine.py
- attractor.py
- sensitivity.py
- experiment.py
"""

import os
import json
import shutil
import tempfile
import unittest

from chaos.presets import get_preset, CHAOS_PRESETS
from chaos.chaos_engine import ChaosEngine
from chaos.attractor import ComputationalAttractor
from chaos.sensitivity import analyze_sensitivity, compute_trajectory_divergence
from chaos.experiment import (
    master_stroke_experiment,
    calculate_surprise_score,
    export_experiment_json,
    export_experiment_csv,
)


class TestChaosPresets(unittest.TestCase):
    def test_get_valid_preset(self):
        calm = get_preset("CALM")
        self.assertEqual(calm["chaos"], 0.0)
        self.assertEqual(calm["variation"], 0.0)

    def test_get_invalid_preset(self):
        with self.assertRaises(ValueError):
            get_preset("INVALID_PRESET")


class TestChaosEngine(unittest.TestCase):
    def test_deterministic_seed_trajectories(self):
        engine1 = ChaosEngine(frequency=1.0, chaos=0.05, seed=42)
        engine2 = ChaosEngine(frequency=1.0, chaos=0.05, seed=42)

        traj1 = engine1.generate_trajectory(iterations=20)
        traj2 = engine2.generate_trajectory(iterations=20)

        for p1, p2 in zip(traj1, traj2):
            self.assertEqual(p1["value"], p2["value"])
            self.assertEqual(p1["frequency"], p2["frequency"])

    def test_invalid_iterations(self):
        engine = ChaosEngine()
        with self.assertRaises(ValueError):
            engine.generate_trajectory(iterations=0)


class TestComputationalAttractor(unittest.TestCase):
    def test_attractor_summary(self):
        engine = ChaosEngine(frequency=1.0, intensity=2.0, seed=42)
        traj = engine.generate_trajectory(iterations=10)
        attractor = ComputationalAttractor(
            trajectory=traj, parameters={"frequency": 1.0, "intensity": 2.0}, seed=42
        )

        summary = attractor.summary_statistics
        self.assertIn("min_value", summary)
        self.assertIn("max_value", summary)
        self.assertIn("avg_value", summary)
        self.assertEqual(attractor.iterations, 10)


class TestSensitivityAndExperiment(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_sensitivity_analysis(self):
        base_params = {"value": 0.0, "frequency": 1.0, "intensity": 1.0, "chaos": 0.01}
        res = analyze_sensitivity(
            base_params=base_params, parameter="frequency", delta=0.0001, iterations=20, seed=42
        )
        self.assertEqual(res["parameter"], "frequency")
        self.assertIn("metrics", res)
        self.assertIn("max_diff", res["metrics"])

    def test_invalid_parameter_sensitivity(self):
        base_params = {"frequency": 1.0}
        with self.assertRaises(ValueError):
            analyze_sensitivity(base_params=base_params, parameter="invalid_param")

    def test_master_stroke_experiment_and_export(self):
        base_params = {"frequency": 1.0, "intensity": 1.0, "chaos": 0.01}
        exp_data = master_stroke_experiment(
            base_params=base_params, parameter="frequency", delta=0.0001, iterations=10, seed=42
        )

        self.assertIn("surprise_score", exp_data)
        self.assertIn("explanation", exp_data)

        json_path = os.path.join(self.temp_dir, "exp.json")
        csv_path = os.path.join(self.temp_dir, "exp.csv")

        export_experiment_json(exp_data, json_path)
        export_experiment_csv(exp_data, csv_path)

        self.assertTrue(os.path.exists(json_path))
        self.assertTrue(os.path.exists(csv_path))

        with open(json_path, "r", encoding="utf-8") as f:
            loaded_json = json.load(f)
            self.assertEqual(loaded_json["experiment_title"], "MATRIX2.0 Master Stroke Experiment")


if __name__ == "__main__":
    unittest.main()
