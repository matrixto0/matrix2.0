"""
MATRIX2.0 Living Lab Achievement System

Tracks educational milestones across Living Lab activities, including prediction outcomes.
"""

from typing import Dict, Any, List


class LabAchievementTracker:
    """
    Tracks educational learning achievements for Living Lab user journeys.
    """

    ACHIEVEMENTS = [
        "FIRST_EXPLORATION",
        "FIRST_ENCODING",
        "FIRST_WAVE",
        "FIRST_PARTICLE_FIELD",
        "FIRST_CHAOS_TEST",
        "FIRST_PREDICTION",
        "FIRST_SUCCESSFUL_PREDICTION",
        "FIRST_FAILED_PREDICTION",
        "FIRST_CUSTOM_EXPERIMENT",
        "FIRST_REPRODUCED_RESULT",
    ]

    def __init__(self):
        self.unlocked: List[str] = []

    def unlock(self, achievement_id: str) -> bool:
        """Unlock an achievement if valid and not already unlocked."""
        ach_upper = achievement_id.upper().strip()
        if ach_upper in self.ACHIEVEMENTS and ach_upper not in self.unlocked:
            self.unlocked.append(ach_upper)
            return True
        return False

    def is_unlocked(self, achievement_id: str) -> bool:
        """Check if an achievement is unlocked."""
        return achievement_id.upper().strip() in self.unlocked

    def record_prediction_outcome(self, confirmed: bool) -> None:
        """
        Record prediction attempt. Both successful and failed predictions unlock achievements.
        """
        self.unlock("FIRST_PREDICTION")
        if confirmed:
            self.unlock("FIRST_SUCCESSFUL_PREDICTION")
        else:
            self.unlock("FIRST_FAILED_PREDICTION")

    def get_progress(self) -> Dict[str, Any]:
        """Return total progress summary."""
        return {
            "unlocked_count": len(self.unlocked),
            "total_count": len(self.ACHIEVEMENTS),
            "unlocked": list(self.unlocked),
        }
