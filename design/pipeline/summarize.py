"""Print the counts for design/logs/run_summary.md: milestones, frames per milestone,
inferred tags per milestone, and open-question ids per system from section 8 of the design doc.
Usage: python summarize.py
"""
from __future__ import annotations

import re

from common import BREAKDOWNS, DESIGN_DOC, LOGS, MILESTONES, read_json
from verify import open_questions_text

ITEM_ID = re.compile(r"\b(?:M\d+-I\d+|D-\d+)\b")


def main() -> None:
    data = read_json(MILESTONES)
    print("| Milestone | Title | Range | Frames | [inferred] |\n| --- | --- | --- | --- | --- |")
    total = 0
    for m in data["milestones"]:
        frames = len(list((BREAKDOWNS / m["id"] / "frames").glob("*.png")))
        inferred = (BREAKDOWNS / m["id"] / "breakdown.md").read_text(encoding="utf-8").count("[inferred]")
        total += frames
        print(f"| {m['id']} | {m['title']} | {m['start']} to {m['end']} | {frames} | {inferred} |")
    print(f"\nTotal frames: {total}\n")

    oq = open_questions_text(DESIGN_DOC.read_text(encoding="utf-8"))
    print("| Section 8 group | Unique ids |\n| --- | --- |")
    for title, body in re.findall(r"^###\s+([^\n]+)\n(.*?)(?=^###\s|\Z)", oq, re.M | re.S):
        print(f"| {title.strip()} | {len(set(ITEM_ID.findall(body)))} |")
    print(f"\nUnique ids in section 8: {len(set(ITEM_ID.findall(oq)))}")
    errors = LOGS / "errors.log"
    print(f"errors.log lines: {len(errors.read_text(encoding='utf-8').splitlines()) if errors.exists() else 0}")


if __name__ == "__main__":
    main()
