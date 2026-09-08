"""
MATRIX2.0
Shunya State Engine - Version 0.1

The first experimental representation of a MATRIX state.
"""


class MatrixState:
    """Represents one state inside the MATRIX2.0 system."""

    def __init__(
        self,
        value=0.0,
        frequency=0.0,
        intensity=0.0,
        phase=0.0,
        chaos=0.0,
        variation=0.0,
    ):
        self.value = value
        self.frequency = frequency
        self.intensity = intensity
        self.phase = phase
        self.chaos = chaos
        self.variation = variation

    def describe(self):
        """Return the current MATRIX state."""
        return {
            "value": self.value,
            "frequency": self.frequency,
            "intensity": self.intensity,
            "phase": self.phase,
            "chaos": self.chaos,
            "variation": self.variation,
        }
