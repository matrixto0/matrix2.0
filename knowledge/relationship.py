"""
Relationship data structure for MATRIX2.0 Knowledge Graph.
"""

from typing import Any, Dict, Optional


class Relationship:
    VALID_TYPES = {
        "ENCODES",
        "PRODUCES",
        "DEPENDS_ON",
        "MEASURES",
        "VISUALIZES",
        "COMPARES_WITH",
        "DERIVED_FROM",
        "USES_PARAMETER",
        "GENERATES",
        "OBSERVES",
        "SUPPORTS",
        "CONTRADICTS",
        "RELATED_TO"
    }

    def __init__(
        self,
        source_id: str,
        target_id: str,
        rel_type: str,
        metadata: Optional[Dict[str, Any]] = None,
        provenance: Optional[Dict[str, Any]] = None
    ):
        if rel_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid relationship type '{rel_type}'. Valid types: {self.VALID_TYPES}")

        self.source_id = source_id
        self.target_id = target_id
        self.type = rel_type
        self.metadata = metadata if metadata is not None else {}
        self.provenance = provenance if provenance is not None else {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_id": self.source_id,
            "target_id": self.target_id,
            "type": self.type,
            "metadata": self.metadata,
            "provenance": self.provenance
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Relationship":
        return cls(
            source_id=data.get("source_id", ""),
            target_id=data.get("target_id", ""),
            rel_type=data.get("type", "RELATED_TO"),
            metadata=data.get("metadata", {}),
            provenance=data.get("provenance", {})
        )
