"""Finish-condition checks 1-4. Exit 0 only when all pass.

1. Every milestone in milestones.json has 03_breakdowns/<id>/breakdown.md.
2. Every frame path referenced in any breakdown.md or the design doc exists.
3. design_document.md contains all 10 required sections.
4. Every [inferred] item in the breakdowns carries an ID (M#-I##) that appears in the
   design doc's Open Questions section.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from common import BREAKDOWNS, DESIGN_DOC, MILESTONES, REPO, read_json

SECTIONS = {
    "1 Overview": r"overview",
    "2 System architecture": r"system architecture",
    "3 Bill of materials": r"bill of materials",
    "4 Tools and software": r"tools and software",
    "5 Build plan": r"build plan",
    "6 Per-system detailed design": r"per-system detailed design",
    "7 Lessons from the video": r"lessons",
    "8 Open questions and assumptions": r"open questions",
    "9 Suggested improvements": r"suggested improvements",
    "10 Proposed layout for src/": r"layout for .?src",
}
FRAME_REF = re.compile(r"[\w./\-]+\.(?:png|jpg|jpeg)", re.I)
INFERRED_ID = re.compile(r"\bM\d+-I\d+\b")


def frame_refs(md: Path) -> list[tuple[str, bool]]:
    out = []
    for ref in sorted(set(FRAME_REF.findall(md.read_text(encoding="utf-8")))):
        exists = (md.parent / ref).resolve().is_file() or (REPO / ref).resolve().is_file()
        out.append((ref, exists))
    return out


def open_questions_text(doc: str) -> str:
    m = re.search(r"^(#{1,3})\s*(?:\d+\.?\s*)?open questions.*$", doc, re.I | re.M)
    if not m:
        return ""
    level = len(m.group(1))
    rest = doc[m.end():]
    nxt = re.search(rf"^#{{1,{level}}}\s", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def main() -> int:
    fails: list[str] = []
    milestones = read_json(MILESTONES)["milestones"]
    breakdowns = []
    for m in milestones:
        p = BREAKDOWNS / m["id"] / "breakdown.md"
        if p.is_file():
            breakdowns.append(p)
        else:
            fails.append(f"[1] missing breakdown for {m['id']}: {p.relative_to(REPO).as_posix()}")

    docs = breakdowns + ([DESIGN_DOC] if DESIGN_DOC.is_file() else [])
    n_refs = 0
    for md in docs:
        for ref, ok in frame_refs(md):
            n_refs += 1
            if not ok:
                fails.append(f"[2] {md.relative_to(REPO).as_posix()} references missing frame {ref}")

    doc = DESIGN_DOC.read_text(encoding="utf-8") if DESIGN_DOC.is_file() else ""
    if not doc:
        fails.append("[3] design_document.md missing")
    headings = "\n".join(re.findall(r"^#{1,3}\s.*$", doc, re.M)).lower()
    for name, pat in SECTIONS.items():
        if doc and not re.search(pat, headings):
            fails.append(f"[3] design doc lacks section {name}")

    oq = open_questions_text(doc)
    n_inferred = 0
    for md in breakdowns:
        for i, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if "[inferred]" not in line.lower():
                continue
            ids = INFERRED_ID.findall(line)
            n_inferred += line.lower().count("[inferred]")
            where = f"{md.relative_to(REPO).as_posix()}:{i}"
            if not ids:
                fails.append(f"[4] {where} has an [inferred] item without an M#-I## id")
            for iid in ids:
                if not re.search(rf"\b{re.escape(iid)}\b", oq):
                    fails.append(f"[4] {iid} ({where}) not in design doc Open Questions")

    print(f"milestones={len(milestones)} breakdowns={len(breakdowns)} frame_refs={n_refs} inferred_tags={n_inferred}")
    for f in fails:
        print("FAIL", f)
    print("PASS" if not fails else f"{len(fails)} failure(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
