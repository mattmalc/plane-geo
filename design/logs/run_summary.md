# Run summary

Run date: 2026-11-17. Source: [I discovered a sound that leaks your exact location (and it's everywhere)](https://www.youtube.com/watch?v=UytYrhYLOKI) by colsto, 29:12, 1280x720 at 60 fps, no YouTube chapters.

`design/pipeline/verify.py` prints `PASS` with 12 milestones, 12 breakdowns, 338 frame references, and 208 `[inferred]` tags. Counts below come from `design/pipeline/summarize.py`.

## Milestones and frames

| Milestone | Title | Range | Frames | [inferred] |
| --- | --- | --- | --- | --- |
| M1 | Problem setup and finding the Doppler curves | 00:00:17 to 00:02:37 | 29 | 14 |
| M2 | Download ADS-B data and keep propeller aircraft | 00:02:37 to 00:04:14 | 15 | 13 |
| M3 | Grid candidate points and compute delayed CPA times | 00:04:14 to 00:07:04 | 34 | 28 |
| M4 | Filter grid points by the 920-second offset | 00:07:04 to 00:08:21 | 19 | 15 |
| M5 | Measure speed, slant distance, and CPA time from each Doppler curve | 00:08:21 to 00:10:38 | 26 | 18 |
| M6 | Apply speed, slant-distance, and silence filters | 00:10:38 to 00:13:35 | 22 | 23 |
| M7 | Forward-model the Doppler curve from real flight geometry | 00:13:35 to 00:16:45 | 28 | 9 |
| M8 | Correct the model for sound travel time | 00:16:45 to 00:18:10 | 14 | 17 |
| M9 | Score modelled curves with locked two-event scoring | 00:18:10 to 00:20:59 | 21 | 20 |
| M10 | Rank candidates by flight pair and inspect the top hits | 00:20:59 to 00:22:41 | 30 | 19 |
| M11 | Confirm with a one-minute known-time clip and Street View | 00:22:41 to 00:26:08 | 31 | 17 |
| M12 | Test countermeasures | 00:26:08 to 00:28:09 | 28 | 15 |

That makes 297 frames in total, all PNG in Git LFS. The intro (00:00:00 to 00:00:17) and outro (00:28:09 to 00:29:12) are outside the milestones.

## Open questions per system

These are the unique ids in section 8 of the design doc. 212 ids are unique overall: the 208 `[inferred]` ids from the breakdowns plus the doc's own cross-milestone items (D-##). Some ids appear under more than one system.

| System | Ids |
| --- | --- |
| S1. ADS-B ingest and aircraft filtering | 19 |
| S2. Spectrogram measurement | 36 |
| S3. Acoustic geometry and propagation | 30 |
| S4. Candidate grid and constraint filters | 33 |
| S5. Doppler curve forward model | 20 |
| S6. Spectrogram scoring and ranking | 45 |
| S7. Map review and ground truth | 15 |
| S8. Countermeasure tests | 15 |

## Stages

| Stage | Result | Notes |
| --- | --- | --- |
| 0. Source | Ran with a change | The brief's video path was a placeholder. At the user's direction the video was downloaded with yt-tools at 720p. |
| 1. Transcript | OK | faster-whisper `large-v3` on CUDA (RTX 5090), 333 segments. No CPU fallback. |
| 2. Milestones | OK | One split (M7/M8, which would have been 275 s against a 263 s limit) and one merge (Street View into M11). `check_milestones.py` passes. Boundaries and visual moments are interpolated within segments, because there are no word-level timestamps. |
| 3. Breakdowns | OK, with fixes | 12 of 12 workers reported PASS. In 6 milestones, `frames.py dedupe` deleted frames whose only change was on-screen text, and the workers re-extracted them. Dedupe now compares 256x144 thumbnails for reruns. Some visual moments landed on frames with no useful content. Each worker kept one frame for those and logged it. |
| 4. Design document | OK | Section 8 reconciles several cross-milestone conflicts (D-01) and leaves four unresolved: the CPA example time, the 930 s timeline readout, 8:37 PM UTC against the filename time, and an M11 curve time. |
| Writing pass | OK | technical-writing and unslop were run over the design doc and both READMEs. The creator's pronouns are not stated in the source, so gendered pronouns were replaced with "the creator". |

No stage failed. `errors.log` is empty.

## Known limits

- The styled version of the doc is `design/04_design/design_document.html`, because markdown cannot carry fonts or colours. Its Mermaid diagram loads from a CDN, so it draws only with network access.
- The video releases no code. Section 6 reconstructs the algorithms from on-screen code and plots, and anything reconstructed is tagged `[inferred]` with an id.
- The source video lives in the yt-tools cache, outside the repo. Its path is in `design/00_source/source.json`.
