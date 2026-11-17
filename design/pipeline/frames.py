"""Stage 3 frame tool. Every frame lands at design/03_breakdowns/<M#>/frames/<M#>_HHMMSS.png.

  python frames.py clean  M3                          delete M3's frames (start of an idempotent rerun)
  python frames.py at     M3 00:05:12 00:05:40 ...    one frame per timestamp
  python frames.py scenes M3 --start 00:05:00 --end 00:09:00 [--threshold 0.3]
  python frames.py dense  M3 --start 00:06:10 --end 00:06:40 [--every 3]
  python frames.py dedupe M3 [--max-diff 2.5] [--protect 00:05:12 ...]
  python frames.py sheet  M3                          labelled contact sheets in design/.work/ (git-ignored)
  python frames.py list   M3

Each extraction command prints the paths it wrote.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path

from common import BREAKDOWNS, DESIGN, compact, ffmpeg, hms, secs, video_path


def frames_dir(mid: str) -> Path:
    d = BREAKDOWNS / mid / "frames"
    d.mkdir(parents=True, exist_ok=True)
    return d


def grab(mid: str, t: float) -> Path:
    out = frames_dir(mid) / f"{mid}_{compact(t)}.png"
    if not out.exists():
        subprocess.run([ffmpeg(), "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(video_path()),
                        "-frames:v", "1", str(out)], check=True)
    return out


def scene_times(start: float, end: float, threshold: float) -> list[float]:
    cmd = [ffmpeg(), "-hide_banner", "-ss", f"{start:.2f}", "-to", f"{end:.2f}", "-i", str(video_path()),
           "-an", "-vf", f"select='gt(scene,{threshold})',showinfo", "-f", "null", "-"]
    err = subprocess.run(cmd, capture_output=True, text=True).stderr
    return [start + float(m) for m in re.findall(r"pts_time:([\d.]+)", err)]


def thumb(path: Path):
    from PIL import Image
    import numpy as np
    return np.asarray(Image.open(path).convert("L").resize((64, 36)), dtype="float32")


def dedupe(mid: str, max_diff: float, protect: set[str]) -> list[Path]:
    removed, prev = [], None
    for p in sorted(frames_dir(mid).glob("*.png")):
        cur = thumb(p)
        if prev is not None and abs(cur - prev).mean() < max_diff and p.stem.split("_")[1] not in protect:
            p.unlink()
            removed.append(p)
            continue
        prev = cur
    return removed


def sheet(mid: str, per_sheet: int = 12) -> list[Path]:
    from PIL import Image, ImageDraw
    frames = sorted(frames_dir(mid).glob("*.png"))
    out_dir = DESIGN / ".work"
    out_dir.mkdir(exist_ok=True)
    for old in out_dir.glob(f"{mid}_sheet_*.jpg"):
        old.unlink()
    outs = []
    w, h, cols = 480, 270, 3
    for i in range(0, len(frames), per_sheet):
        chunk = frames[i:i + per_sheet]
        rows = (len(chunk) + cols - 1) // cols
        canvas = Image.new("RGB", (cols * w, rows * (h + 22)), "white")
        draw = ImageDraw.Draw(canvas)
        for j, f in enumerate(chunk):
            x, y = (j % cols) * w, (j // cols) * (h + 22)
            canvas.paste(Image.open(f).convert("RGB").resize((w, h)), (x, y + 22))
            draw.text((x + 4, y + 4), f.name, fill="black")
        out = out_dir / f"{mid}_sheet_{i // per_sheet + 1:02d}.jpg"
        canvas.save(out, quality=85)
        outs.append(out)
    return outs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["clean", "at", "scenes", "dense", "dedupe", "sheet", "list"])
    ap.add_argument("mid")
    ap.add_argument("times", nargs="*")
    ap.add_argument("--start")
    ap.add_argument("--end")
    ap.add_argument("--threshold", type=float, default=0.3)
    ap.add_argument("--every", type=float, default=3.0)
    ap.add_argument("--max-diff", type=float, default=2.5)
    ap.add_argument("--protect", nargs="*", default=[])
    a = ap.parse_args()

    if a.cmd == "clean":
        shutil.rmtree(BREAKDOWNS / a.mid / "frames", ignore_errors=True)
        frames_dir(a.mid)
        return
    if a.cmd == "at":
        paths = [grab(a.mid, secs(t)) for t in a.times]
    elif a.cmd == "scenes":
        paths = [grab(a.mid, t) for t in scene_times(secs(a.start), secs(a.end), a.threshold)]
    elif a.cmd == "dense":
        t, end, paths = secs(a.start), secs(a.end), []
        while t <= end:
            paths.append(grab(a.mid, t))
            t += a.every
    elif a.cmd == "dedupe":
        paths = dedupe(a.mid, a.max_diff, {compact(p) for p in a.protect})
        print(f"removed {len(paths)} near-duplicates")
    elif a.cmd == "sheet":
        paths = sheet(a.mid)
    else:
        paths = sorted(frames_dir(a.mid).glob("*.png"))
    for p in dict.fromkeys(paths):
        print(p.relative_to(DESIGN.parent).as_posix())


if __name__ == "__main__":
    main()
