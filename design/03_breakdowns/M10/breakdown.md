# M10 breakdown: Rank candidates by flight pair and inspect the top hits

Range: 00:20:59 to 00:22:41. Systems: S6, S7.

## 1. Goal and done criteria

Goal: turn the scored candidate cloud into one ranked answer. Each candidate has an event 1 score and an event 2 score [stated]. Group candidates by flight pair, keep the best point per pair, rank the pairs, and confirm the leader visually on spectrograms and on a map [stated].

Done when:
- A scatter plot of event 1 score against event 2 score exists for every surviving candidate [shown].
- A best-point-per-flight-pair view exists, and one pair clearly leads [shown].
- A "Top N flight-pair combos" page shows the modelled curve over the observed spectrogram for both events of each top pair [shown].
- The scored points and per-event heat maps for the winning flights load in QGIS [shown].
- The leader's modelled curves cover both observed curves, and the runners-up visibly miss [stated].

## 2. Procedure

1. Finish scoring every candidate point [stated] [00:20:54]. The first frame at the results cue still shows the previous M9 step-by-step Doppler slide and carries no results content [shown]: [frame](frames/M10_002101.png).
2. Plot every surviving candidate as x = event 1 score, y = event 2 score [shown] [00:21:01]-[00:21:07]. The plot shows 29245 points [shown]. Higher is better, so look in the top right [stated] [00:21:07].
   ![scatter all](frames/M10_002107.png)
3. Hover points to read flight IDs, lat/lon, and scores [shown] [00:21:11]. One hovered point reads flight1=1100069709, flight2=1100048665, score_1=10.737, score_2=7.141, match_score=17.878 [shown] (partly blurred). No single point stands out yet [stated].
   ![hover](frames/M10_002111.png)
4. Zoom into the top-right region [shown] [00:21:13]: [zoom, ungrouped](frames/M10_002114.png), [zoom, later](frames/M10_002126.png).
5. Note that each flight pair produces a cluster of grid points [stated] [00:21:14]. The video cuts to QGIS, showing a candidate cluster on a regular grid, coloured dark red to orange [shown] [00:21:19]: [QGIS cluster](frames/M10_002119.png).
6. Tick "color by flight-pair combo" [shown] [00:21:26]. Status line: "51 unique flight-pair combo(s) in current view (of 195 total) -- 29245 point(s) shown" [shown]: [coloured](frames/M10_002129.png).
7. Tick "show only best point per combo (by match_score)" [shown] [00:21:29]. Status line: "41 unique flight-pair combo(s) in current view (of 195 total) -- 195 point(s) shown" [shown]. One point now sits far above the rest at about (10.64, 9.84) [shown] [00:21:32].
   ![best per pair](frames/M10_002132.png)
8. Hover the leader [shown] [00:21:39]: flight1=1100069709, flight2=1100048665, lat=40.8764657, lon=-73.5249506, score_1=10.638, score_2=9.845, match_score=20.483 [shown].
   ![leader](frames/M10_002139.png)
9. Open the "Top 7 flight-pair combos -- best point per combo (by match_score alone)" page [shown] [00:21:42]. Each combo has an event 1 panel and an event 2 panel, with the red modelled curve over the spectrogram [shown].
   ![top 7](frames/M10_002142.png)
