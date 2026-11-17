# M11 breakdown: Confirm with a one-minute known-time clip and Street View

Range: 00:22:41 to 00:26:08.

## 1. Goal and done criteria

Goal: show that one faint Doppler event plus a known recording time locates the camera US-wide, then confirm the location on the ground.

Done when:
- A single-event search over the continental US, restricted to flight segments at the known time, ranks the true location first. [stated] [00:23:44]
- That top point agrees with the two-event search result, about 40.87, -73.5. [stated] [00:23:58]
- The heat-map centre coordinate, opened in Google Maps Street View, shows the tree line from the source footage and the camera pole. [stated] [00:25:54] [00:26:04]

## 2. Procedure

1. Pick the faint event 1 Doppler curve, the one that is inaudible. [stated] [00:22:52] It shows in the spectrogram as a thin falling streak from about 600 Hz to about 450 Hz near 940 to 970 s on that view's axis. [shown] [00:23:06]
   ![faint curve](frames/M11_002306.png)
   The prior two-event heat map is still on screen at the start. [shown] [00:22:53] ![two-event heat map](frames/M11_002253.png)
2. Assume a known recording time of 8:37 PM UTC and a one-minute clip. [stated] [00:23:02] No time text appears on screen. [shown] [00:23:06]
3. Measure the curve on the spectrogram as before to get velocity bounds for the flight. [stated] [00:23:09]
4. Filter flight segments to the velocity bounds and to the known time only. Search the whole continental US. [stated] [00:23:12] [00:24:22] The QGIS view shows small clusters of candidate points scattered across the US, in layers named `1:21:16_single_...`. [shown] [00:23:16]
   ![segments at that time](frames/M11_002316.png)
5. Score every candidate point. With one event there is no event 1 vs event 2 scatter plot, only a histogram; right is better. [stated] [00:23:20] ![all scores](frames/M11_002322.png)
6. Keep the best point per flight and plot that histogram (253 flights). [shown] [00:23:26] ![best per flight](frames/M11_002326.png)
7. Because the curve is too faint for brightness scoring, trace it by hand as a line and score each candidate's modelled curve by its closeness to that line. [stated] [00:23:34] The overlay legend reads "traced composite line (LINE_POINTS)". [shown] [00:23:31]
   ![top 8 overlays](frames/M11_002330.png) ![overlays detail](frames/M11_002331.png)
   Toggling off the candidate curve shows the cyan traced line on the faint streak. [shown] [00:23:38] ![traced line](frames/M11_002338.png) ![traced line only](frames/M11_002347.png)
   Hover on the raw spectrogram reads x 4,908.248, y 495.2637, z -40.44075. [shown] [00:23:45] ![hover](frames/M11_002345.png)
8. Inspect the ranking. Top point fits; second place is close but visibly off; beyond that it degrades. [stated] [00:23:44] ![second place](frames/M11_002350.png)
9. Compare with the two-event result. The top combo there is at (40.876466, -73.524951). [shown] [00:23:58] The creator calls it the same location, first by a significant margin, from different flights. [stated] [00:24:01]
   ![two-event combos](frames/M11_002354.png) ![combo 1 zoom](frames/M11_002358.png) ![coordinate highlighted](frames/M11_002401.png)
10. State the tradeoff: temporal constraint, spatial constraint, and number of flights in the recording form a triangle; one strong side is enough. [shown] [00:24:14] ![triangle](frames/M11_002414.png)
    Example 1: full US, 1 day, 2 flights (~30 min). Example 2: full US, 1 hour, 1 flight (~60 s). [shown] [00:24:58] ![table](frames/M11_002452.png)
11. Illustrate a city-sized search area (San Francisco Bay Area box) against US land area; a city is about 0.01% of land area, which allows much looser time bounds. [stated] [00:24:46] ![city box](frames/M11_002448.png)
12. In QGIS, zoom to the centre of the heat map. It sits in the water, so take a point on the bank. [stated] [00:25:20] ![heat map](frames/M11_002521.png) ![centre](frames/M11_002524.png)
    A QGIS Measure window shows a 28.122 m segment, ellipsoidal. [shown] [00:25:04] ![measure](frames/M11_002504.png)
