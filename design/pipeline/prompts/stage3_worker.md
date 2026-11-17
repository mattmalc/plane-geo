# Stage 3 brief: breakdown for milestone {MID}

Repo root: `C:\Users\beanw\plane-geo`. Run every command from the repo root. `PY` means `design/.venv/Scripts/python`.

You own `design/03_breakdowns/{MID}/` and nothing else. Do not touch other milestone folders, other files, or git. You may append to `design/logs/decisions.tsv` (only through `log.sh`) and to `design/logs/errors.log`.

## Inputs
- Your milestone entry is id `{MID}` in `design/02_milestones/milestones.json`.
- The system list is in the same file.
- Get your transcript slice, padded by 30 s on each side, with `PY design/pipeline/transcript_slice.py {MID}`.
- The video path is in `design/00_source/source.json`. `frames.py` reads it for you.
- The creator's methodology summary is the `description` field of `design/00_source/source.json`.

## Frames
1. Run `PY design/pipeline/frames.py clean {MID}` first so a rerun starts clean.
2. Run `PY design/pipeline/frames.py at {MID} <t> <t> ...` for every visual_moment timestamp. This step is mandatory.
3. Run `PY design/pipeline/frames.py scenes {MID} --start <start> --end <end> --threshold 0.3` over the full milestone range.
4. For dense segments, run `PY design/pipeline/frames.py dense {MID} --start <t> --end <t> --every 2`, using a 2 to 5 s interval. Dense segments include code, plots, spectrograms, maps, UI, formulas, tables, and hardware close-ups.
5. **Look at every frame.** Run `frames.py sheet {MID}` to build labelled contact sheets in `design/.work/`, then Read each sheet image. Wherever detail matters (numbers, code, axis labels, map labels, UI text), open the individual frame with Read. If a frame is blurry, mid-transition, or cuts the detail off, grab frames 0.5 to 2 s around it with `frames.py at` until one is legible. Never describe a frame from the transcript alone.
6. Delete duplicate and useless frames, such as black frames, transitions, talking heads that add nothing, and near-duplicates. `frames.py dedupe {MID} --protect <visual moment times>` removes near-duplicates. Delete the rest by hand with `rm`. Keep every frame the breakdown cites.
7. If a visual moment shows nothing useful, keep one frame anyway, say so in the breakdown, and log the call.

Frames are named `{MID}_HHMMSS.png`. In breakdown.md, reference them by the relative path `frames/{MID}_HHMMSS.png`. Every frame path you write must exist on disk.

## breakdown.md
Write `design/03_breakdowns/{MID}/breakdown.md` with these sections:
1. **Goal and done criteria.** What this milestone achieves and what "done" looks like.
2. **Procedure.** Numbered steps in build order. Each step cites timestamps as `[HH:MM:SS]` and frames as markdown images or links.
3. **Components.** Data sources, datasets, hardware, parameters, constants, thresholds, values, units, and file formats, with quantities and specs. Read them off the screen where visible.
4. **Systems touched.** For each system id, cover how it works, its inputs and outputs, and how it connects to other systems.
5. **Code, configs, formulas, and on-screen text.** Transcribe them from the screen verbatim where legible. Write formulas in plain text or LaTeX.
6. **Tools and software.**
7. **Problems and fixes.** What the creator ran into and how they resolved it.
8. **Gaps.** Anything not shown or explained that a rebuild needs. Give each a best guess and a confidence level of high, medium, or low.

Tag every fact as `[shown]` (visible on screen), `[stated]` (said aloud or written in the description), or `[inferred]` (your own reasoning). Never present an inferred spec as shown or stated.

**Give every `[inferred]` tag a unique id on the same line, written as `[inferred] {MID}-I01`, `{MID}-I02`, and so on.** Every Gap item is inferred, so each one carries an id too. Stage 4 copies every id into the design doc's Open Questions section, and `verify.py` checks that it did.

## Judgment calls
Log every judgment call, such as a skipped frame, an ambiguous spec, or a degraded fallback, with this command:

`bash design/pipeline/log.sh design/logs/decisions.tsv stage3-{MID} "<decision>" "<why>" "<evidence>" "<result>"`

If a command fails, retry it once. If it fails again, append a line to `design/logs/errors.log` and continue.

## Done check
Before you report, confirm that every `frames/...png` path in breakdown.md exists on disk and that every `[inferred]` line has an id.

## Report
Under 150 words, nothing else. Start with `PASS`, `ISSUES`, or `BLOCKED`. Then give the frames kept and deleted, the counts of [shown], [stated], and [inferred] tags, the 3 most important specs you read off the screen, and any problems.
