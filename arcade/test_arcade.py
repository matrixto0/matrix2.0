"""
Unit tests for MATRIX2.0 Simulation Arcade modules and all 7 games.
"""

import os
import json
import shutil
import tempfile
import unittest

from arcade.game import Game
import arcade.games  # Ensure all games are registered
from arcade.registry import REGISTRY
from arcade.prediction import PredictionEvaluator
from arcade.scoring import ArcadeScoring
from arcade.missions import validate_mission, list_missions


class TestArcadeCore(unittest.TestCase):
    def test_registry_games_count(self):
        games = REGISTRY.list_games()
        self.assertEqual(len(games), 7)

    def test_prediction_evaluator(self):
        eval_res = PredictionEvaluator.evaluate(
            prediction_text="I predict frequency increase",
            expected_trend="increase",
            actual_value_delta=0.5,
        )
        self.assertEqual(eval_res["status"], "confirmed")

    def test_arcade_scoring(self):
        score_info = ArcadeScoring.calculate_score("confirmed", mission_completed=True, difficulty_level=2)
        self.assertGreater(score_info["total_score"], 50)

    def test_mission_validation(self):
        ctx = {"prediction": "I predict wave will change"}
        self.assertTrue(validate_mission("predict_before_run", ctx))


class TestArcadeGames(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_wave_runner(self):
        game = REGISTRY.get_game("wave_runner")
        self.assertIsNotNone(game)
        res = game.run({"frequency": 2.0}, prediction="increase", seed=42)
        self.assertEqual(res["game_id"], "wave_runner")

        json_file = os.path.join(self.temp_dir, "wr.json")
        game.export_json(res, json_file)
        self.assertTrue(os.path.exists(json_file))

    def test_phase_shift(self):
        game = REGISTRY.get_game("phase_shift")
        res = game.run({"phase_shift": 1.57}, seed=42)
        self.assertEqual(res["game_id"], "phase_shift")

    def test_chaos_race(self):
        game = REGISTRY.get_game("chaos_race")
        res = game.run({"parameter": "frequency", "delta": 0.0001}, seed=42)
        self.assertEqual(res["game_id"], "chaos_race")

    def test_particle_dance(self):
        game = REGISTRY.get_game("particle_dance")
        res = game.run({"particle_count": 5}, seed=42)
        self.assertEqual(res["game_id"], "particle_dance")

    def test_resonance_lab(self):
        game = REGISTRY.get_game("resonance_lab")
        res = game.run({"frequency_1": 1.0, "frequency_2": 1.0}, seed=42)
        self.assertTrue(res["frequency_matched"])

    def test_pattern_hunter(self):
        game = REGISTRY.get_game("pattern_hunter")
        res = game.run({"frequency": 1.5}, seed=42)
        self.assertEqual(len(res["sequence"]), 10)

    def test_state_transformer(self):
        game = REGISTRY.get_game("state_transformer")
        res = game.run({"text": "MOTHER"}, seed=42)
        self.assertTrue(res["lossless_reconstruction"])


if __name__ == "__main__":
    unittest.main()
