"""Stage 2 self-check for milestones.json: schema, contiguity, and length limits.

Rules: milestones are contiguous (intro before M1 and outro after the last are allowed),
none longer than 15% of the video (+1% slack), none shorter than 60 s, visual moments
inside their milestone. Usage: python check_milestones.py
"""
from __future__ import annotations

import re
import sys

from common import MILESTONES, SOURCE, read_json, secs

STAMP = re.compile(r"^\d{2}:\d{2}:\d{2}$")


def main() -> int:
    data = read_json(MILESTONES)
    duration = read_json(SOURCE)["duration_s"]
    sys_ids = {s["id"] for s in data.get("systems", [])}
    fails = []
    if not data.get("project_summary"):
        fails.append("project_summary empty")
    ms = data.get("milestones", [])
    for i, m in enumerate(ms):
        mid = m.get("id")
        if mid != f"M{i + 1}":
            fails.append(f"milestone {i} has id {mid}, expected M{i + 1}")
        for k in ("title", "start", "end", "summary", "systems", "parts_tools_software", "visual_moments"):
            if k not in m:
                fails.append(f"{mid} missing {k}")
        if not (STAMP.match(m.get("start", "")) and STAMP.match(m.get("end", ""))):
            fails.append(f"{mid} start/end not HH:MM:SS")
            continue
        a, b = secs(m["start"]), secs(m["end"])
        length = b - a
        if length <= 0:
            fails.append(f"{mid} ends before it starts")
        if length > 0.16 * duration:
            fails.append(f"{mid} is {length:.0f}s, over 15% of {duration:.0f}s; split it")
        if length < 60:
            fails.append(f"{mid} is {length:.0f}s, under 60s; merge it")
        if i and m["start"] != ms[i - 1]["end"]:
            fails.append(f"{mid} starts {m['start']} but {ms[i - 1]['id']} ends {ms[i - 1]['end']} (gap or overlap)")
        for s in m.get("systems", []):
            if s not in sys_ids:
                fails.append(f"{mid} references unknown system {s}")
        for v in m.get("visual_moments", []):
            if not STAMP.match(v.get("t", "")) or not a <= secs(v["t"]) <= b:
                fails.append(f"{mid} visual moment {v.get('t')} outside {m['start']}-{m['end']}")
    if ms and secs(ms[-1]["end"]) > duration + 1:
        fails.append(f"last milestone ends after the video ({duration:.0f}s)")
    for f in fails:
        print("FAIL", f)
    print(f"{len(ms)} milestones, {len(sys_ids)} systems: " + ("PASS" if not fails else f"{len(fails)} failure(s)"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
