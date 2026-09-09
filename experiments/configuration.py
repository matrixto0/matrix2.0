"""
Experiment configuration model for MATRIX2.0 Reproducible Experiment Engine.
"""

import json
from typing import Any, Dict, Optional


class ExperimentConfig:
    """Encapsulates execution parameters, seed, iteration count, and model specification."""

    def __init__(
        self,
        experiment_id: str,
        name: str,
        description: str,
        model: str,
        parameters: Optional[Dict[str, Any]] = None,
        input_state: Optional[Any] = None,
        seed: int = 42,
        iterations: int = 100,
        metadata: Optional[Dict[str, Any]] = None
    ):
        self.experiment_id = experiment_id
        self.name = name
        self.description = description
        self.model = model
        self.parameters = parameters if parameters is not None else {}
        self.input_state = input_state
        self.seed = seed
        self.iterations = iterations
        self.metadata = metadata if metadata is not None else {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to a dictionary."""
        return {
            "experiment_id": self.experiment_id,
            "name": self.name,
            "description": self.description,
            "model": self.model,
            "parameters": self.parameters,
            "input_state": self.input_state,
            "seed": self.seed,
            "iterations": self.iterations,
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ExperimentConfig":
        """Instantiate configuration from a dictionary."""
        return cls(
            experiment_id=data.get("experiment_id", "unnamed_exp"),
            name=data.get("name", "Unnamed Experiment"),
            description=data.get("description", ""),
            model=data.get("model", "wave_stability"),
            parameters=data.get("parameters", {}),
            input_state=data.get("input_state"),
            seed=data.get("seed", 42),
            iterations=data.get("iterations", 100),
            metadata=data.get("metadata", {})
        )

    def to_json(self, indent: int = 2) -> str:
        """Serialize configuration to a JSON string."""
        return json.dumps(self.to_dict(), indent=indent)

    @classmethod
    def from_json(cls, json_str: str) -> "ExperimentConfig":
        """Instantiate configuration from a JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)
