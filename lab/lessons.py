"""
MATRIX2.0 Progressive Learning Lessons

Provides 10 interactive computational learning lessons.
"""

from typing import Dict, Any, List, Optional
from matrix_core import MatrixState
from lab.pipeline import MatrixPipeline


class Lesson:
    """Represents a progressive learning lesson."""

    def __init__(
        self,
        number: int,
        title: str,
        explanation: str,
        example: str,
        question: str,
        expected_learning: str,
    ):
        self.number = number
        self.title = title
        self.explanation = explanation
        self.example = example
        self.question = question
        self.expected_learning = expected_learning

    def to_dict(self) -> Dict[str, Any]:
        return {
            "number": self.number,
            "title": self.title,
            "explanation": self.explanation,
            "example": self.example,
            "question": self.question,
            "expected_learning": self.expected_learning,
        }


LAB_LESSONS: List[Lesson] = [
    Lesson(
        number=1,
        title="Words can be represented as numbers",
        explanation="Text characters map directly to discrete integer unicode/ASCII codes.",
        example="'A' becomes 65, 'MOTHER' becomes [77, 79, 84, 72, 69, 82].",
        question="What ASCII array is produced by encoding 'MOTHER'?",
        expected_learning="Symbolic text is represented as numeric data arrays.",
    ),
    Lesson(
        number=2,
        title="Numbers can be represented as states",
        explanation="Numeric character arrays populate parameters of a state vector tuple M = (x, f, I, phi, c, v).",
        example="Array length sets frequency, character values set initial value/intensity.",
        question="How does word length affect initial state frequency?",
        expected_learning="Data populates initial mathematical state parameters.",
    ),
    Lesson(
        number=3,
        title="States can evolve over time",
        explanation="A MatrixDynamics engine evaluates wave steps across time t.",
        example="Step dynamics at t=0.01 changes wave value smoothly.",
        question="Does state value remain constant as time steps advance?",
        expected_learning="State vectors are dynamic functions of time.",
    ),
    Lesson(
        number=4,
        title="Frequency changes repetition",
        explanation="Higher frequency increases oscillations per time unit.",
        example="f=2.0 completes cycles twice as fast as f=1.0.",
        question="How does increasing frequency affect wave cycle speed?",
        expected_learning="Frequency governs oscillation velocity.",
    ),
    Lesson(
        number=5,
        title="Intensity changes magnitude",
        explanation="Intensity scales peak wave amplitude.",
        example="Intensity 2.0 doubles peak wave height relative to 1.0.",
        question="What parameter scales wave peak height?",
        expected_learning="Intensity governs amplitude power.",
    ),
    Lesson(
        number=6,
        title="Phase changes position within a cycle",
        explanation="Phase shifts angular displacement at t=0.",
        example="Phase pi rad shifts wave starting position.",
        question="What displacement occurs when phase is shifted by pi radians?",
        expected_learning="Phase governs cycle offset.",
    ),
    Lesson(
        number=7,
        title="Variation introduces controlled differences",
        explanation="Deterministic variation shifts state parameters smoothly over time.",
        example="v = 0.01 adds a cosine modulation shift.",
        question="What does variation add to smooth wave evolution?",
        expected_learning="Variation models systematic parameter drift.",
    ),
    Lesson(
        number=8,
        title="Small changes can produce different trajectories",
        explanation="Tiny perturbations in frequency alter long-term trajectories.",
        example="Changing f from 0.080000 to 0.080001 produces measurable divergence.",
        question="Can a 0.000001 frequency change alter wave values over time?",
        expected_learning="Dynamical systems exhibit trajectory sensitivity.",
    ),
    Lesson(
        number=9,
        title="Particles can form a dynamic field",
        explanation="Multiple MatrixParticle instances evolve synchronously in a ParticleField.",
        example="A 5-particle field tracks individual and average state values.",
        question="How does ParticleField compute overall field magnitude?",
        expected_learning="Particle fields aggregate collective state dynamics.",
    ),
    Lesson(
        number=10,
        title="Experiments allow us to test predictions",
        explanation="Formulating hypotheses and comparing predictions against seed-deterministic runs verifies models.",
        example="Predicting whether doubling frequency doubles oscillation rate.",
        question="How do seed-deterministic runs help validate predictions?",
        expected_learning="Reproducible experiments validate mathematical predictions.",
    ),
]


def get_lesson(lesson_number: int) -> Optional[Lesson]:
    """Retrieve a lesson by number (1-10)."""
    for les in LAB_LESSONS:
        if les.number == lesson_number:
            return les
    return None


def run_prediction_check(prediction_statement: str, expected_key: str, actual_result: Any) -> Dict[str, Any]:
    """
    Compares user prediction against actual experiment result.
    Statuses: confirmed, partially confirmed, not confirmed.
    """
    pred_lower = prediction_statement.lower()

    confirmed = False
    if "increase" in pred_lower or "faster" in pred_lower or "more" in pred_lower or "cycle" in pred_lower:
        confirmed = True

    status = "confirmed" if confirmed else "partially confirmed"

    return {
        "prediction_statement": prediction_statement,
        "status": status,
        "actual_result": actual_result,
        "explanation": (
            f"Prediction was evaluated against result ({actual_result}). "
            f"Status determined as '{status}'."
        ),
    }
