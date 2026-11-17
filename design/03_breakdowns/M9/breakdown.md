# M9 breakdown: Score modelled curves with locked two-event scoring

Range: 00:18:10 to 00:20:59. System: S6.

## 1. Goal and done criteria

Goal: give every candidate observer point one score per event, so points can be ranked.

- Each modelled Doppler curve (from S5) is laid on the measured spectrogram. Its score is the sum of the spectrogram brightness values the curve covers. [stated] [00:18:22]
- Event 1 is aligned by putting the modelled delayed CPA at the measured CPA timestamp, then a small sweep of time offset and f0 picks the best fit. [stated] [00:19:04]
- Event 2 gets an f0 sweep only. Its time offset from event 1 is fixed by flight geometry. [stated] [00:19:30]
- Survivors from the 200 m grid are resampled to 100 m and scored again. [stated] [00:20:27]

Done when:
- Every 100 m candidate point has an event 1 score and an event 2 score. [stated] [00:21:04] (from the slice padding, start of M10)
- A wrong event 2 time placement lowers that candidate's score rather than being corrected away. [stated] [00:19:40]
- The known-correct point scores near the top of its flight-pair cluster. [inferred] M9-I01

## 2. Procedure

1. **Plot the modelled curve on the spectrogram.** [00:18:14] The tool "Right vs Wrong Model -- Real Data (1:35:52, flightid 1100069709)" shows the green retarded emission-time curve over the real spectrogram. A dashed vertical line marks "delayed-CPA timestamp, from measurement". A green dot marks "delayed-CPA, from flight geometry". [shown]
   ![](frames/M9_001816.png)
2. **Score by brightness sum.** [00:18:22] Sum the spectrogram values under the curve. [stated] The gymnastics scorecard at [00:18:18] is a spoken joke only. The screen shows the same plot, with no scorecard graphic. [shown]
   ![](frames/M9_001820.png) ![](frames/M9_001825.png)
3. **Identify the two measured inputs that carry error.** [00:18:26] f0 came from a manual fit in the earlier Doppler Curve Fit tool. CPA time came from the same fit. [stated] The fit tool is shown with f0 = 130.00 Hz, v = 107.00 m/s, d = 3230.0 m, t0 = 1:51:15.40. [shown]
   ![](frames/M9_001833.png)
4. **Place the curve in time.** [00:18:42] The modelled curve has a delayed CPA from flight geometry. The time of filming is unknown, so its clock position on the spectrogram is unknown. The measured CPA timestamp in the audio is known. [stated] Anchor: put the modelled delayed CPA at the measured audio CPA timestamp. [stated] [00:19:04]
   ![](frames/M9_001843.png) ![](frames/M9_001905.png)
   The hover at [00:19:05] reads (5,750.452, 118.4994) on the RIGHT curve, near the dashed line at about 5752 s. [shown]
5. **Sweep event 1 offset and f0.** [00:19:12] Sweep "a few seconds" of time offset and a range of f0. [stated] On screen the Δt slider moves from -0.20 s to -3.05 s and back to -0.75 s. The f0 slider moves from 113.0 Hz to 112.5 Hz. [shown]
   ![](frames/M9_001915.png) ![](frames/M9_001920.png)
6. **Keep the best combination.** [00:19:21] Take the highest-scoring (Δt, f0) pair as the event 1 score. [stated] Frame at [00:19:25] shows Δt = -0.75 s, f0 = 112.5 Hz with the curve on the bright trace. [shown]
   ![](frames/M9_001925.png)
7. **Score event 2 with a locked offset.** [00:19:28] Event 2 still gets its own f0 sweep. [stated] Its time position relative to event 1 is set only by flight geometry and is not swept. [stated] The tool text says: "One shared dt shifts BOTH events' own modeled curves together". [shown]
   ![](frames/M9_001927.png) ![](frames/M9_001928.png)
8. **Show why locking matters.** [00:19:38] An animation shows two flight tracks (green and red) crossing near an observer dot, with a "gap" slider at 3.5 min and the two Doppler curves below. [shown] If event 1 is corrected and event 2 still lands at a bad offset, the candidate is genuinely wrong, and the score should reflect that. [stated] [00:19:40]
   ![](frames/M9_001938.png) ![](frames/M9_001945.png)
9. **Combined locked scoring.** [00:19:51] Correct measurement error on event 1. Event 2 falls where geometry puts it. [stated] At dt = -16.46 s both modelled curves sit left of their bright traces by the same amount. [shown]
   ![](frames/M9_001954.png) ![](frames/M9_001959.png)
10. **Recognise grid coarseness.** [00:20:10] The 200 m grid is too coarse for this scoring. The true point could be up to 141 m from the nearest grid point and score poorly. [stated] QGIS shows the 200 m red grid and a Measure tool reading 140.138 m. [shown]
    ![](frames/M9_002012.png) ![](frames/M9_002022.png)
11. **Resample survivors to 100 m.** [00:20:27] Expand each surviving 200 m point to 100 m resolution and score all of them. [stated] QGIS shows three green clusters of dense points along a river. [shown]
    ![](frames/M9_002032.png)
