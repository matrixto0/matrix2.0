"""
Unit tests for MATRIX2.0 Open Source Contribution Engine modules:
- opportunity_score.py
- bug_scanner.py
- contribution_tracker.py
"""

import os
import shutil
import tempfile
import unittest

from opensource.opportunity_score import ContributionOpportunity
from opensource.bug_scanner import BugScanner
from opensource.contribution_tracker import ContributionTracker


class TestOpportunityScore(unittest.TestCase):
    def test_valid_opportunity_score_calculation(self):
        """Test score calculation and normalization."""
        opp = ContributionOpportunity(
            project="matrix2.0",
            issue_type="bug",
            description="Null pointer in wave step",
            evidence="Traceback at line 42",
            difficulty=2.0,
            impact=8.0,
            reproducibility=10.0,
            estimated_effort=1.0,
            relevance=7.0,
            learning_value=5.0,
        )
        # raw_score = 8 + 10 + 7 + 5 - 2 = 28
        # normalized = ((28 + 10) / 50) * 100 = 76.0
        self.assertEqual(opp.score, 76.0)
        self.assertEqual(opp.issue_type, "bug")

    def test_invalid_issue_type(self):
        """Test that invalid issue types raise ValueError."""
        with self.assertRaises(ValueError):
            ContributionOpportunity(
                project="test",
                issue_type="invalid_type",
                description="desc",
                evidence="ev",
                difficulty=1,
                impact=1,
                reproducibility=1,
                estimated_effort=1,
            )

    def test_invalid_project_name(self):
        """Test that empty project name raises ValueError."""
        with self.assertRaises(ValueError):
            ContributionOpportunity(
                project="",
                issue_type="bug",
                description="desc",
                evidence="ev",
                difficulty=1,
                impact=1,
                reproducibility=1,
                estimated_effort=1,
            )


class TestBugScanner(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_scanner_detects_issues(self):
        """Test scanner detects TODO markers, bare excepts, and missing docstrings."""
        sample_code = (
            "# TODO: fix this later\n"
            "def broken_function():\n"
            "    try:\n"
            "        x = 1 / 0\n"
            "    except:\n"
            "        pass\n"
        )
        filepath = os.path.join(self.test_dir, "sample.py")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(sample_code)

        scanner = BugScanner(self.test_dir)
        findings = scanner.scan()

        types = [f["type"] for f in findings]
        self.assertIn("todo_marker", types)
        self.assertIn("bare_except", types)
        self.assertIn("missing_docstring", types)


class TestContributionTracker(unittest.TestCase):
    def test_tracker_lifecycle(self):
        """Test tracking workflow and status updates."""
        tracker = ContributionTracker()
        item = tracker.add_contribution(
            repository="matrix2.0",
            contribution_type="bug",
            finding="Bare except handler",
            status="identified",
        )
        self.assertEqual(item["status"], "identified")

        updated = tracker.update_status(item["id"], "verified", result="Confirmed on Python 3.12")
        self.assertEqual(updated["status"], "verified")
        self.assertEqual(updated["result"], "Confirmed on Python 3.12")

        verified_list = tracker.get_contributions(status_filter="verified")
        self.assertEqual(len(verified_list), 1)

    def test_invalid_status_transition(self):
        """Test setting an invalid status raises ValueError."""
        tracker = ContributionTracker()
        with self.assertRaises(ValueError):
            tracker.add_contribution(
                repository="repo",
                contribution_type="bug",
                finding="finding",
                status="not_a_valid_status",
            )


if __name__ == "__main__":
    unittest.main()
