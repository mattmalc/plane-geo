"""Stage 1: transcribe the source video with faster-whisper.

large-v3 on CUDA when a GPU is usable, otherwise medium on CPU.
Writes design/01_transcript/transcript.json and transcript.md.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from common import TRANSCRIPT_DIR, hms, log_error, read_json, SOURCE, video_path, write_json


def expose_cuda_wheels() -> None:
    """On Windows, put the pip-installed cuBLAS/cuDNN DLLs where ctranslate2 can load them."""
    if sys.platform != "win32":
        return
    import importlib.util
    for pkg in ("nvidia.cublas", "nvidia.cudnn"):
        spec = importlib.util.find_spec(pkg)
        if spec and spec.submodule_search_locations:
            bin_dir = Path(list(spec.submodule_search_locations)[0]) / "bin"
            if bin_dir.is_dir():
                os.add_dll_directory(str(bin_dir))
                os.environ["PATH"] = f"{bin_dir}{os.pathsep}{os.environ['PATH']}"


def load_model():
    from faster_whisper import WhisperModel
    expose_cuda_wheels()
    try:
        import ctranslate2
        if ctranslate2.get_cuda_device_count() > 0:
            return WhisperModel("large-v3", device="cuda", compute_type="float16"), "large-v3", "cuda"
    except Exception as e:  # noqa: BLE001  any CUDA load failure means CPU fallback
        log_error("stage1", f"CUDA load failed, falling back to medium on CPU: {e}")
    return WhisperModel("medium", device="cpu", compute_type="int8"), "medium", "cpu"


def main() -> None:
    model, name, device = load_model()
    segments, meta = model.transcribe(str(video_path()), beam_size=5, vad_filter=True,
                                      condition_on_previous_text=False)
    segs = [{"start": round(s.start, 2), "end": round(s.end, 2), "t": hms(s.start), "text": s.text.strip()}
            for s in segments]
    src = read_json(SOURCE)
    write_json(TRANSCRIPT_DIR / "transcript.json", {
        "model": name, "device": device, "language": meta.language,
        "video": src.get("title"), "segments": segs,
    })
    lines = [f"# Transcript: {src.get('title')}", "",
             f"Model `{name}` on `{device}`, language `{meta.language}`, {len(segs)} segments.", ""]
    lines += [f"[{s['t']}] {s['text']}" for s in segs]
    (TRANSCRIPT_DIR / "transcript.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(segs)} segments, model {name} on {device}")


if __name__ == "__main__":
    main()
