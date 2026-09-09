"""
Experiment representation model for MATRIX2.0 Reproducible Experiment Engine.
"""

import json
from typing import Any, Dict, Optional
from experiments.configuration import ExperimentConfig


class Experiment:
    """Represents a complete computational experiment including configuration, measurements, and metadata."""

    def __init__(
        self,
        config: ExperimentConfig,
        timestamp: Optional[str] = None,
        measurements: Optional[Dict[str, Any]] = None,
        summary: Optional[Dict[str, Any]] = None,
        reproducible: Optional[bool] = None
    ):
        self.config = config
        self.timestamp = timestamp or "2025-01-01T00:00:00Z"
        self.measurements = measurements if measurements is not None else {}
        self.summary = summary if summary is not None else {}
        self.reproducible = reproducible

    @property
    def experiment_id(self) -> str:
        return self.config.experiment_id

    @property
    def name(self) -> str:
        return self.config.name

    @property
    def description(self) -> str:
        return self.config.description

    @property
    def model(self) -> str:
        return self.config.model

    @property
    def parameters(self) -> Dict[str, Any]:
        return self.config.parameters

    @property
    def seed(self) -> int:
        return self.config.seed

    @property
    def iterations(self) -> int:
        return self.config.iterations

    def to_dict(self, include_timestamp: bool = True) -> Dict[str, Any]:
        """Convert experiment to a dictionary."""
        d = {
            "config": self.config.to_dict(),
            "measurements": self.measurements,
            "summary": self.summary,
            "reproducible": self.reproducible
        }
        if include_timestamp:
            d["timestamp"] = self.timestamp
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Experiment":
        """Instantiate experiment from a dictionary."""
        config_data = data.get("config", data)
        config = ExperimentConfig.from_dict(config_data)
        return cls(
            config=config,
            timestamp=data.get("timestamp"),
            measurements=data.get("measurements", {}),
            summary=data.get("summary", {}),
            reproducible=data.get("reproducible")
        )

    def to_json(self, indent: int = 2, include_timestamp: bool = True) -> str:
        """Serialize experiment to JSON string."""
        return json.dumps(self.to_dict(include_timestamp=include_timestamp), indent=indent)

    @classmethod
    def from_json(cls, json_str: str) -> "Experiment":
        """Instantiate experiment from JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)
