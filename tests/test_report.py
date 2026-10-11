import csv
import unittest
from pathlib import Path

from demo.report import draft, validate


EXAMPLE = Path(__file__).resolve().parents[1] / "demo" / "tasks.csv"


class ReportTest(unittest.TestCase):
    def setUp(self):
        with EXAMPLE.open(newline="", encoding="utf-8") as file:
            self.rows = list(csv.DictReader(file))

    def test_counts_only_leaf_tasks(self):
        report = draft(self.rows)
        self.assertIn("Leaf tasks completed: 2/3", report)
        self.assertIn("Nothing has been sent", report)

    def test_rejects_missing_parent(self):
        self.rows[1]["parent_id"] = "not-a-task"
        self.assertTrue(any("parent task is missing" in error for error in validate(self.rows)))

    def test_rejects_duplicate_period_and_task(self):
        self.rows.append(self.rows[0].copy())
        self.assertTrue(any("duplicate task" in error for error in validate(self.rows)))


if __name__ == "__main__":
    unittest.main()