13. Right-click, Copy Coordinate, EPSG:4326: 40.8767282N, -73.5264340E. [shown] [00:25:27] ![copy coordinate](frames/M11_002527.png)
14. Paste into Google, open Google Maps: 40°52'36.2"N 73°31'35.2"W, 40.876728, -73.526434, plus code VFGF+MCW Oyster Bay, New York. [shown] [00:25:28] [00:25:30] ![google search](frames/M11_002528.png) ![google maps](frames/M11_002530.png)
15. Study the source footage tree line: a V-shaped tree, then a point, then a big rounded part. [stated] [00:25:37] ![source tree line](frames/M11_002535.png) ![target features](frames/M11_002538.png)
16. Enter Street View at 19 Bayview Ave, Oyster Bay, New York (imagery Sep 2025). [shown] [00:25:42] ![street view street](frames/M11_002542.png)
17. Pan across the water. Reject views without the V shape or with a V going the wrong way. [stated] [00:25:42] ![candidate view](frames/M11_002549.png)
18. Find the V shape with the point and rounded part, behind a wooden utility pole. [stated] [00:25:54] ![match](frames/M11_002554.png) ![match 2](frames/M11_002559.png)
19. Compare source and Street View side by side. [shown] [00:25:59] ![side by side](frames/M11_002600.png)
20. Tilt up the pole. The security camera that took the footage is on top. [stated] [00:26:04] The pole carries a bird nest and grey boxes near the top. [shown] [00:26:05] ![pole camera](frames/M11_002605.png)

## 3. Components

- Input audio: one minute of the recording around the faint event 1. [stated] [00:22:57]
- Known time: 8:37 PM UTC. [stated] [00:23:02]
- Event label in the viewer: "Single-Event (1:21:16)". [shown] [00:23:31] 1:21:16 equals 4,876 s, inside the 4,850 to 4,910 s plotted window. [inferred] M11-I01
- Faint curve on the scoring plots: about 510 Hz falling to about 310 Hz between about 4,852 and 4,910 s elapsed recording time. [shown] [00:23:31]
- Spectrogram app view: 860 s to 1,100 s window, playhead 15:55.494 / 60:00.000, cursor 955.494 s, frequency axis 5 to 800 Hz, channel CH 2. [shown] [00:23:06]
- All-points histogram: "All Scored Points -- 1:21:16", n = 380,127, min = -137.78, max = -1.74, mean = -51.44, axis match_score, count up to about 5,500. [shown] [00:23:22]
- Best-per-flight histogram: "Best Score Per Flight -- 1:21:16 (253 flight(s))", n = 253, min = -63.48, max = -1.74, mean = -28.53. [shown] [00:23:26]
- Top flights, single event: [shown] [00:23:31]
  - top1 flight 1100029523, (40.877922, -73.531941), score -1.74, dt +0.45 s.
  - top2 flight 1100057337, (41.044589, -77.739976), score -3.68, dt +0.15 s.
  - top3 flight 1100026508, (43.692244, -79.325785), score -4.66, dt +0.50 s.
  - top4 flight 1100046734, (32.072902, -102.151974), score -4.70, dt +0.50 s.
  - f0 values are cut off at the panel edge. [shown] [00:23:31]
