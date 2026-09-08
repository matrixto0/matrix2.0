"""
MATRIX2.0 Open Source Opportunity Scoring Engine

Defines ContributionOpportunity model and calculates normalized opportunity scores.
"""

from typing import Dict, Any, Optional

SUPPORTED_ISSUE_TYPES = {
    "bug",
    "security",
    "documentation",
    "testing",
    "performance",
    "feature",
    "research",
}


class ContributionOpportunity:
    """
    Represents an open-source contribution opportunity.
    """

    def __init__(
        self,
        project: str,
        issue_type: str,
        description: str,
        evidence: str,
        difficulty: float,
        impact: float,
        reproducibility: float,
        estimated_effort: float,
        relevance: float = 5.0,
        learning_value: float = 5.0,
    ):
        if not project or not isinstance(project, str):
            raise ValueError("Project name must be a non-empty string.")

        issue_type_lower = issue_type.lower() if isinstance(issue_type, str) else ""
        if issue_type_lower not in SUPPORTED_ISSUE_TYPES:
            raise ValueError(
                f"Unsupported issue type '{issue_type}'. Supported types: {sorted(SUPPORTED_ISSUE_TYPES)}"
            )

        self.project = project
        self.issue_type = issue_type_lower
        self.description = description
        self.evidence = evidence
        self.difficulty = float(difficulty)
        self.impact = float(impact)
        self.reproducibility = float(reproducibility)
        self.estimated_effort = float(estimated_effort)
        self.relevance = float(relevance)
        self.learning_value = float(learning_value)

        self.score = self.calculate_score()

    def calculate_score(self) -> float:
        """
        Calculate raw score and normalize to 0-100 range.

        Formula:
        raw_score = impact + reproducibility + relevance + learning_value - difficulty
        """
        raw_score = (
            self.impact
            + self.reproducibility
            + self.relevance
            + self.learning_value
            - self.difficulty
        )

        # Assuming default scale bounds per metric approximately 0..10 (raw range -10 .. 40)
        # We normalize linearly bounded strictly between 0.0 and 100.0
        normalized = ((raw_score + 10.0) / 50.0) * 100.0
        return max(0.0, min(100.0, round(normalized, 2)))

    def to_dict(self) -> Dict[str, Any]:
        """Return structured dictionary representation."""
        return {
            "project": self.project,
            "issue_type": self.issue_type,
            "description": self.description,
            "evidence": self.evidence,
            "difficulty": self.difficulty,
            "impact": self.impact,
            "reproducibility": self.reproducibility,
            "estimated_effort": self.estimated_effort,
            "relevance": self.relevance,
            "learning_value": self.learning_value,
            "score": self.score,
        }
