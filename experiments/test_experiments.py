"""
Comprehensive unit tests for MATRIX2.0 Reproducible Experiment Engine.
"""

import json
import unittest
from experiments.configuration import ExperimentConfig
from experiments.experiment import Experiment
from experiments.statistics import mean, median, min_val, max_val, variance, std_dev, range_val, calculate_summary_stats
from experiments.runner import ExperimentRunner, generate_parameter_sweeps
from experiments.reproducibility import check_reproducibility
from experiments.comparison import compare_results, compare_multiple
from experiments.results import generate_experiment_report
from experiments.registry import register_experiment, get_experiment, list_experiments, run_experiment


class TestExperimentEngine(unittest.TestCase):

    def test_configuration_serialization(self):
        cfg = ExperimentConfig(
            experiment_id="test_exp",
            name="Test Experiment",
            description="Testing serialization",
            model="wave_stability",
            parameters={"frequency": 2.0, "intensity": 1.5},
            seed=123,
            iterations=50
        )
        json_str = cfg.to_json()
        restored = ExperimentConfig.from_json(json_str)

        self.assertEqual(restored.experiment_id, "test_exp")
        self.assertEqual(restored.parameters["frequency"], 2.0)
        self.assertEqual(restored.seed, 123)

    def test_statistics_functions(self):
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.assertEqual(mean(data), 3.0)
        self.assertEqual(median(data), 3.0)
        self.assertEqual(min_val(data), 1.0)
        self.assertEqual(max_val(data), 5.0)
        self.assertEqual(range_val(data), 4.0)
        self.assertAlmostEqual(variance(data), 2.0)
        self.assertAlmostEqual(std_dev(data), 1.41421356, places=5)

    def test_deterministic_runner_reproducibility(self):
        cfg = ExperimentConfig(
            experiment_id="rep_test",
            name="Repro Test",
            description="Testing seed determinism",
            model="wave_stability",
            parameters={"frequency": 1.0, "chaos": 0.05},
            seed=42,
            iterations=50
        )
        runner = ExperimentRunner()
        exp_a = runner.run(cfg)
        exp_b = runner.run(cfg)

        repro_check = check_reproducibility(exp_a, exp_b)
        self.assertTrue(repro_check["reproducible"])
        self.assertEqual(exp_a.measurements["wave_values"], exp_b.measurements["wave_values"])

    def test_parameter_sweeps(self):
        base_cfg = ExperimentConfig(
            experiment_id="sweep_base",
            name="Sweep Base",
            description="Base for parameter sweep",
            model="wave_stability",
            parameters={"frequency": 1.0, "chaos": 0.0},
            seed=42
        )
        sweep_params = {"chaos": [0.00, 0.01], "variation": [0.00, 0.01]}
        configs = generate_parameter_sweeps(base_cfg, sweep_params)

        self.assertEqual(len(configs), 4)
        self.assertEqual(configs[0].parameters["chaos"], 0.00)
        self.assertEqual(configs[0].parameters["variation"], 0.00)

    def test_comparison_and_reports(self):
        runner = ExperimentRunner()
        cfg_a = ExperimentConfig("exp_a", "Exp A", "Desc", "wave_stability", {"frequency": 1.0, "chaos": 0.0})
        cfg_b = ExperimentConfig("exp_b", "Exp B", "Desc", "wave_stability", {"frequency": 2.0, "chaos": 0.05})

        exp_a = runner.run(cfg_a)
        exp_b = runner.run(cfg_b)

        comp = compare_results(exp_a, exp_b)
        self.assertEqual(comp["parameter_differences"]["frequency_difference"], 1.0)

        report = generate_experiment_report(exp_a, comparison_target=exp_b)
        self.assertIn("MATRIX2.0 EXPERIMENT REPORT", report)
        self.assertIn("SCIENTIFIC INTERPRETATION & BOUNDS", report)

    def test_registry_and_presets(self):
        registered = list_experiments()
        self.assertIn("wave_stability", registered)
        self.assertIn("chaos_divergence", registered)

        exp = run_experiment("wave_stability", overrides={"iterations": 20})
        self.assertEqual(exp.iterations, 20)


if __name__ == "__main__":
    unittest.main()
