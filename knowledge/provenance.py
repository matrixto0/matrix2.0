"""
Provenance records for MATRIX2.0 Knowledge Graph nodes and relationships.
"""

from typing import Any, Dict, Optional


class Provenance:
    """Represents traceable origin metadata for computational artifacts and edges."""

    def __init__(
        self,
        source_type: str,
        source_id: str,
        description: str = "",
        experiment_id: Optional[str] = None,
        seed: Optional[int] = None,
        parameters: Optional[Dict[str, Any]] = None
    ):
        self.source_type = source_type
        self.source_id = source_id
        self.description = description
        self.experiment_id = experiment_id
        self.seed = seed
        self.parameters = parameters if parameters is not None else {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_type": self.source_type,
            "source_id": self.source_id,
            "description": self.description,
            "experiment_id": self.experiment_id,
            "seed": self.seed,
            "parameters": self.parameters
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Provenance":
        return cls(
            source_type=data.get("source_type", "system"),
            source_id=data.get("source_id", "core"),
            description=data.get("description", ""),
            experiment_id=data.get("experiment_id"),
            seed=data.get("seed"),
            parameters=data.get("parameters", {})
        )