10. Inspect combo 1/7, event 1, score 10.64. The red curve covers the observed curve so fully that the curve is hidden [stated] [00:21:45]: [frame](frames/M10_002147.png), [frame](frames/M10_002148.png).
11. Inspect combo 1/7, event 2, score 9.84 (LOCKED). The match is similar [stated] [00:21:48]: [frame](frames/M10_002150.png).
12. Inspect combo 2/7, combined 15.25, event 1 score 9.52 [shown] [00:21:54]-[00:21:59]. It misses the top bit of the curve and is slightly off in the centre [stated]: [frame](frames/M10_002157.png), [frame](frames/M10_002159.png). Toggle "show predicted curve" off to see the faint observed curve [shown]: [frame](frames/M10_002201.png).
13. Compare event 1 scores: 9.52 for combo 2 against 10.64 for combo 1 ("a nine five ... a 10 six") [stated] [00:22:01]-[00:22:05]: [frame](frames/M10_002204.png).
14. Inspect combo 2/7, event 2, score 5.73 (LOCKED). It is badly off, and this drags its total down [stated] [00:22:05]-[00:22:11]: [overlay on](frames/M10_002208.png), [overlay off](frames/M10_002211.png).
15. Inspect combo 3/7, combined 15.04, event 1 score 7.90 [shown] [00:22:15]. It is worse on event 1 and a little better on event 2 than combo 2 [stated]: [frame](frames/M10_002215.png), [hover](frames/M10_002217.png). Scroll past combo 4/7 (14.87) and combo 5/7 (14.85) [shown]: [frame](frames/M10_002219.png), [frame](frames/M10_002220.png). "None of these are even close. And then first place is spot on." [stated] [00:22:15]-[00:22:20].
16. Scroll back to the top of the page [shown] [00:22:22]: [frame](frames/M10_002222.png).
17. Load the scored points in QGIS at the leader's location [shown] [00:22:25]. A red grid cluster sits on a bay shoreline [shown]: [frame](frames/M10_002225.png).
18. Now that the flight IDs are known, rerun scoring at much finer resolution with only those flights [stated] [00:22:26]. Show the event 1 heat map with its flight path (yellow dotted line) [shown] [00:22:32]: [frame](frames/M10_002232.png).
19. Show the event 2 flight path (red dotted line) [shown] [00:22:36], then its heat map [shown] [00:22:38]: [path](frames/M10_002236.png), [heat map](frames/M10_002238.png).
20. Show the combined heat map: one red peak near the shoreline [shown] [00:22:40]: [frame](frames/M10_002240.png), [frame](frames/M10_002241.png).

## 3. Components

- Candidate count in the scatter plot: 29245 points [shown].
- Flight-pair combos: 195 total [shown]. In the zoomed view, 51 are visible ungrouped and 41 with best-only [shown]. The best-only view shows 195 points, one per combo [shown].
- Event labels in the plot title: "1:35:52 vs 1:51:13" [shown]. These are the CPA times of event 1 and event 2 in the recording [inferred] M10-I01. 1:35:52 = 5752 s and 1:51:13 = 6673 s, a gap of 921 s, consistent with the 920 s offset [inferred] M10-I02.
- Scatter axis ranges, full view: x from about -3 to 11, y from about -6 to 10 [shown].
- Ranking key: match_score [shown]. match_score = score_1 + score_2. The leader's tooltip shows 10.638 + 9.845 = 20.483 [shown].
- Spectrogram panels: event 1 x axis 5700 to 5880 s, y about 80 to 190 Hz. Event 2 x axis about 6635 to 6740 s, y about 100 to 185 Hz [shown]. Axis labels: "elapsed recording time (s)", "frequency (Hz)" [shown]. Colormap: blue, with a bright observed curve. Model curve: red [shown].
- One event 2 panel (combo 4/7) uses a y axis up to about 600 Hz [shown]: [frame](frames/M10_002219.png).
- Top 7 table, as shown:

| Rank | flight1 | flight2 | lat, lon | combined | event 1 | event 2 |
|---|---|---|---|---|---|---|
| 1 | 1100069709 | 1100048665 | 40.876466, -73.524951 | 20.48 | 10.64 | 9.84 |
| 2 | 1100088546 | 1100072793 | 45.699498, -73.643756 | 15.25 | 9.52 | 5.73 |
| 3 | 1100029918 | 1100060374 | 36.454080, -94.456016 | 15.04 | 7.90 | not legible |
| 4 | 1100065108 | 1100061857 | 42.012829, -81.426671 | 14.87 | 8.33 | 6.54 |
| 5 | 1100069287 | 1100070751 | 43.437551, -79.358276 | 14.85 | 5.75 | not shown |

