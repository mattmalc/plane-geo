# M4 breakdown: Filter grid points by the 920-second offset

Range: 00:07:04 to 00:08:21. System: S4.

## 1. Goal and done criteria

Goal. Keep only grid points that heard one plane and then another plane 920 s later. [stated]

Input. Every grid point carries a list of flight IDs and the delayed CPA time of each flight at that point. [stated] [00:06:50]

Done looks like this:
- Every grid point is tested for any pair of delayed CPA times 920 s apart, within a tolerance of about 5 s either way. [stated] [00:07:34]
- The surviving point set exists as a layer. In the test area it holds about 35,000 points. [stated] [00:07:49]
- The survivors are recognised as still far too many for a US-wide search, which motivates the Doppler constraints in M5 onward. [stated] [00:08:21]

## 2. Procedure

1. Start from the M3 output: a grid of points, each holding the flight IDs and delayed CPA times of every flight it heard. [stated] [00:06:50] The QGIS attribute panel shows one such point. [shown] ![](frames/M4_000712.png)
2. Restate the target. The audio holds two flyovers whose curves sit 920 s apart. [stated] [00:07:04] The graphic shows two plane icons under a spectrogram, bracketed "920 sec". [shown] ![](frames/M4_000704.png)
3. For each point, place the delayed CPA times on a timeline. [stated] [00:07:10] The "CPA Timeline" tool draws one green vertical line with a blue dot per CPA time. [shown] ![](frames/M4_000713.png)
4. Slide a fixed 920 s window across the timeline. The window is drawn as two vertical bars joined by a dashed line. [shown] [00:07:14] ![](frames/M4_000719.png)
5. Check both window edges against CPA times. When only one edge lands on a CPA time, that edge label turns green and the other stays white. [shown] [00:07:20] ![](frames/M4_000720.png) When neither edge lands, there is no match. [shown] [00:07:23] ![](frames/M4_000723.png) ![](frames/M4_000726.png)
6. When both edges land on CPA times, both labels turn green and the window turns green. That point passes. [shown] [00:07:28] ![](frames/M4_000730.png)
7. Allow tolerance. Where the "centre" of a Doppler curve is placed is a judgment, so the window edge has about ±5 s of slack. [stated] [00:07:34] The creator moves the spectrogram cursor across one curve to show the ambiguity. [shown] ![](frames/M4_000735.png) ![](frames/M4_000736.png) ![](frames/M4_000740.png) Zoomed in, each window edge carries a shaded tolerance band. [shown] [00:07:43] ![](frames/M4_000743.png)
8. Run the check over every grid point in the test area. [stated] The pre-filter grid is a dense layer covering the whole test area. [shown] [00:07:48] ![](frames/M4_000748.png)
9. Keep passing points. About 35,000 survive. They lie in strips along flight tracks. [stated] [00:07:49] [shown] ![](frames/M4_000752.png)
10. Put the result in scale. The test area is a small patch in the southeastern US, under 0.05% of continental US land area. [stated] [00:07:55] [shown] ![](frames/M4_000756.png)
11. Football-field comparison. Divide the continental US into football fields, lay them end to end, and the line wraps around the Earth and reaches the Moon and back almost 200 times. [stated] [00:08:05] ![](frames/M4_000809.png) ![](frames/M4_000811.png) ![](frames/M4_000813.png) ![](frames/M4_000817.png)
12. Conclusion: the offset filter alone cannot handle a US-wide search. More information is needed from the Doppler curves. [stated] [00:08:21]

## 3. Components

| Item | Value | Tag |
|---|---|---|
| Target offset between events | 920 s | [stated] [shown] (`Window length (s): 920`, frames/M4_000713.png) |
| Tolerance on each window edge | about ±5 s | [stated]; shaded band about 10 s wide at frames/M4_000743.png [shown] |
| Per-point attributes (QGIS layer `gridpoints_heard_multiple — points`) | `fid`, `n_flights`, `flight_ids`, `retarded_cpa_times` | [shown] frames/M4_000712.png |
| Example point | `fid` 203833, `n_flights` 8 | [shown] frames/M4_000712.png |
| Example `retarded_cpa_times` | 19:13:28, 19:08:49, 19:09:00, 18:30:20, 22:44:51, 23:49:35, 00:36:59, 01:16:28 | [shown] frames/M4_000712.png |
| Example `flight_ids` (first six) | 1100037924, 1100049757, 1100043136, 1100041036, 1099966250, 1100102896 | [shown] frames/M4_000712.png |
| Matching pair on timeline | left = 26:20:51, right = 26:36:11 (difference 920 s) | [shown] frames/M4_000730.png |
| Timeline span for example point | about 18:00 to 02:40 | [shown] frames/M4_000713.png |
| Survivors in test area | about 35,000 points | [stated] |
| Test area share of continental US | under 0.05% | [stated] |
| Grid spacing | 200 m, out to 10 km from each track (from M3) | [stated] in methodology and at [00:06:45] |
| Source recording length | 60:00.000 | [shown] frames/M4_000736.png |
| Spectrogram display band in this segment | 5 to 800 Hz | [shown] frames/M4_000736.png |
| Event 1 curve position | about 2143 to 2145 s into the audio | [shown] cursor 2143.450s and 2144.567s, frames/M4_000735.png, frames/M4_000740.png |

The `retarded_cpa_times` field is the same quantity the narration calls "delayed CPA time". [inferred] M4-I01

