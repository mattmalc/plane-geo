# Design pipeline

This pipeline turns the source video into `04_design/design_document.md`, a document detailed enough to rebuild the project without watching the video. It runs in five stages. Each stage reads the previous stage's files from disk and writes only its own folder, so you can rerun any stage by itself.

| Stage | Output | Run by |
| --- | --- | --- |
| 0. Source | `00_source/source.json` | `pipeline/source.py` |
| 1. Transcript | `01_transcript/transcript.json`, `transcript.md` | `pipeline/transcribe.py` |
| 2. Milestones and systems | `02_milestones/milestones.json`, `milestones.md` | One agent with `pipeline/prompts/stage2_milestones.md`, checked by `pipeline/check_milestones.py` |
| 3. Breakdowns | `03_breakdowns/M#/breakdown.md`, `frames/` | One agent per milestone with `pipeline/prompts/stage3_worker.md`, using `pipeline/frames.py` and `pipeline/transcript_slice.py` |
| 4. Design document | `04_design/design_document.md`, `design_document.html` | One agent with `pipeline/prompts/stage4_design_doc.md`, then `pipeline/render_doc.py` |
| Verify | exit code 0 | `pipeline/verify.py` |

`logs/decisions.tsv` records every judgment call, one row per call. `logs/errors.log` records steps that failed twice. `logs/run_summary.md` summarises the last full run.

## Requirements

- Python 3.10 to 3.12. The pinned `ctranslate2` wheels do not support 3.13 or later yet.
- An NVIDIA GPU is optional. With one, Stage 1 runs Whisper `large-v3` on CUDA. Without one, it falls back to `medium` on CPU, which is much slower.
- Git LFS, which stores the frames.
- The source video on local disk. The pipeline never downloads it. This run fetched it with [yt-tools](https://github.com/mattmalc/yt-tools) (`yt-tools video UytYrhYLOKI --max-height 720`).

ffmpeg comes bundled through `imageio-ffmpeg`, so no system install is needed.

```sh
uv venv --python 3.12 design/.venv
uv pip install --python design/.venv -r design/requirements.txt
```

## Rerunning a stage

Run these from the repo root. `PY` stands for `design/.venv/Scripts/python` on Windows or `design/.venv/bin/python` elsewhere.

```sh
PY design/pipeline/source.py --video /path/to/video.mp4    # stage 0
PY design/pipeline/transcribe.py                           # stage 1
PY design/pipeline/check_milestones.py                     # after stage 2
PY design/pipeline/frames.py --help                        # stage 3 frame tool
PY design/pipeline/render_doc.py                           # after stage 4
PY design/pipeline/verify.py                               # finish checks 1 to 4
```

Stages 2, 3, and 4 need judgment, so an agent runs them. To rerun one, give a coding agent (Claude Code here) the matching brief from `pipeline/prompts/`. For Stage 3, replace `{MID}` with the milestone id. Each brief names the files the stage may write. A Stage 3 worker starts with `frames.py clean M#`, so a rerun replaces that milestone's frames and leaves the others alone.

`pipeline/run_stage.sh "<message>" <paths>` commits and pushes one stage's outputs.

## Conventions

- Timestamps are `HH:MM:SS`. Frames are `03_breakdowns/M#/frames/M#_HHMMSS.png`.
- Every fact in a breakdown is tagged `[shown]` (on screen), `[stated]` (said aloud or in the description), or `[inferred]` (reasoned). Each `[inferred]` item has an id such as `M3-I04`. `verify.py` checks that every id appears in the design doc's Open Questions section.
- Markdown cannot carry styling. `render_doc.py` writes `design_document.html` with the required look: white background, Arial 10pt, compact spacing, and greyscale headings, with colour only inside Mermaid diagrams.

## What verify.py checks

1. Every milestone in `milestones.json` has a `breakdown.md`.
2. Every frame path referenced in a breakdown or the design doc exists.
3. The design doc has all 10 required sections.
4. Every `[inferred]` id in the breakdowns appears in the design doc's Open Questions section.
