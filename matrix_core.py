"""
Canonical MATRIX state representation for MATRIX2.0.
M = (x, f, I, phi, c, v)
"""

from typing import Any, Dict


class MatrixState:
    """Canonical 6D matrix state representation."""

    def __init__(
        self,
        value: float = 1.0,
        frequency: float = 1.0,
        intensity: float = 1.0,
        phase: float = 0.0,
        chaos: float = 0.0,
        variation: float = 0.0
    ):
        self.value = float(value)
        self.frequency = float(frequency)
        self.intensity = float(intensity)
        self.phase = float(phase)
        self.chaos = float(chaos)
        self.variation = float(variation)

    def describe(self) -> Dict[str, float]:
        return {
            "value": self.value,
            "frequency": self.frequency,
            "intensity": self.intensity,
            "phase": self.phase,
            "chaos": self.chaos,
            "variation": self.variation
        }

    def to_dict(self) -> Dict[str, float]:
        return self.describe()

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MatrixState":
        return cls(
            value=data.get("value", 1.0),
            frequency=data.get("frequency", 1.0),
            intensity=data.get("intensity", 1.0),
            phase=data.get("phase", 0.0),
            chaos=data.get("chaos", 0.0),
            variation=data.get("variation", 0.0)
        )
