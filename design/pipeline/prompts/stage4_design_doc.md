# Stage 4 brief: design document

Repo root: `C:\Users\beanw\plane-geo`. Python: `design/.venv/Scripts/python`. Run commands from the repo root.

## Inputs
Read in full: `design/02_milestones/milestones.json`, every `design/03_breakdowns/M*/breakdown.md`, and `design/00_source/source.json`. When you need to confirm a detail, open the key frame with Read.

## Output
Write `design/04_design/design_document.md`. It must be detailed enough to rebuild the project without watching the video. Use these exact numbered H2 headings:

1. `## 1. Overview` covers what the project is, what it does, and the final result.
2. `## 2. System architecture` covers each system, its responsibilities, and the interfaces between systems (data shapes and formats), with a Mermaid block diagram.
3. `## 3. Bill of materials` is consolidated and deduplicated. List the data sources, datasets, hardware, and services, with quantities, specs, and source timestamps.
4. `## 4. Tools and software`
5. `## 5. Build plan` lists the milestones in order. Each has prerequisites, steps, acceptance criteria, and key frames embedded as `![caption](../03_breakdowns/M#/frames/M#_HHMMSS.png)`.
6. `## 6. Per-system detailed design` covers specs, algorithms, formulas, code, config, and parameters.
7. `## 7. Lessons from the video` covers the problems the creator hit and how they resolved them.
8. `## 8. Open questions and assumptions` lists every `[inferred]` item and every gap from every breakdown, grouped by system with one H3 per system. Each item keeps its id (such as `M3-I04`), states the best guess and confidence, and links its breakdown. Do not drop any id. To merge duplicates, list all their ids on one item.
9. `## 9. Suggested improvements for the rebuild` is kept clearly separate from what the video shows.
10. `## 10. Proposed layout for src/` describes how to organize the rebuild in this repo, based on the systems.

Keep the `[shown]`, `[stated]`, and `[inferred]` tags on facts carried over from the breakdowns. Never upgrade an inferred spec.

Formatting: plain markdown, compact, with tables where they help. Use colour only inside Mermaid diagrams, with no coloured text, badges, or emoji. `design/pipeline/render_doc.py` produces the styled HTML version (white background, Arial 10pt, greyscale headings).

Do not edit any other file. Do not commit.

## Check
Run `design/.venv/Scripts/python design/pipeline/verify.py`. Fix every failure that comes from the design doc until checks 2 to 4 pass for it. Then run `design/.venv/Scripts/python design/pipeline/render_doc.py`.

## Report
Under 150 words. Give the verify.py output, the word count of each section, and anything you could not resolve.
