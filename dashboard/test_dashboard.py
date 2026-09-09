"""
Unit tests for Research Dashboard configurations and state representations.
"""

import unittest
import json
import os


class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.config_path = os.path.join(os.path.dirname(__file__), "data", "dashboard_config.json")

    def test_dashboard_config_exists_and_valid(self):
        self.assertTrue(os.path.exists(self.config_path))
        with open(self.config_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data["title"], "MATRIX2.0 Research Dashboard")
        self.assertIn("subtitle", data)
        self.assertIn("architecture_layers", data)
        self.assertEqual(len(data["architecture_layers"]), 8)

    def test_architecture_layer_statuses(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        layers = data["architecture_layers"]
        layer_names = [layer["name"] for layer in layers]
        expected_names = ["Text", "Encoding", "State", "Dynamics", "Particles", "Chaos", "Experiments", "Visualization"]
        self.assertEqual(layer_names, expected_names)

        for layer in layers:
            self.assertEqual(layer["status"], "Implemented")

    def test_dashboard_disclaimer_present(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("disclaimer", data)
        self.assertIn("physical causation", data["disclaimer"])


if __name__ == "__main__":
    unittest.main()
