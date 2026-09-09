"""
Node data structure for MATRIX2.0 Knowledge Graph.
"""

from typing import Any, Dict, Optional


class Node:
    VALID_TYPES = {
        "concept",
        "parameter",
        "state",
        "experiment",
        "metric",
        "result",
        "visualization",
        "game",
        "research_record",
        "observation",
        "hypothesis"
    }

    def __init__(
        self,
        node_id: str,
        node_type: str,
        name: str,
        description: str = "",
        metadata: Optional[Dict[str, Any]] = None,
        provenance: Optional[Dict[str, Any]] = None
    ):
        if node_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid node type '{node_type}'. Valid types: {self.VALID_TYPES}")

        self.id = node_id
        self.type = node_type
        self.name = name
        self.description = description
        self.metadata = metadata if metadata is not None else {}
        self.provenance = provenance if provenance is not None else {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata,
            "provenance": self.provenance
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Node":
        return cls(
            node_id=data.get("id", ""),
            node_type=data.get("type", "concept"),
            name=data.get("name", ""),
            description=data.get("description", ""),
            metadata=data.get("metadata", {}),
            provenance=data.get("provenance", {})
        )