All rows above are [shown]. Combo 3's event 2 score is 15.04 - 7.90 = 7.14 [inferred] M10-I03. Combo 5's event 2 score is 14.85 - 5.75 = 9.10 [inferred] M10-I04.
- Leader coordinate: 40.876466, -73.524951 [shown]. This is on the north shore of Long Island, New York [inferred] M10-I05.
- The leader's lat/lon in the scatter tooltip (40.8764657, -73.5249506) matches the Top 7 header to 6 decimals [shown].
- Fine heat map: a square raster of about 128 x 128 screen pixels at the zoom shown. Colour ramp runs dark blue (low) through green and yellow to dark red (high) [shown].
- Event 1 and event 2 heat maps each show a diagonal ridge, the band of points at the right slant distance from that flight's track [shown]. The ridges cross at the combined peak [inferred] M10-I06.

## 4. Systems touched

### S6 Spectrogram scoring and ranking
- How it works: each candidate already has an event 1 score (event 1 isolated) and an event 2 score (locked to event 1) from `curve_match_scores_locked_spectrogram` [shown]. Candidates are grouped by (flight1, flight2), and the max-match_score point per group is kept [shown]. Groups are ranked by that score [shown].
- Inputs: the final output of `1_2b_v7.py`, i.e. every surviving candidate with flight IDs, lat/lon, score_1, score_2, and match_score [shown]. Also the observed spectrogram windows and the modelled curves from S5 [inferred] M10-I07.
- Outputs: an interactive scatter plot, a Top-N per-combo page with overlays, and a ranked list of flight pairs [shown]. The winning flight IDs feed a fine-resolution rerun [stated].
- Connections: consumes S4 candidates and S5 curves. Feeds S7 with the scored points and the winning flight IDs [stated].

### S7 Map review and ground-truth confirmation
- How it works: scored points and fine-resolution heat maps load as QGIS layers on a Google satellite basemap [shown]. The layers sit under the "event scores" and "flightpaths" groups [shown].
- Inputs: scored candidate points, fine-grid scores per event and combined, and flight paths for the winning flights [shown].
- Outputs: a visual location estimate, the peak of the combined heat map [shown]. Street View confirmation follows in a later milestone [stated].
- Connections: takes S6 output. Also reruns S5/S6 at finer resolution for the two winning flights [stated].

## 5. Code, configs, formulas, and on-screen text

Scatter page, verbatim [shown]:
```
Event1 Score vs Event2 Score (1:35:52 vs 1:51:13)
Every surviving candidate from 1_2b_v7.py's own final output. x = this candidate's event1 score, y = its event2
score (both from curve_match_scores_locked_spectrogram -- event1 isolated, event2 locked to it).
[ ] color by flight-pair combo   [ ] show only best point per combo (by match_score)
29245 point(s) shown, color grouping OFF
```
With both boxes ticked [shown]:
```
41 unique flight-pair combo(s) in current view (of 195 total) -- 195 point(s) shown
```
Leader tooltip [shown]:
```
flight1=1100069709, flight2=1100048665
lat=40.8764657, lon=-73.5249506
score_1=10.638, score_2=9.845
match_score=20.483
```
Top-N page header [shown]:
```
Top 7 flight-pair combos -- best point per combo (by match_score alone)
Same viewer as the top-N-points version, but ONE point per unique flight-pair combo -- whichever point is that
combo's own single best by match_score alone -- for the top-scoring combos, instead of several points that might
all belong to the same one combo's own internal densification-grid cloud.
[x] Show predicted curve overlays (all panels)
combo 1/7 -- flight1=1100069709, flight2=1100048665, (40.876466, -73.524951), combined score=20.48
event1 score=10.64        event2 score=9.84 (LOCKED)
```
Curve hover labels: "(5,708.957, 166.2793) this candida..." and "(5,725.569, 155.291) this candida..." (time s, frequency Hz) [shown].

