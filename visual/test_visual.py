"""
Unit tests for MATRIX2.0 Visual Universe modules:
- wave_data.py
- particle_data.py
- trajectory_data.py
- comparison_data.py
- visual_state.py
"""

import os
import json
import shutil
import tempfile
import unittest

from matrix_core import MatrixState
from matrix_particles import ParticleField, MatrixParticle
from visual.wave_data import WaveVisualization
from visual.particle_data import ParticleVisualization
from visual.trajectory_data import TrajectoryVisualization
from visual.comparison_data import ComparisonVisualization
from visual.visual_state import (
    get_visual_preset,
    change_one_parameter,
    export_visualization_json,
    export_visualization_csv,
    VISUAL_PRESETS,
)


class TestWaveVisualization(unittest.TestCase):
    def test_wave_points_generation(self):
        state = MatrixState(frequency=1.0, intensity=2.0)
        wv = WaveVisualization(state)
        data = wv.to_dict(steps=10, dt=0.01)

        self.assertEqual(len(data["points"]), 10)
        self.assertIn("t", data["points"][0])
        self.assertIn("value", data["points"][0])

    def test_invalid_steps(self):
        wv = WaveVisualization()
        with self.assertRaises(ValueError):
            wv.generate_points(steps=0)


class TestParticleVisualization(unittest.TestCase):
    def test_particle_nodes_generation(self):
        field = ParticleField()
        p1 = MatrixParticle(value=0.5, intensity=1.0, phase=0.0)
        field.add_particle(p1)

        pv = ParticleVisualization(field)
        data = pv.to_dict()

        self.assertEqual(data["particle_count"], 1)
        node = data["particles"][0]
        self.assertIn("x", node)
        self.assertIn("y", node)
        self.assertEqual(node["x"], 1.0)


class TestTrajectoryVisualization(unittest.TestCase):
    def test_trajectory_generation(self):
        state = MatrixState(frequency=1.0, intensity=1.0)
        tv = TrajectoryVisualization(state)
        data = tv.to_dict(steps=5, dt=0.01)

        self.assertEqual(len(data["trajectory"]), 5)
        self.assertIn("time", data["trajectory"][0])


class TestComparisonAndVisualState(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_comparison_visualization(self):
        s_base = MatrixState(frequency=1.0, intensity=1.0)
        s_pert = MatrixState(frequency=1.5, intensity=1.0)

        cv = ComparisonVisualization(s_base, s_pert, steps=10, dt=0.01)
        data = cv.compare()

        self.assertIn("frequency", data["changed_parameters"])
        self.assertIn("maximum_divergence", data)

    def test_visual_presets(self):
        preset = get_visual_preset("CALM_WAVE")
        self.assertEqual(preset["params"]["chaos"], 0.0)

        with self.assertRaises(ValueError):
            get_visual_preset("INVALID_PRESET")

    def test_change_one_parameter_and_export(self):
        s_base = MatrixState(frequency=1.0, intensity=1.0)
        res = change_one_parameter(s_base, parameter="frequency", delta=0.1, steps=10, seed=42)

        self.assertIn("comparison", res)
        self.assertIn("explanations", res)

        json_file = os.path.join(self.temp_dir, "vis.json")
        csv_file = os.path.join(self.temp_dir, "vis.csv")

        export_visualization_json(res, json_file)
        export_visualization_csv(res, csv_file)

        self.assertTrue(os.path.exists(json_file))
        self.assertTrue(os.path.exists(csv_file))


if __name__ == "__main__":
    unittest.main()
