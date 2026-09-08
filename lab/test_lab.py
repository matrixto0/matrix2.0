"""
Unit tests for MATRIX2.0 Living Lab modules:
- pipeline.py
- session.py
- metrics.py
- state_view.py
- lessons.py
- achievements.py
"""

import os
import json
import shutil
import tempfile
import unittest

from matrix_core import MatrixState
from lab.pipeline import MatrixPipeline, MatrixLab
from lab.session import MatrixSession, save_experiment, load_experiment, reproduce_experiment
from lab.metrics import DiscoveryResult, what_changed
from lab.state_view import beginner_view, deep_view, generate_report
from lab.lessons import get_lesson, run_prediction_check, LAB_LESSONS
from lab.achievements import LabAchievementTracker


class TestLabPipeline(unittest.TestCase):
    def test_pipeline_encode_decode(self):
        p = MatrixPipeline()
        enc = p.encode("MOTHER")
        dec = p.decode(enc)
        self.assertEqual(dec, "MOTHER")

    def test_pipeline_create_state_and_simulate(self):
        p = MatrixPipeline()
        state = p.create_state("MOTHER")
        traj = p.simulate(state, steps=10)
        self.assertEqual(len(traj), 10)

    def test_matrix_lab_explore(self):
        lab = MatrixLab(seed=42)
        res = lab.explore("MOTHER")
        self.assertIn("what_started_with", res)
        self.assertIn("chaos_experiment_measured", res)


class TestLabSessionSerialization(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_save_load_reproduce_session(self):
        session = MatrixSession(input_text="MOTHER", seed=42)
        json_path = os.path.join(self.temp_dir, "session.json")

        save_experiment(session, json_path)
        loaded = load_experiment(json_path)
        self.assertEqual(loaded["input_text"], "MOTHER")

        repro = reproduce_experiment(json_path)
        self.assertTrue(repro["reproduced"])


class TestLabMetrics(unittest.TestCase):
    def test_discovery_result(self):
        s1 = MatrixState(value=0.0)
        s2 = MatrixState(value=1.5)
        traj = [{"value": 0.0}, {"value": 1.5}]
        dr = DiscoveryResult(s1, s2, traj, divergence_metric=0.1)

        self.assertEqual(dr.metrics["absolute_change"], 1.5)
        self.assertEqual(dr.metrics["trajectory_length"], 2)

    def test_what_changed(self):
        b = {"frequency": 1.0, "intensity": 1.0}
        a = {"frequency": 2.5, "intensity": 1.0}
        diff_info = what_changed(b, a)

        self.assertEqual(diff_info["most_changed_parameter"], "frequency")
        self.assertEqual(diff_info["max_difference"], 1.5)


class TestLabStateView(unittest.TestCase):
    def test_views_and_report(self):
        s = MatrixState(value=0.5, frequency=1.2, intensity=0.8).describe()
        b_str = beginner_view(s)
        d_str = deep_view(s)

        self.assertIn("0.5000", b_str)
        self.assertIn("x=0.500000", d_str)

        session_dict = MatrixSession(input_text="MOTHER", seed=42).to_dict()
        report = generate_report(session_dict)
        self.assertIn("[DATA - INPUT & ENCODING]", report)
        self.assertIn("[INTERPRETATION & EXPLANATION]", report)


class TestLabLessonsAndAchievements(unittest.TestCase):
    def test_all_10_lessons(self):
        self.assertEqual(len(LAB_LESSONS), 10)
        les1 = get_lesson(1)
        self.assertIsNotNone(les1)
        self.assertEqual(les1.number, 1)

    def test_prediction_check(self):
        pred_res = run_prediction_check("Increasing frequency will make wave faster", "frequency", 1.2)
        self.assertEqual(pred_res["status"], "confirmed")

    def test_achievement_tracker(self):
        tracker = LabAchievementTracker()
        tracker.record_prediction_outcome(confirmed=True)
        self.assertTrue(tracker.is_unlocked("FIRST_PREDICTION"))
        self.assertTrue(tracker.is_unlocked("FIRST_SUCCESSFUL_PREDICTION"))

        tracker.record_prediction_outcome(confirmed=False)
        self.assertTrue(tracker.is_unlocked("FIRST_FAILED_PREDICTION"))


if __name__ == "__main__":
    unittest.main()
