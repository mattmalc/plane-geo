"""Paths, timestamp helpers, and logging shared by every pipeline stage."""
from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
from pathlib import Path

DESIGN = Path(__file__).resolve().parent.parent
REPO = DESIGN.parent
SOURCE = DESIGN / "00_source" / "source.json"
TRANSCRIPT_DIR = DESIGN / "01_transcript"
MILESTONES = DESIGN / "02_milestones" / "milestones.json"
BREAKDOWNS = DESIGN / "03_breakdowns"
DESIGN_DOC = DESIGN / "04_design" / "design_document.md"
LOGS = DESIGN / "logs"


def ffmpeg() -> str:
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def hms(seconds: float) -> str:
    s = int(round(max(seconds, 0)))
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def secs(stamp: str) -> float:
    parts = [float(p) for p in stamp.strip("[]").split(":")]
    while len(parts) < 3:
        parts.insert(0, 0.0)
    h, m, s = parts
    return h * 3600 + m * 60 + s


def compact(stamp_or_secs: str | float) -> str:
    s = stamp_or_secs if isinstance(stamp_or_secs, str) else hms(stamp_or_secs)
    return s.replace(":", "")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def video_path() -> Path:
    p = Path(read_json(SOURCE)["video_path"])
    if not p.exists():
        raise SystemExit(f"video not found at {p}; rerun stage 0 (source.py) with --video")
    return p


def log_error(stage: str, message: str) -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with (LOGS / "errors.log").open("a", encoding="utf-8") as f:
        f.write(f"{stamp}\t{stage}\t{message.replace(chr(10), ' ')}\n")


def probe(path: Path) -> dict:
    """Width, height, fps, duration parsed from ffmpeg's stream banner (imageio-ffmpeg ships no ffprobe)."""
    out = subprocess.run([ffmpeg(), "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    info: dict = {}
    if m := re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", out):
        info["duration_s"] = int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3])
    if m := re.search(r"Video: .*?, (\d{2,5})x(\d{2,5})", out):
        info["width"], info["height"] = int(m[1]), int(m[2])
    if m := re.search(r"(\d+(?:\.\d+)?) fps", out):
        info["fps"] = float(m[1])
    return info
