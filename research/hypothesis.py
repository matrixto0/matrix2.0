"""
Hypothesis definition for MATRIX2.0 Research Framework.
"""

from typing import Any, Dict, Optional


class Hypothesis:
    """Represents a scientific or computational hypothesis to be evaluated."""

    def __init__(self, statement: str, variables: Optional[Dict[str, Any]] = None, rationale: str = ""):
        self.statement = statement
        self.variables = variables if variables is not None else {}
        self.rationale = rationale

    def to_dict(self) -> Dict[str, Any]:
        return {
            "statement": self.statement,
            "variables": self.variables,
            "rationale": self.rationale
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Hypothesis":
        return cls(
            statement=data.get("statement", ""),
            variables=data.get("variables", {}),
            rationale=data.get("rationale", "")
        )