- Two-event top combo: flight1 1100069709, flight2 1100048665, (40.876466, -73.524951), combined score 20.48, event1 score 10.64, event2 score 9.84 (LOCKED). [shown] [00:23:58] Combo 2/7: (45.699498, -73.643756), 15.25. Combo 3/7: (36.454080, -94.456016), 15.04. [shown] [00:23:54]
- Two-event spectrogram bands: event 1 about 80 to 180 Hz over 5,700 to 5,880 s; event 2 about 100 to 180 Hz over 6,640 to 6,740 s. [shown] [00:23:54]
- Single-event top and two-event top differ by about 0.0015° latitude and 0.007° longitude, about 600 m. [inferred] M11-I02
- Google Maps point is about 130 m from the two-event top and about 480 m from the single-event top. [inferred] M11-I03
- Score sign: score is negative and the best is closest to zero, so it is likely a negative distance or error to the traced line. [inferred] M11-I04
- Spatial fraction: a city is about 0.01% of US land area. [stated] [00:24:48]
- Accuracy: within a couple hundred feet from one minute of inaudible audio. [stated] [00:25:01]
- Final coordinate: 40.8767282, -73.5264340 (EPSG:4326); map CRS EPSG:3857 -8184925.20E, 4994176.08N. [shown] [00:25:27]
- Measure tool points: -8184915.347, 4994190.242 and -8184949.848, 4994204.042; total 28.122 m. [shown] [00:25:04]
- Location: 19 Bayview Ave, Oyster Bay, New York; Street View Sep 2025. [shown] [00:25:42]

## 4. Systems touched

- **S1 ADS-B ingest and aircraft filtering.** Takes the day's flight paths. Here it cuts segments to the measured velocity range and to the known time window. [stated] [00:23:09] Output: a sparse set of flight segments across the US, shown as point clusters. [shown] [00:23:16] Feeds S5. The time window width is not stated; the table says "1 hour". [shown] [00:24:58]
- **S2 Spectrogram measurement.** Gives velocity bounds from the event 1 curve. [stated] [00:23:09] Also produces the hand-traced line ("traced composite line (LINE_POINTS)") that S6 scores against. [shown] [00:23:31] Feeds S1 filters and S6.
- **S5 Doppler curve forward model.** For each candidate point and flight, produces the predicted curve, drawn red as "this candidate (real geometry)". [shown] [00:23:31] The page text says the red curve is the flight's own best-scoring candidate's geometry-derived predicted curve. [shown] [00:23:31] Feeds S6.
- **S6 Spectrogram scoring and ranking.** Scores by distance to the traced line instead of brightness. [stated] [00:23:39] Outputs a score histogram, a best-per-flight histogram, and a top-8 flight panel with dt offsets. [shown] [00:23:22] [00:23:26] [00:23:31] The per-point dt (+0.15 to +0.50 s) suggests the CPA time-offset sweep from the two-event method is kept. [inferred] M11-I05 Feeds S7.
- **S7 Map review and ground-truth confirmation.** QGIS shows the heat map from the locked two-event layer (`va_locked_con...` checked under "event scores"). [shown] [00:25:20] Copy Coordinate goes to Google Maps and Street View, where the tree line is matched by eye. [shown] [00:25:27] [stated] [00:25:37]

## 5. Code, configs, formulas, and on-screen text

Viewer headings and captions, verbatim where legible: [shown] [00:23:22] [00:23:26] [00:23:31] [00:23:54]

```
All Scored Points -- 1:21:16
n = 380,127 | min = -137.78 | max = -1.74 | mean = -51.44
match_score distribution

Best Score Per Flight -- 1:21:16 (253 flight(s))
n = 253 | min = -63.48 | max = -1.74 | mean = -28.53

Single-Event (1:21:16): Top 8 Flights by Own Best Score
Magma heatmap = the REAL recorded spectrogram (brighter = louder). Red solid = this specific flight's own best-scoring candidate's real, geometry-derived predicted curve -- this IS the score, not a comparison against a separate reference. One panel per flight, its own single best-scoring point only.
Show predicted curve overlays (all panels)
top1_flight_1100029523
...ght_1100029523 -- (40.877922, -73.531941) flightid=1100029523 score=-1.74 | dt=+0.45s f0=
legend: this candidate (real geometry) / traced composite line (LINE_POINTS)

Top 7 flight-pair combos -- best point per combo (by match_score alone)
Same viewer as the top-N-points version, but ONE point per unique flight-pair combo -- whichever point is that combo's own single best by match_score alone -- for the top-scoring combos, instead of several points that might all belong to the same one combo's own internal densification-grid cloud.
combo 1/7 -- flight1=1100069709, flight2=1100048665, (40.876466, -73.524951), combined score=20.48
event1 score=10.64    event2 score=9.84 (LOCKED)
```

