"""
MATRIX2.0 Explanations, WhatIf Engine, Complexity Scoring & Achievements

Provides simple and mathematical explanation generators, state diff calculators,
complexity level scoring, and achievement tracking.
"""

from typing import Dict, Any, List, Optional
from matrix_core import MatrixState
from matrix_dynamics import step_dynamics, compute_wave_value


def explain_state_params(frequency: float, intensity: float, phase: float = 0.0) -> Dict[str, str]:
    """Provide simple and mathematical explanations for state parameters."""
    simple = (
        f"The frequency ({frequency}) controls how quickly the wave repeats. "
        f"The intensity ({intensity}) controls how tall or strong the wave gets."
    )
    mathematical = (
        f"Wave function W(t) = {intensity} * sin(2*pi*{frequency}*t + {phase}). "
        f"Oscillation rate is {frequency} Hz with amplitude scaling {intensity}."
    )
    return {
        "simple": simple,
        "mathematical": mathematical,
    }


class WhatIfEngine:
    """Calculates state changes and explains parameter differences."""

    @staticmethod
    def what_if_frequency_doubles(initial_state: MatrixState, t: float = 0.25) -> Dict[str, Any]:
        s_orig = MatrixState(**initial_state.describe())
        s_double = MatrixState(**initial_state.describe())
        s_double.frequency = initial_state.frequency * 2.0

        v_orig = step_dynamics(s_orig, t=t).value
        v_double = step_dynamics(s_double, t=t).value

        return {
            "question": "What if frequency doubles?",
            "original_frequency": initial_state.frequency,
            "new_frequency": s_double.frequency,
            "original_value": v_orig,
            "new_value": v_double,
            "explanation": f"Doubling frequency from {initial_state.frequency} to {s_double.frequency} doubles the oscillation rate, completing cycles twice as fast.",
        }

    @staticmethod
    def what_if_intensity_zero(initial_state: MatrixState, t: float = 0.25) -> Dict[str, Any]:
        s_zero = MatrixState(**initial_state.describe())
        s_zero.intensity = 0.0

        v_orig = step_dynamics(MatrixState(**initial_state.describe()), t=t).value
        v_zero = step_dynamics(s_zero, t=t).value

        return {
            "question": "What if intensity becomes zero?",
            "original_intensity": initial_state.intensity,
            "new_intensity": 0.0,
            "original_value": v_orig,
            "new_value": v_zero,
            "explanation": "Setting intensity to 0 reduces wave amplitude to zero, resulting in a flat signal.",
        }

    @staticmethod
    def what_if_chaos_increases(initial_state: MatrixState, new_chaos: float = 0.1, t: float = 0.25) -> Dict[str, Any]:
        s_high_chaos = MatrixState(**initial_state.describe())
        s_high_chaos.chaos = new_chaos

        v_orig = step_dynamics(MatrixState(**initial_state.describe()), t=t).value
        v_chaos = step_dynamics(s_high_chaos, t=t).value

        return {
            "question": "What if chaos increases?",
            "original_chaos": initial_state.chaos,
            "new_chaos": new_chaos,
            "original_value": v_orig,
            "new_value": v_chaos,
            "explanation": f"Increasing chaos to {new_chaos} introduces larger random noise perturbations into the wave output.",
        }


def calculate_complexity_score(state: MatrixState, particle_count: int = 1) -> Dict[str, Any]:
    """
    Computes a 0-100 complexity score based on active parameters and field size.

    0-20: Beginner
    21-40: Explorer
    41-60: Intermediate
    61-80: Advanced
    81-100: Research
    """
    score = 0.0

    if state.frequency > 0:
        score += 10.0
    if state.intensity > 0:
        score += 10.0
    if state.phase > 0:
        score += 15.0
    if state.chaos > 0:
        score += 20.0
    if state.variation > 0:
        score += 20.0

    score += min(25.0, particle_count * 5.0)

    score = max(0.0, min(100.0, score))

    if score <= 20:
        level = "Beginner"
    elif score <= 40:
        level = "Explorer"
    elif score <= 60:
        level = "Intermediate"
    elif score <= 80:
        level = "Advanced"
    else:
        level = "Research"

    return {
        "score": score,
        "level": level,
    }


class AchievementTracker:
    """Tracks educational learning achievements."""

    ACHIEVEMENTS = [
        "FIRST_WAVE",
        "FIRST_ENCODING",
        "FIRST_DECODING",
        "FIRST_PARTICLE",
        "FIRST_EXPERIMENT",
        "FIRST_PARAMETER_CHANGE",
        "FIRST_CUSTOM_EXPERIMENT",
        "FIRST_RESEARCH_RESULT",
    ]

    def __init__(self):
        self.unlocked: List[str] = []

    def unlock(self, achievement_id: str) -> bool:
        ach_upper = achievement_id.upper()
        if ach_upper in self.ACHIEVEMENTS and ach_upper not in self.unlocked:
            self.unlocked.append(ach_upper)
            return True
        return False

    def is_unlocked(self, achievement_id: str) -> bool:
        return achievement_id.upper() in self.unlocked

    def get_progress(self) -> Dict[str, Any]:
        return {
            "unlocked_count": len(self.unlocked),
            "total_count": len(self.ACHIEVEMENTS),
            "unlocked": list(self.unlocked),
        }
