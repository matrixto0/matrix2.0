"""
Observation data structures for MATRIX2.0 Research Framework.
"""

import time
from typing import Any, Dict, List, Optional


class Observation:
    """Represents data or metrics recorded during experiment execution."""

    def __init__(self, step: int, data: Dict[str, Any], timestamp: Optional[float] = None):
        self.step = step
        self.data = data
        self.timestamp = timestamp if timestamp is not None else time.time()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "step": self.step,
            "data": self.data,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Observation":
        return cls(
            step=data.get("step", 0),
            data=data.get("data", {}),
            timestamp=data.get("timestamp")
        )


class ObservationLogger:
    """Collects and manages observations recorded during an experiment run."""

    def __init__(self):
        self.observations: List[Observation] = []

    def record(self, step: int, data: Dict[str, Any]):
        obs = Observation(step=step, data=data)
        self.observations.append(obs)
        return obs

    def get_summary(self) -> Dict[str, Any]:
        return {
            "count": len(self.observations),
            "steps": [obs.step for obs in self.observations]
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "observations": [obs.to_dict() for obs in self.observations]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ObservationLogger":
        logger = cls()
        logger.observations = [Observation.from_dict(item) for item in data.get("observations", [])]
        return logger