The order of `retarded_cpa_times` matches the order of `flight_ids`, so it is not sorted by time. [inferred] M4-I02

## 4. Systems touched

### S4 Candidate grid and constraint filters
- How it works. For each grid point, take its delayed CPA times and test whether any pair is 920 s apart within about ±5 s. Keep the point if a pair exists. [stated]
- Inputs. The grid point layer from S3/M3, with per-point `flight_ids` and `retarded_cpa_times`. [shown] The 920 s target offset, which comes from S2 spectrogram measurement of the two events. [stated]
- Outputs. A smaller point layer, about 35,000 points in the test area. [stated] Each survivor needs to keep which two flights formed the pair, because later stages model a curve per flight. [inferred] M4-I03
- Connections. Upstream: S3 supplies delayed CPA times; S2 supplies the offset. Downstream: M5+ add speed and slant-distance constraints and the silence constraint, then S5/S6 model and score Doppler curves. [stated] in the description. S7 (QGIS) is used to view the layers. [shown]

### S7 Map review (viewing only)
- QGIS displays the grid layers and the survivors over satellite imagery. [shown] frames/M4_000752.png
- The CPA Timeline tool is a separate interactive visualisation used to explain the check. It is not the filter itself. [inferred] M4-I04

## 5. Code, configs, formulas, and on-screen text

On-screen text, verbatim:
- `CPA Timeline` [shown]
- `Window length (s): 920` [shown]
- `left = 18:38:29    right = 18:53:49` [shown] (00:07:13)
- `left = 18:03:33    right = 18:18:53` (right in green) [shown] (00:07:20)
- `left = 22:20:11    right = 22:35:31` [shown] (00:07:26)
- `left = 26:20:51    right = 26:36:11` (both green) [shown] (00:07:30)
- `slide window` [shown]
- QGIS Identify Results: `gridpoints_heard_multiple — points [2]`, `fid 203833`, `n_flights 8`, `flight_ids 1100037924,1100049757,1100043136,1100041036,1099966250,1100102896,1100...`, `retarded_cpa_times 19:13:28,19:08:49,19:09:00,18:30:20,22:44:51,23:49:35,00:36:59,01:16:28` [shown]
- Graphic labels: `920 sec`, `Moon`, `x 200` [shown]

Formula. A point passes if there exist delayed CPA times t_i and t_j at that point such that [stated, written as plain text]:

    | (t_j - t_i) - 920 s | <= tol,   tol ≈ 5 s

The order is fixed: the earlier event is event 1. [inferred] M4-I05

Whether the two times must come from different flight IDs is not stated. A rebuild should require i and j to be different flights. [inferred] M4-I06

No code is shown. [shown] The description says no code will be released. [stated]

## 6. Tools and software

- QGIS, with satellite basemap layers (`google`, `bing`, `carto` in the layer list), a `dem_r...` layer, and a `test are...` layer group. [shown] frames/M4_000712.png
- A custom "CPA Timeline" web tool with a slider and a Plotly-style toolbar (camera, zoom, pan, box select, lasso, reset icons). [shown] The toolbar looks like Plotly, so it was likely built with Plotly or Dash. [inferred] M4-I07
- A custom spectrogram viewer with playback bar, time cursor, and a "Claude Code" status-bar label. [shown] frames/M4_000736.png
- Python for the pipeline. [stated] in the description.

## 7. Problems and fixes

- Problem: where a Doppler curve's centre sits is ambiguous, so a strict 920 s test would reject the true point. [stated] Fix: allow about ±5 s of slack on each edge. [stated] [shown] frames/M4_000743.png
- Problem: about 35,000 points still pass in an area under 0.05% of the continental US. Scaled up, this filter alone cannot search the country. [stated] Fix: add Doppler-derived constraints (speed, slant distance) in later milestones. [stated] at [00:08:21]

## 8. Gaps

1. Exact tolerance value and whether it is symmetric per edge or applied to the difference. Best guess: |Δt − 920| ≤ 5 s on the difference. Confidence: medium. [inferred] M4-I08
2. How the 920 s offset was measured from the spectrogram (curve centre, steepest slope, or fitted CPA). Best guess: difference of fitted CPA times from S2 curve fits. Confidence: medium. [inferred] M4-I09
3. Time format past 24 h (`26:20:51`). Best guess: seconds since midnight of the target day, so flights after midnight get hours above 24. Store times as epoch seconds in a rebuild. Confidence: high. [inferred] M4-I10
4. Whether one point can pass with several candidate pairs, and whether all pairs are kept. Best guess: keep every qualifying (flight A, flight B) pair per point. Confidence: medium. [inferred] M4-I11
5. Whether the recording time is restricted at this stage. The example timeline spans about 18:00 to 02:40, so no time window seems applied yet. Best guess: no time restriction in M4. Confidence: medium. [inferred] M4-I12
6. Test area bounds. The map shows a small patch in the southeastern US. Exact coordinates are not given. Best guess: a box of a few thousand km² around the true location. Confidence: low. [inferred] M4-I13
7. The QGIS example point (8 flights) and the timeline example (10 CPA lines) do not match, so they are probably different points. Treat the timeline as illustrative. Confidence: medium. [inferred] M4-I14
8. Algorithm for the check. Best guess: sort each point's times and use a two-pointer or binary search for t + 920 ± 5. This is O(n log n) per point. Confidence: high that this works, low that it matches the creator's code. [inferred] M4-I15
