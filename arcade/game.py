"""
MATRIX2.0 Arcade Game Base Interface

Defines universal simulation game interface, difficulty levels, prediction hooks,
explanations (Simple, Mathematical, Research), and serialization handlers.
"""

import csv
import json
import os
import sys
from typing import Dict, Any, List, Optional

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


DIFFICULTY_LEVELS = {
    1: "Curious",
    2: "Explorer",
    3: "Scientist",
    4: "Researcher",
}


class Game:
    """
    Universal base class for MATRIX2.0 Arcade simulation games.
    """

    def __init__(
        self,
        game_id: str,
        title: str,
        description: str,
        learning_objective: str,
        difficulty_level: int = 1,
    ):
        self.game_id = game_id
        self.title = title
        self.description = description
        self.learning_objective = learning_objective
        self.difficulty_level = difficulty_level if difficulty_level in DIFFICULTY_LEVELS else 1
        self.difficulty_name = DIFFICULTY_LEVELS[self.difficulty_level]

    def run(
        self,
        params: Dict[str, Any],
        prediction: Optional[str] = None,
        seed: Optional[int] = 42,
    ) -> Dict[str, Any]:
        """
        Main execution loop following:
        INTRO -> LEARN -> PREDICT -> PLAY -> RUN -> OBSERVE -> COMPARE -> EXPLAIN -> TRY AGAIN
        Override in subclasses.
        """
        raise NotImplementedError("Subclasses must implement run().")

    def export_json(self, result_data: Dict[str, Any], filepath: str) -> None:
        """Export game experiment result to JSON."""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(result_data, f, indent=2)

    def export_csv(self, trajectory: List[Dict[str, float]], filepath: str) -> None:
        """Export trajectory points to CSV."""
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if trajectory:
                writer.writerow(list(trajectory[0].keys()))
                for row in trajectory:
                    writer.writerow(list(row.values()))
