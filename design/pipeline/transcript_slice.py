"""Print the transcript for one milestone's range plus padding. Usage: python transcript_slice.py M3 [--pad 30]"""
from __future__ import annotations

import argparse

from common import MILESTONES, TRANSCRIPT_DIR, read_json, secs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("mid")
    ap.add_argument("--pad", type=float, default=30)
    a = ap.parse_args()
    m = next(x for x in read_json(MILESTONES)["milestones"] if x["id"] == a.mid)
    lo, hi = secs(m["start"]) - a.pad, secs(m["end"]) + a.pad
    for s in read_json(TRANSCRIPT_DIR / "transcript.json")["segments"]:
        if s["end"] >= lo and s["start"] <= hi:
            print(f"[{s['t']}] {s['text']}")


if __name__ == "__main__":
    main()
