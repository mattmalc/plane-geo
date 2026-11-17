# Stage 2 brief: milestones and systems

Repo root: `C:\Users\beanw\plane-geo`. Python: `design/.venv/Scripts/python`. Run commands from the repo root.

## Inputs
- `design/00_source/source.json` holds the title, duration, chapters, and description. The description includes a methodology summary. Treat it as [stated] by the creator.
- `design/01_transcript/transcript.md`. Read all of it.

## Task
Identify:
1. **Milestones.** The order in which the project gets built or the investigation proceeds.
2. **Systems.** The functional subsystems of the finished project. One system can span several milestones, and one milestone can touch several systems.

Write `design/02_milestones/milestones.json` with exactly this schema:

```json
{
  "project_summary": "...",
  "systems": [{"id": "S1", "name": "...", "description": "..."}],
  "milestones": [{
    "id": "M1", "title": "...", "start": "HH:MM:SS", "end": "HH:MM:SS",
    "summary": "...", "systems": ["S1"],
    "parts_tools_software": ["..."],
    "visual_moments": [{"t": "HH:MM:SS", "reason": "..."}]
  }]
}
```

A visual moment is a time when the picture matters more than the speech. Examples are "like this", "as you can see", "here", a plot, a spectrogram, a map, code, a schematic, a measurement, or a UI on screen. Be generous, because Stage 3 extracts a frame at every one.

Also write `design/02_milestones/milestones.md`, a readable table of the same content.

## Self-check
Fix problems yourself, then log each change.
- Milestones are contiguous. No gaps or overlaps are allowed, except an intro before M1 and an outro after the last milestone.
- No milestone is longer than about 15% of the video's duration. Split any that are.
- No milestone is shorter than about 1 minute. Merge any that are into a neighbour.
- If the video has YouTube chapters, align boundaries to them where sensible.

Log every split, merge, boundary call, or ambiguous call with this command. Write the log text plainly.

`bash design/pipeline/log.sh design/logs/decisions.tsv stage2 "<decision>" "<why>" "<evidence path or timestamp>" "<result>"`

Then run `design/.venv/Scripts/python design/pipeline/check_milestones.py` and fix anything it reports until it prints PASS.

Edit nothing outside `design/02_milestones/` and the decisions log. Do not commit.

## Report
Under 200 words. Give the number of milestones and systems, one line per milestone with its title and times, every split or merge you made, and the check_milestones output.
