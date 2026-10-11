"""Build a reviewable report draft from fictional task data.

This is a local example, not the employer's Feishu integration.
"""

import csv
import sys
from pathlib import Path


REQUIRED = {"period", "task_id", "parent_id", "owner", "status"}


def validate(rows):
    errors = []
    seen = set()
    task_ids = {row.get("task_id", "") for row in rows}

    for line_number, row in enumerate(rows, start=2):
        missing = REQUIRED - row.keys()
        if missing:
            errors.append(f"row {line_number}: missing columns {', '.join(sorted(missing))}")
            continue

        if not row["period"] or not row["task_id"] or not row["owner"]:
            errors.append(f"row {line_number}: period, task ID, and owner are required")
        if row["parent_id"] and row["parent_id"] not in task_ids:
            errors.append(f"row {line_number}: parent task is missing")
        if row["status"] not in {"todo", "in_progress", "done"}:
            errors.append(f"row {line_number}: unknown status")

        key = (row["period"], row["task_id"])
        if key in seen:
            errors.append(f"row {line_number}: duplicate task in reporting period")
        seen.add(key)

    return errors


def draft(rows):
    errors = validate(rows)
    if errors:
        raise ValueError("\n".join(errors))

    periods = {row["period"] for row in rows}
    if len(periods) != 1:
        raise ValueError("report must contain exactly one reporting period")

    parents = {row["parent_id"] for row in rows if row["parent_id"]}
    leaf_tasks = [row for row in rows if row["task_id"] not in parents]
    completed = sum(row["status"] == "done" for row in leaf_tasks)
    period = periods.pop()

    return (
        f"# Report draft — {period}\n\n"
        f"Leaf tasks completed: {completed}/{len(leaf_tasks)}\n\n"
        "Status: pending human review. Nothing has been sent.\n"
    )


def main(path):
    with path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    print(draft(rows), end="")


if __name__ == "__main__":
    try:
        main(Path(sys.argv[1]))
    except (IndexError, OSError, ValueError) as error:
        print(f"Cannot build draft: {error}", file=sys.stderr)
        raise SystemExit(1)