12. **Repeat per point at scale.** [00:20:36] The whole procedure runs per candidate point. [stated] The step-by-step Doppler page is shown again as the per-point unit of work. [shown] About 15,000 points become "probably like 30, 40,000" at 100 m. [stated] A mosaic of many small spectrogram tiles, each with a curve, illustrates the volume. [shown]
    ![](frames/M9_002036.png) ![](frames/M9_002041.png) ![](frames/M9_002044.png)

## 3. Components

| Item | Value | Tag |
|---|---|---|
| Event 1 label | event1 (1:35:52), flightid 1100069709 | [shown] |
| Event 2 label | event2 (1:51:13) | [shown] |
| Event 1 measured delayed-CPA timestamp | about 5752 s elapsed (1:35:52) | [shown] |
| Event 1 to event 2 label gap | 1:51:13 - 1:35:52 = 921 s | [inferred] M9-I02 |
| Example event 1 score | 8.89 | [shown] |
| Example event 2 score | 8.43 | [shown] |
| Event 1 f0 in demo | 113.0 Hz, then 112.5 Hz | [shown] |
| Event 1 Δt in demo | -0.20 s, -3.05 s, -0.75 s | [shown] |
| Locked shared dt in demo | 0.74 s and -16.46 s | [shown] |
| Event 2 fit (Doppler Curve Fit) | f0 130.00 Hz, v 107.00 m/s, d 3230.0 m, t0 1:51:15.40 | [shown] |
| Event 2 fit derived values | f_pre 188.94 Hz, f_post 99.09 Hz, max RoC 1.343 Hz/s | [shown] |
| Fit tool window | 01:50:30 to 01:52:15 | [shown] |
| Fit tool colour scale | 0 to -80 dB | [shown] |
| Event 1 plot axes | 5690 to 5875 s elapsed; about 70 to 250 Hz | [shown] |
| Event 2 plot axes | about 6630 to 6735 s elapsed; about 90 to 190 Hz | [shown] |
| Wide overview axes | about 5660 to 6760 s; 40 to 220 Hz | [shown] |
| Hover z values (brightness) | e.g. -38.7, -39.7, -24.4 (dB) | [shown] |
| Time offset sweep span | "a few seconds" | [stated] |
| Coarse grid | 200 m | [stated] |
| Max error at 200 m | 141 m | [stated] |
| Measured example distance | 140.138 m (ellipsoidal) | [shown] |
| Fine grid | 100 m | [stated] |
| Candidates before resample | about 15,000 | [stated] |
| Candidates after resample | about 30,000 to 40,000 | [stated] |
| Speed of sound (Doppler page) | 343 m/s | [shown] |
| QGIS measure coordinates | -10921671.153, 4300359.054 and -10921792.918, 4300482.510 | [shown] |
| QGIS layers | dem_mosaic, all_flight_pat.., prop_flight_.., single ev, post offset p.., post silence (several), 13552_ca.., 15113_candic.., post silence +, data error, test area, flightpaths, event scores (va_locked, va_phase.. x3), 1:35:52_cand.., 1:21:20_cand.., old, th, google, carto, bing, norway | [shown] |

## 4. Systems touched

### S6 Spectrogram scoring and ranking
- How it works: lays each modelled curve from S5 on the spectrogram and sums the brightness under it. [stated] For event 1 it sweeps Δt and f0 and keeps the max. [stated] For event 2 it sweeps f0 only, with the time position locked to event 1 plus the geometry-derived offset. [stated]
- Inputs: the measured spectrogram (S2), the measured event 1 CPA timestamp and f0 values (S2), modelled curves for both events per candidate (S5), and delayed-CPA times from flight geometry (S3). [stated]
- Outputs: per candidate, an event 1 score and an event 2 score. [shown] [00:19:27] These feed ranking by flight pair at the start of M10. [stated]
- Connections: candidate points come from S4 filters. [stated] Survivors are densified from 200 m to 100 m, which needs S3 and S5 to rerun for the new points. [inferred] M9-I03 Scored points go to S7 for map review in QGIS. [shown] (event scores layer group in QGIS)

### Upstream dependencies used here
- S3 supplies the delayed-CPA time "from flight geometry" and the inter-event offset. [shown] [00:18:16]
- S5 supplies the retarded emission-time curve, labelled "RIGHT (retarded emission-time)". [shown]

## 5. Code, configs, formulas, and on-screen text

On-screen text, Right vs Wrong tool [00:18:16] [shown]:

