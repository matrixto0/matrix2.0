"""
MATRIX2.0 Arcade Game Registry

Manages discovery and registration of simulation games.
"""

from typing import Dict, List, Optional, Any
from arcade.game import Game


class GameRegistry:
    """
    Central registry for MATRIX2.0 Arcade simulation games.
    """

    def __init__(self):
        self._games: Dict[str, Game] = {}

    def register(self, game: Game) -> None:
        """Register a simulation game instance."""
        self._games[game.game_id] = game

    def get_game(self, game_id: str) -> Optional[Game]:
        """Retrieve a game by ID."""
        return self._games.get(game_id)

    def list_games(self) -> List[Dict[str, Any]]:
        """Return list of available registered simulation games."""
        return [
            {
                "id": g.game_id,
                "title": g.title,
                "description": g.description,
                "learning_objective": g.learning_objective,
                "difficulty": f"Level {g.difficulty_level} ({g.difficulty_name})",
            }
            for g in self._games.values()
        ]


# Global default registry
REGISTRY = GameRegistry()
