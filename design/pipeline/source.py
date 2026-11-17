"""Stage 0: write design/00_source/source.json from the local video and its yt-tools metadata.

Usage: python source.py --video PATH [--info PATH_TO_info.json]
"""
from __future__ import annotations

import argparse
from pathlib import Path

from common import SOURCE, hms, probe, read_json, write_json


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True, type=Path)
    ap.add_argument("--info", type=Path, help="yt-tools info.json (defaults to the one beside the video)")
    args = ap.parse_args()

    video = args.video.resolve()
    info_path = args.info or video.with_name("info.json")
    meta = read_json(info_path) if info_path.exists() else {}
    local = probe(video)
    duration = local.get("duration_s") or meta.get("duration") or 0

    chapters = [
        {"title": c.get("title", ""), "start": hms(c["start_time"]), "end": hms(c["end_time"])}
        for c in (meta.get("chapters") or [])
    ]
    write_json(SOURCE, {
        "video_path": str(video),
        "url": meta.get("webpage_url"),
        "id": meta.get("id"),
        "title": meta.get("title"),
        "channel": meta.get("channel"),
        "upload_date": meta.get("upload_date"),
        "duration_s": round(duration, 2),
        "duration": hms(duration),
        "width": local.get("width"),
        "height": local.get("height"),
        "fps": local.get("fps"),
        "chapters": chapters,
        "description": meta.get("description"),
    })
    print(f"wrote {SOURCE} ({hms(duration)}, {local.get('width')}x{local.get('height')}, {len(chapters)} chapters)")


if __name__ == "__main__":
    main()