Formulas:
- match_score = score_1 + score_2 [shown]
- best per pair = argmax over points in a (flight1, flight2) group of match_score [shown]
- rank = sort pairs by best match_score, descending [shown]

QGIS layer names visible (truncated in the panel) [shown]: dem_mosaic_1k..., all_flight_paths, prop_flight_paths, single ev, post offset pre si..., post silence + off..., 13552_cand..., 15113_candidate..., data error, test area, flightpaths (top n locs pe..., top n combo..., match_1:35..., 1:21:20_c..., 1:35:52_c..., 1:51:13_c..., match_1:21:...), va_flightpath... (three), event scores (va_locked_co..., va_phase1_eve... x3), 1:35:52_candid..., 1:21:20_candid..., old, old, th, google, carto, bing, norway.

## 6. Tools and software

- Interactive Plotly-style web plots with toolbar (camera, zoom, pan, box, lasso, +/-, autoscale, home) [shown]. The library is Plotly [inferred] M10-I08.
- Custom HTML viewer pages: scatter page and Top-N combos page, with checkboxes [shown].
- Python scoring script `1_2b_v7.py` and function or table `curve_match_scores_locked_spectrogram` [shown].
- QGIS with a Google satellite basemap (layers: google, carto, bing) [shown].

## 7. Problems and fixes

- Problem: in the raw cloud no single point stands out. Many points belong to the same flight pair's densification grid [stated] [00:21:14]. Fix: group by flight pair and keep only the best point per pair. The leader then separates clearly [stated] [00:21:24]-[00:21:32].
- Problem: a high event 1 score alone misleads. Combo 2 is close on event 1 (9.52 against 10.64) but badly off on event 2 (5.73) [stated] [00:22:01]-[00:22:11]. Fix: rank by the combined, locked two-event score [shown].
- Problem: the 100 m candidate grid is too coarse to pinpoint the spot [inferred] M10-I09. Fix: rerun at much finer resolution with only the winning flights [stated] [00:22:26].

## 8. Gaps

- Exact score definition behind score_1 and score_2 (e.g. sum of spectrogram brightness along the curve, normalisation, units). Covered in earlier milestones. Best guess: mean normalised brightness under the curve, summed or scaled. Confidence: low. [inferred] M10-I10
- Why some scores are negative (down to about -5.5). Best guess: brightness is z-scored against background, so a curve over below-average pixels scores negative. Confidence: medium. [inferred] M10-I11
- Fine-resolution grid spacing and extent for the heat maps. Best guess: 10 to 25 m spacing over about 1 to 2 km square around the leader. Confidence: low. [inferred] M10-I12
- Whether the fine rerun re-sweeps event 1 CPA offset and fundamental frequency per point or reuses the leader's values. Best guess: it re-sweeps, as in the main pipeline. Confidence: medium. [inferred] M10-I13
- How the combined heat map is formed. Best guess: per-point sum of the event 1 and locked event 2 scores, same as match_score. Confidence: medium. [inferred] M10-I14
- Heat map colour scale limits and interpolation. Best guess: linear min-to-max stretch, spectral ramp, no interpolation. Confidence: medium. [inferred] M10-I15
- Combo 3's event 2 score is cut off in every frame. Best guess: 7.14 by subtraction. Confidence: high. [inferred] M10-I16
- How Top N was chosen as 7. Best guess: a fixed CLI parameter. Confidence: low. [inferred] M10-I17
- The flight ID scheme (e.g. 1100069709). Best guess: an internal per-flight ID from the ADS-B source, not ICAO hex. Confidence: medium. [inferred] M10-I18
- Spectrogram settings for the overlay panels (FFT size, hop, dB scaling). Not shown here. Best guess: same as the S2 measurement settings. Confidence: medium. [inferred] M10-I19