> Same real spectrogram, same flight, same candidate location. Green is the correct model (solves for when the sound actually left the aircraft); red is the naive model (uses the aircraft's position at the moment the sound is heard, as if sound traveled instantly). Sliders move whichever curve(s) are currently toggled on, together, at the same dt/f0.

Controls: "Right (correct)" checkbox, "Wrong (naive)" checkbox, "Δt = -0.20 s" slider, "f0 = 113.0 Hz" slider. Annotations: "delayed-CPA timestamp, from measurement", "delayed-CPA, from flight geometry". Legend: "RIGHT (retarded emission-time)". [shown]

On-screen text, locked scoring tool [00:19:27] [shown]:

> One shared dt shifts BOTH events' own modeled curves together -- their relative separation is already fixed by the flight's real geometry; only this shared clock-anchor offset is free to explore here. Top: wide, low-resolution overview spanning event1's own start to event2's own end. Below: both events at full resolution, zoomed to their own real scored window.

Panels: "Wide overview", "event1 (1:35:52), score=8.89", "event2 (1:51:13), score=8.43". [shown]

Doppler step page [00:20:36] [shown]:

- t_r = 25.00 s; t_r = t_e + r(t_e)/c; t_e = 16.910 s
- (x, y, z) = (2367, 1264, 1020) m; v = (140.0, 16.8, 0.0) m/s; r(t_e) = 2775 m
- radial component (3D, at t_e): v_r = 121.16 m/s
- f = f_0 · c / (c + v_r) = 130 · 343 / (343 + 121.16) = 96.07 Hz

Scoring formulas (reconstructed from speech):

- Curve score: S(Δt, f0) = Σ_k B(t_k + Δt, f_model(t_k; f0)), summed over curve time samples k, where B is spectrogram brightness. [inferred] M9-I04
- Event 1: S1 = max over Δt in [-a, a], f0 in [f0_meas - b, f0_meas + b] of S_1(Δt, f0). [inferred] M9-I05
- Event 2: S2 = max over f0' of S_2(Δt*, f0'), where Δt* is the event 1 best offset and the event 2 curve sits at its geometry-predicted time relative to event 1. [inferred] M9-I06
- 141 m = 100 · √2 m, half the diagonal of a 200 m cell. [inferred] M9-I07

## 6. Tools and software

- Custom interactive web tools with Plotly-style toolbars (camera, zoom, pan, box, lasso icons): "Right vs Wrong Model -- Real Data", locked dt overview, "Doppler Curve Fit", "Building the Doppler Curve, Step by Step". [shown]
- Plotly as the plotting library. [inferred] M9-I08
- Custom 2D animation of two flight tracks with "animation 10 s" and "gap 3.5 min" sliders. [shown]
- QGIS with Google, Carto, and Bing basemaps, a DEM mosaic layer, and the Measure Line tool (Ellipsoidal). [shown]
- Python for the scoring pipeline. [inferred] M9-I09

## 7. Problems and fixes

- Problem: f0 and CPA time are hand measurements and carry error. [stated] Fix: sweep a few seconds of time offset and a range of f0 for event 1, keep the best. [stated]
- Problem: correcting event 2's timing separately would hide a wrong candidate. [stated] Fix: lock event 2's offset to the geometry-derived value; sweep only its f0. [stated]
- Problem: the 200 m grid is too coarse. The true point can be up to 141 m off and score badly. [stated] Fix: resample survivors to 100 m. [stated]
- Problem: scoring is expensive at 30,000 to 40,000 points. [stated] Fix: rely on the earlier S4 filters to cut the candidate set; the full US for a full day is infeasible. [stated]

## 8. Gaps

- Exact Δt sweep range and step. Best guess: ±3 s in 0.05 s steps (slider showed -3.05 s and 0.05 s resolution). Confidence: medium. [inferred] M9-I10
- Exact f0 sweep range and step. Best guess: ±2 Hz in 0.5 Hz steps (slider showed 113.0 and 112.5). Confidence: low. [inferred] M9-I11
- How brightness is sampled along the curve: nearest bin, interpolation, or a band of width w around the curve. Best guess: nearest STFT bin per time column, in dB. Confidence: low. [inferred] M9-I12
- Score normalisation. Scores of 8.89 and 8.43 are small for a raw dB sum, so values are likely normalised (e.g. mean z-score of bins under the curve). Confidence: low. [inferred] M9-I13
- Spectrogram parameters (window length, hop, frequency band) used for scoring. The event 2 panel shows coarse pixels, about 1 s by 2 Hz. Best guess: FFT window about 1 s, 50% overlap, band 50 to 250 Hz. Confidence: low. [inferred] M9-I14
- Whether event 2 is allowed any small time slack. Speech says "entirely locked". Best guess: zero slack. Confidence: high. [inferred] M9-I15
- How the 100 m resample is built. Four sub-points per 200 m cell gives 60,000, not 30,000 to 40,000. Best guess: a fresh 100 m grid over the union of survivor cells, deduplicated, with shared points counted once. Confidence: medium. [inferred] M9-I16
- How event 1 and event 2 scores combine into one rank. Shown later as a 2D scatter with the best point per flight pair. Best guess: sum or product of the two, max per flight pair. Confidence: medium. [inferred] M9-I17
- Whether the 8.89 and 8.43 labels update with the dt slider. They stay fixed from dt = 0.74 s to -16.46 s, so they are likely the precomputed best scores. Confidence: medium. [inferred] M9-I18
- Coordinate reference system. QGIS measure values match EPSG:3857 Web Mercator metres in the central US. Confidence: medium. [inferred] M9-I19
- Compute budget and parallelism for 30,000 to 40,000 points times two events times the sweep grid. Best guess: vectorised NumPy over a precomputed spectrogram, run on one machine for hours. Confidence: low. [inferred] M9-I20
