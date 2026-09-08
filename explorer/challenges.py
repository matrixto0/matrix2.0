"""
MATRIX2.0 Explorer Challenges

Provides interactive learning challenges with flexible validation functions.
"""

from typing import Dict, Any, Callable, List, Optional
from matrix_core import MatrixState
from matrix_dynamics import step_dynamics
from matrix_particles import ParticleField
from matrix_encode import encode_text
from matrix_decode import decode_values


class Challenge:
    """Represents an interactive learning challenge."""

    def __init__(
        self,
        id: str,
        title: str,
        objective: str,
        difficulty: str,
        hints: List[str],
        expected_learning: str,
        validator: Callable[..., bool],
    ):
        self.id = id
        self.title = title
        self.objective = objective
        self.difficulty = difficulty
        self.hints = hints
        self.expected_learning = expected_learning
        self.validator = validator

    def validate(self, *args, **kwargs) -> bool:
        """Run the validator function to check if challenge objective is met."""
        return self.validator(*args, **kwargs)


# 1. Challenge: Faster Oscillation
def _val_faster_oscillation(state: MatrixState) -> bool:
    return state.frequency >= 2.0


# 2. Challenge: Stronger Wave
def _val_stronger_wave(state: MatrixState) -> bool:
    return state.intensity >= 2.0


# 3. Challenge: Create Two Different Waves
def _val_two_waves(state_a: MatrixState, state_b: MatrixState) -> bool:
    return state_a.frequency != state_b.frequency or state_a.intensity != state_b.intensity


# 4. Challenge: Predict Peak Time
def _val_predict_peak(predicted_value: float, actual_state: MatrixState) -> bool:
    return abs(predicted_value - actual_state.value) < 0.1


# 5. Challenge: Encode MOTHER
def _val_encode_mother(text: str, encoded: List[int]) -> bool:
    return text.upper() == "MOTHER" and encoded == [77, 79, 84, 72, 69, 82]


# 6. Challenge: Decode Numbers
def _val_decode_numbers(encoded: List[int], decoded: str) -> bool:
    return decoded == "MOTHER" and encoded == [77, 79, 84, 72, 69, 82]


# 7. Challenge: Create Particle Field
def _val_particle_field(field: ParticleField) -> bool:
    return len(field.particles) >= 5


# 8. Challenge: Surprising Result (Chaos + Phase combination)
def _val_surprising_result(state: MatrixState) -> bool:
    return state.chaos > 0.02 and state.phase > 0.0


LEARNING_CHALLENGES: List[Challenge] = [
    Challenge(
        id="faster_wave",
        title="Make the wave oscillate faster",
        objective="Set frequency to 2.0 or higher.",
        difficulty="Beginner",
        hints=["Increase the frequency attribute on MatrixState."],
        expected_learning="Frequency determines oscillation rate.",
        validator=_val_faster_oscillation,
    ),
    Challenge(
        id="stronger_wave",
        title="Make the wave stronger",
        objective="Set intensity to 2.0 or higher.",
        difficulty="Beginner",
        hints=["Increase the intensity attribute on MatrixState."],
        expected_learning="Intensity scales amplitude peak height.",
        validator=_val_stronger_wave,
    ),
    Challenge(
        id="two_waves",
        title="Create two different waves",
        objective="Construct two MatrixState objects with different frequencies or intensities.",
        difficulty="Beginner",
        hints=["Pass distinct parameter values when initializing MatrixState."],
        expected_learning="Individual state vectors maintain independent parameters.",
        validator=_val_two_waves,
    ),
    Challenge(
        id="predict_peak",
        title="Predict wave value before step",
        objective="Predict the wave value output within 0.1 error bound.",
        difficulty="Intermediate",
        hints=["Use W(t) = I * sin(2*pi*f*t + phi)."],
        expected_learning="Mathematical equations accurately predict deterministic outputs.",
        validator=_val_predict_peak,
    ),
    Challenge(
        id="encode_mother",
        title="Encode the word MOTHER",
        objective="Encode 'MOTHER' into numeric ASCII code list.",
        difficulty="Beginner",
        hints=["Use encode_text('MOTHER')."],
        expected_learning="Symbolic text maps directly to numeric unicode sequences.",
        validator=_val_encode_mother,
    ),
    Challenge(
        id="decode_numbers",
        title="Decode the numbers",
        objective="Decode [77, 79, 84, 72, 69, 82] back into 'MOTHER'.",
        difficulty="Beginner",
        hints=["Use decode_values([77, 79, 84, 72, 69, 82])."],
        expected_learning="Numeric state codes can be reconstructed losslessly.",
        validator=_val_decode_numbers,
    ),
    Challenge(
        id="particle_field",
        title="Create a particle field",
        objective="Initialize a ParticleField with at least 5 particles.",
        difficulty="Intermediate",
        hints=["Use ParticleField.generate_random_particles(5)."],
        expected_learning="Field containers orchestrate multi-particle state evolution.",
        validator=_val_particle_field,
    ),
    Challenge(
        id="surprising_result",
        title="Find a surprising combination",
        objective="Combine positive chaos and non-zero phase.",
        difficulty="Advanced",
        hints=["Set chaos > 0.02 and phase > 0.0."],
        expected_learning="Non-zero phase and chaos create perturbed initial conditions.",
        validator=_val_surprising_result,
    ),
]


def get_challenge(challenge_id: str) -> Optional[Challenge]:
    """Retrieve a challenge by ID."""
    for ch in LEARNING_CHALLENGES:
        if ch.id == challenge_id:
            return ch
    return None
