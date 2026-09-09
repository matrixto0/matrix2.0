"""
Unit tests for MATRIX2.0 Explorer modules:
- concepts.py
- experiments.py
- explanations.py
- challenges.py
"""

import math
import unittest

from matrix_core import MatrixState
from matrix_particles import ParticleField
from explorer.concepts import Concept, get_concept, CORE_CONCEPTS
from explorer.experiments import (
    exp_1_frequency_change,
    exp_2_intensity_change,
    exp_3_phase_change,
    exp_4_chaos_disruption,
    exp_5_wave_interaction,
    exp_6_word_to_numbers,
    exp_7_numbers_to_dynamic_state,
    exp_8_particle_field_evolution,
)
from explorer.explanations import (
    explain_state_params,
    WhatIfEngine,
    calculate_complexity_score,
    AchievementTracker,
)
from explorer.challenges import get_challenge, LEARNING_CHALLENGES


class TestExplorerConcepts(unittest.TestCase):
    def test_get_concept(self):
        c = get_concept("frequency")
        self.assertIsNotNone(c)
        self.assertEqual(c.name, "Frequency")
        self.assertIn("repeats", c.beginner_description)

    def test_all_12_concepts_present(self):
        expected_keys = {
            "value", "frequency", "intensity", "phase", "wave",
            "chaos", "variation", "particle", "state", "transformation",
            "encoding", "decoding"
        }
        self.assertTrue(expected_keys.issubset(set(CORE_CONCEPTS.keys())))


class TestExplorerExperiments(unittest.TestCase):
    def test_exp_1_frequency_change(self):
        res = exp_1_frequency_change(0.5, 2.0)
        self.assertIn("wave_a", res)
        self.assertIn("wave_b", res)

    def test_exp_2_intensity_change(self):
        res = exp_2_intensity_change(0.5, 2.5)
        self.assertGreater(abs(res["peak_b"]), abs(res["peak_a"]))

    def test_exp_3_phase_change(self):
        res = exp_3_phase_change(math.pi)
        self.assertAlmostEqual(res["initial_val_zero_phase"], 0.0, places=5)

    def test_exp_6_word_to_numbers(self):
        res = exp_6_word_to_numbers("MOTHER")
        self.assertEqual(res["ascii_numbers"], [77, 79, 84, 72, 69, 82])

    def test_exp_8_particle_field_evolution(self):
        res = exp_8_particle_field_evolution(particle_count=5, seed=42)
        self.assertEqual(res["particle_count"], 5)


class TestExplorerExplanations(unittest.TestCase):
    def test_explain_state_params(self):
        expl = explain_state_params(1.0, 2.0)
        self.assertIn("simple", expl)
        self.assertIn("mathematical", expl)

    def test_what_if_engine(self):
        state = MatrixState(frequency=1.0, intensity=1.0)
        res = WhatIfEngine.what_if_frequency_doubles(state)
        self.assertEqual(res["new_frequency"], 2.0)

    def test_calculate_complexity_score(self):
        state = MatrixState(frequency=1.0, intensity=1.0, chaos=0.01, variation=0.01)
        score_info = calculate_complexity_score(state, particle_count=5)
        self.assertGreater(score_info["score"], 40.0)
        self.assertIn(score_info["level"], ["Intermediate", "Advanced", "Research"])

    def test_achievement_tracker(self):
        tracker = AchievementTracker()
        unlocked = tracker.unlock("FIRST_WAVE")
        self.assertTrue(unlocked)
        self.assertTrue(tracker.is_unlocked("FIRST_WAVE"))
        self.assertFalse(tracker.unlock("FIRST_WAVE"))  # Duplicate unlock returns False


class TestExplorerChallenges(unittest.TestCase):
    def test_challenge_validation(self):
        ch = get_challenge("faster_wave")
        self.assertIsNotNone(ch)
        self.assertTrue(ch.validate(MatrixState(frequency=2.5)))
        self.assertFalse(ch.validate(MatrixState(frequency=1.0)))

    def test_encode_mother_challenge(self):
        ch = get_challenge("encode_mother")
        self.assertTrue(ch.validate("MOTHER", [77, 79, 84, 72, 69, 82]))


if __name__ == "__main__":
    unittest.main()
