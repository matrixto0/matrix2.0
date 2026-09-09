"""
MATRIX2.0 Contribution Lifecycle Tracker

Tracks open-source contribution items across lifecycle statuses:
- identified
- verified
- reported
- submitted
- accepted
- rejected
- merged
"""

import datetime
from typing import Dict, List, Any, Optional

VALID_STATUSES = {
    "identified",
    "verified",
    "reported",
    "submitted",
    "accepted",
    "rejected",
    "merged",
}


class ContributionTracker:
    """
    Manages records of open-source contributions and their verification status.
    """

    def __init__(self):
        self.contributions: List[Dict[str, Any]] = []

    def add_contribution(
        self,
        repository: str,
        contribution_type: str,
        finding: str,
        status: str = "identified",
        url: Optional[str] = None,
        result: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Record a new contribution lifecycle item.
        """
        status_lower = status.lower()
        if status_lower not in VALID_STATUSES:
            raise ValueError(
                f"Invalid status '{status}'. Must be one of: {sorted(VALID_STATUSES)}"
            )

        item = {
            "id": len(self.contributions) + 1,
            "repository": repository,
            "contribution_type": contribution_type,
            "finding": finding,
            "status": status_lower,
            "date": datetime.date.today().isoformat(),
            "url": url,
            "result": result,
        }
        self.contributions.append(item)
        return item

    def update_status(
        self,
        contribution_id: int,
        new_status: str,
        url: Optional[str] = None,
        result: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Update status and metadata for an existing contribution entry.
        """
        new_status_lower = new_status.lower()
        if new_status_lower not in VALID_STATUSES:
            raise ValueError(
                f"Invalid status '{new_status}'. Must be one of: {sorted(VALID_STATUSES)}"
            )

        for item in self.contributions:
            if item["id"] == contribution_id:
                item["status"] = new_status_lower
                if url is not None:
                    item["url"] = url
                if result is not None:
                    item["result"] = result
                return item

        raise KeyError(f"Contribution ID {contribution_id} not found.")

    def get_contributions(
        self, status_filter: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get all tracked contributions, optionally filtered by status.
        """
        if status_filter:
            filter_lower = status_filter.lower()
            return [c for c in self.contributions if c["status"] == filter_lower]
        return list(self.contributions)
