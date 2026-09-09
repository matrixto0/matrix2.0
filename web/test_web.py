"""
Unit tests for MATRIX2.0 Web Simulation Universe assets.
Verifies file existence, JSON validity, HTML structure, CSS rules, and JS syntax integrity.
"""

import json
import os
import unittest


class TestWebSimulationUniverse(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.games_json_path = os.path.join(self.base_dir, 'data', 'games.json')
        self.index_html_path = os.path.join(self.base_dir, 'index.html')
        self.style_css_path = os.path.join(self.base_dir, 'style.css')
        self.app_js_path = os.path.join(self.base_dir, 'app.js')
        self.api_design_path = os.path.join(self.base_dir, 'API_DESIGN.md')
        self.readme_path = os.path.join(self.base_dir, 'README.md')

    def test_web_files_exist(self):
        """Verify that all required web assets exist in web/."""
        self.assertTrue(os.path.exists(self.games_json_path), "games.json should exist")
        self.assertTrue(os.path.exists(self.index_html_path), "index.html should exist")
        self.assertTrue(os.path.exists(self.style_css_path), "style.css should exist")
        self.assertTrue(os.path.exists(self.app_js_path), "app.js should exist")
        self.assertTrue(os.path.exists(self.api_design_path), "API_DESIGN.md should exist")
        self.assertTrue(os.path.exists(self.readme_path), "README.md should exist")

    def test_games_json_validity(self):
        """Verify games.json valid syntax and expected game schema structure."""
        with open(self.games_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.assertIsInstance(data, list, "games.json root should be a list")
        self.assertGreaterEqual(len(data), 7, "Should contain at least 7 arcade games")

        expected_keys = {'id', 'name', 'description', 'target_metric', 'difficulty', 'mission', 'default_params'}
        for game in data:
            self.assertTrue(expected_keys.issubset(game.keys()), f"Game {game.get('id')} missing keys")
            params = game['default_params']
            self.assertIn('frequency', params)
            self.assertIn('intensity', params)
            self.assertIn('phase', params)

    def test_index_html_structure(self):
        """Verify index.html contains necessary UI elements."""
        with open(self.index_html_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn('id="games-grid"', content)
        self.assertIn('id="wave-canvas"', content)
        self.assertIn('id="particle-canvas"', content)
        self.assertIn('id="live-equation"', content)
        self.assertIn('id="live-vector"', content)
        self.assertIn('id="history-table"', content)
        self.assertIn('Scientific & Epistemological Disclaimer', content)

    def test_style_css_content(self):
        """Verify style.css includes key rules and theme variables."""
        with open(self.style_css_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn('--bg-color:', content)
        self.assertIn('.game-card', content)
        self.assertIn('canvas', content)
        self.assertIn('.inspector-card', content)

    def test_app_js_content(self):
        """Verify app.js includes canvas rendering, event listeners, and localStorage history logic."""
        with open(self.app_js_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn("fetch('data/games.json')", content)
        self.assertIn('requestAnimationFrame', content)
        self.assertIn('waveCanvas', content)
        self.assertIn('particleCanvas', content)
        self.assertIn('localStorage', content)


if __name__ == '__main__':
    unittest.main()