Slides: [shown] [00:24:14] [00:24:58]

```
Temporal constraint (when the video was filmed)
Number of flights in recording
Spatial constraint (where the video was filmed)

            Example 1      Example 2
Spatial     Full US        Full US
Temporal    1 day          1 hour
# of flights 2 (~30min)    1 (~60sec)
```

QGIS layer names visible: dem_mosaic_1km, all_flight_paths, prop_flight_paths, single ev, post offset pre sil..., post silence + offs..., 13552_candid..., 15113_candidate_..., data error, test area, flightpaths, event scores, va_locked_con..., va_phase1_eve..., 1:35:52_candidat..., 1:21:20_candidate..., google, carto, bing, norway. [shown] [00:25:24]

Distance score, best guess: score = -mean over traced points of |f_model(t) - f_traced(t)| in Hz. [inferred] M11-I06

## 6. Tools and software

- Custom spectrogram app with a playhead, time ruler, and CH 2 channel selector; a "Claude Code" label sits in its status bar. [shown] [00:23:06]
- Browser-based Plotly-style viewer for histograms and spectrogram overlays (camera, zoom, pan toolbar; hover x/y/z). [shown] [00:23:45] Plotly as the library is a guess from the toolbar. [inferred] M11-I07
- QGIS with Google satellite basemap, Measure tool, and Copy Coordinate. [shown] [00:25:04] [00:25:27]
- Google Search, Google Maps, Google Street View. [shown] [00:25:28] [00:25:42]

## 7. Problems and fixes

- The event 1 curve is too faint for brightness scoring. Fix: trace it by hand as a line and score by distance to the line. [stated] [00:23:34]
- One event gives no two-axis scatter plot. Fix: use a histogram of scores. [stated] [00:23:20]
- The heat-map centre lies in the water. Fix: take a coordinate on the nearby bank. [stated] [00:25:23]
- The source tree line is heavily pixelated. Fix: match its shape (V, point, rounded part) and direction ("up and to the right") rather than detail. [stated] [00:25:31] [00:25:49]

## 8. Gaps

- Elapsed-time mapping: the panel axis (4,850 to 4,910 s) and the spectrogram app axis (curve near 955 s of a 60:00 file) differ. Best guess: the app shows a one-hour chunk and the viewer uses time from the full recording start. Confidence low. [inferred] M11-I08
- Time window width around 8:37 PM UTC: the slide says "1 hour". Best guess: a ±30 min window on segment timestamps, delay-corrected. Confidence medium. [inferred] M11-I09
- Tracing method: how the line was drawn (tool, number of points) is not shown. Best guess: manual clicks on the spectrogram exported as time-frequency pairs, interpolated linearly. Confidence medium. [inferred] M11-I10
- Distance metric: the exact formula is not shown. Best guess as in section 5, mean absolute frequency error in Hz, negated. Confidence medium. [inferred] M11-I11
- f0 sweep range for the single event: values are cut off on screen. Best guess: same f0 and dt sweep as the two-event event 1 search. Confidence medium. [inferred] M11-I12
- Candidate grid for the single event: spacing and extent not shown; 380,127 points across 253 flights is about 1,500 per flight. Best guess: points at the measured slant distance on a 200 m grid. Confidence medium. [inferred] M11-I13
- Velocity bounds for event 1: not given in this segment. Best guess: reuse the earlier event 1 measurement from the two-event search. Confidence high. [inferred] M11-I14
- Purpose of the 28.122 m measurement: not explained. Best guess: grid spacing check or point-to-shore distance. Confidence low. [inferred] M11-I15
- Heat-map source: the QGIS heat map comes from the locked two-event layer, not the single-event run. Best guess: the ground-truth step uses the two-event result. Confidence medium. [inferred] M11-I16
- Street View heading and pitch for the match: not shown. Best guess: look roughly north-east across Oyster Bay harbor from Bayview Ave. Confidence low. [inferred] M11-I17
