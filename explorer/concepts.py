"""
MATRIX2.0 Explorer Concepts

Provides structured educational descriptions for mathematical and computational concepts.
"""

from typing import Dict, Any, Optional


class Concept:
    """
    Represents an educational concept in MATRIX2.0.
    """

    def __init__(
        self,
        name: str,
        beginner_description: str,
        deep_description: str,
        difficulty: str = "Beginner",
        example: str = "",
        formula: str = "",
        experiment: str = "",
    ):
        self.name = name
        self.beginner_description = beginner_description
        self.deep_description = deep_description
        self.difficulty = difficulty
        self.example = example
        self.formula = formula
        self.experiment = experiment

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "beginner_description": self.beginner_description,
            "deep_description": self.deep_description,
            "difficulty": self.difficulty,
            "example": self.example,
            "formula": self.formula,
            "experiment": self.experiment,
        }


CORE_CONCEPTS: Dict[str, Concept] = {
    "value": Concept(
        name="Value",
        beginner_description="The current height or size of a wave at a specific moment.",
        deep_description="The scalar state output value W(t) computed at time t.",
        difficulty="Beginner",
        example="A value of 1.0 means the wave is at its peak height.",
        formula="W(t) = I * sin(2*pi*f*t + phi)",
        experiment="Observe how value changes as time advances.",
    ),
    "frequency": Concept(
        name="Frequency",
        beginner_description="How quickly something repeats.",
        deep_description="The number of complete cycles occurring per unit of time (Hz).",
        difficulty="Beginner",
        example="High frequency makes a wave oscillate rapidly.",
        formula="f = cycles / time",
        experiment="Change frequency from 0.5 to 2.0 and observe wave speed.",
    ),
    "intensity": Concept(
        name="Intensity",
        beginner_description="How strong or tall a wave is.",
        deep_description="The maximum amplitude or energy scale factor of the wave signal.",
        difficulty="Beginner",
        example="Higher intensity produces taller peaks and deeper troughs.",
        formula="Intensity = Peak Amplitude",
        experiment="Increase intensity to see the wave scale up.",
    ),
    "phase": Concept(
        name="Phase",
        beginner_description="Where a wave starts in its repeating pattern.",
        deep_description="The angular displacement of the wave cycle at t=0, measured in radians.",
        difficulty="Intermediate",
        example="A phase shift of pi flips the wave upside down at t=0.",
        formula="phi = angular displacement (rad)",
        experiment="Shift phase to shift the wave left or right.",
    ),
    "wave": Concept(
        name="Wave",
        beginner_description="A smooth repeating pattern that moves up and down.",
        deep_description="A periodic mathematical function oscillating around an equilibrium state.",
        difficulty="Beginner",
        example="A sine wave smoothly moving between +1 and -1.",
        formula="W(t) = I * sin(2*pi*f*t + phi)",
        experiment="Combine frequency and intensity to form a custom wave.",
    ),
    "chaos": Concept(
        name="Chaos",
        beginner_description="Small unpredictable fluctuations added to a smooth wave.",
        deep_description="Bounded stochastic noise perturbation altering parameter stability.",
        difficulty="Intermediate",
        example="Adding chaos makes a smooth sine wave jittery.",
        formula="noise in [-c, +c]",
        experiment="Increase chaos parameter to see noise disrupt the wave.",
    ),
    "variation": Concept(
        name="Variation",
        beginner_description="A slow, steady change over time.",
        deep_description="Systematic parameter drift or deterministic low-frequency modulation.",
        difficulty="Intermediate",
        example="A wave slowly getting stronger over time.",
        formula="shift = v * cos(t)",
        experiment="Set variation to see gradual parameter shifts.",
    ),
    "particle": Concept(
        name="Particle",
        beginner_description="An individual point that follows wave rules.",
        deep_description="A discrete state instance governed by an individual MatrixDynamics engine.",
        difficulty="Intermediate",
        example="A single particle oscillating in a particle field.",
        formula="MatrixParticle(state, dynamics)",
        experiment="Observe an individual particle inside a field.",
    ),
    "state": Concept(
        name="State",
        beginner_description="A snapshot of all settings at one moment.",
        deep_description="A complete vector parameter tuple M = (x, f, I, phi, c, v).",
        difficulty="Beginner",
        example="The state describes value, frequency, and intensity together.",
        formula="M = (x, f, I, phi, c, v)",
        experiment="Inspect state parameters before and after a step.",
    ),
    "transformation": Concept(
        name="Transformation",
        beginner_description="Changing information from one form into another.",
        deep_description="A deterministic mathematical mapping function between domains.",
        difficulty="Advanced",
        example="Converting text into a dynamic wave state.",
        formula="T: Text -> MatrixState",
        experiment="Transform a word into a dynamic wave.",
    ),
    "encoding": Concept(
        name="Encoding",
        beginner_description="Turning letters or words into numbers.",
        deep_description="Mapping discrete symbolic input characters into numeric state representations.",
        difficulty="Beginner",
        example="'A' becomes 65.",
        formula="code = ord(char)",
        experiment="Encode 'MOTHER' into ASCII values.",
    ),
    "decoding": Concept(
        name="Decoding",
        beginner_description="Turning numbers back into words.",
        deep_description="Reconstructing symbolic textual representations from numeric state values.",
        difficulty="Beginner",
        example="65 becomes 'A'.",
        formula="char = chr(code)",
        experiment="Decode ASCII numbers back into 'MOTHER'.",
    ),
}


def get_concept(name: str) -> Optional[Concept]:
    """Retrieve a Concept object by key (case-insensitive)."""
    return CORE_CONCEPTS.get(name.lower().strip())
