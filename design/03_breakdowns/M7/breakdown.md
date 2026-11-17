# M7 breakdown: Forward-model the Doppler curve from real flight geometry

Range: 00:13:35 to 00:16:45. System: S5.

## 1. Goal and done criteria

Goal: for any candidate observer point and any flight, compute the frequency-over-time curve that observer would hear, using the flight's real ADS-B track. The curve is then compared with the spectrogram (S6). [stated]

The constant-velocity fit from earlier milestones does not match the measured curves exactly, because planes change heading, speed, and altitude. [stated] Several geometries can produce the same curve variation, so the spectrogram cannot be inverted to a flight geometry. [stated] The method runs the other way: model the exact curve for each candidate point on each flight path, then find the one that matches. [stated]

Done when:
- Given a flight track and an observer point, the model outputs frequency per time step. [stated]
- The worked example reproduces: t = 0 s (07:12:30), v_r = 0.00 m/s, f = 130.00 Hz; t = 5 s (07:12:35), v_r = 62.73 m/s, f = 109.90 Hz. [shown]
- Curves differ by observer position for a non-linear track (red, blue, grey example curves). [shown]

## 2. Procedure

1. Revisit the constant-velocity fit. Under linear constant velocity only speed and slant distance set the curve shape. [stated] [00:13:36]. The event-1 fit does not follow the measured trace exactly. [shown] [00:13:46] ![fit](frames/M7_001346.png) ![fit zoom](frames/M7_001402.png)
   - The 00:13:36 frame shows the tail of the previous QGIS map, not the constant-velocity explanation. It is kept only to cover the visual moment. [shown] ![qgis](frames/M7_001336.png)
2. Name the cause: planes change heading, speed up, slow down. That information is in the curve. [stated] [00:13:53] The creator shows a Google Earth flight-sim clip as illustration ("i dont have footage for this part"). [shown] ![flightsim](frames/M7_001356.png)
3. Recap the constraint layers so far. Layer 1: was there a flight at this offset (920 sec). Layer 2: a flight of a given speed at a given distance at this offset. Layer 3 (new): how exactly the flight passed over. [stated] [00:14:05] to [00:14:23] ![920 sec](frames/M7_001410.png) ![ranges](frames/M7_001416.png)
4. Rule out inversion. Speed change, heading change, and altitude change, alone or combined, can all cause the same variation. [shown] [00:14:23] to [00:14:34] ![spec to map](frames/M7_001423.png) ![spec to map](frames/M7_001429.png) ![bullets](frames/M7_001430.png)
5. Forward-model instead. Take the actual flight geometry and compute the curve it would produce. [stated] [00:14:34] to [00:14:46] ![map to spec](frames/M7_001440.png)
6. Repeat for each candidate point on each flight path. Different observer points along one bent track yield different curves (red, blue, grey). [shown] [00:14:46] ![three candidates](frames/M7_001447.png) ![curves vs spectrogram](frames/M7_001450.png)
7. Pick the curve that matches the spectrogram. [stated] [00:14:50] (Scoring is S6, not this milestone.) The section header asks how to model a curve. [shown] [00:14:53] ![question](frames/M7_001453.png)
8. Compute radial velocity: the component of plane velocity directly toward or away from the observer. [stated] [00:14:57] to [00:15:09]
   - Observer dead ahead: plane 90 m/s, radial 90 m/s, angle 0.0 deg. [shown] ![ahead](frames/M7_001515.png)
   - Near ahead: 89.3 m/s radial at 7.4 deg. [shown] [00:15:09] ![near ahead](frames/M7_001509.png)
   - Observer to the side: radial 4.6 m/s at 87.1 deg; at 90 deg radial is about zero and there is no Doppler shift. [shown] [stated] [00:15:15] ![side](frames/M7_001519.png)
   - In between, the red line is the radial component: 34.2 m/s at 67.7 deg, 21.6 m/s at 76.1 deg. [shown] [00:15:26] ![between](frames/M7_001526.png) ![between](frames/M7_001530.png)
9. Show that curve shape depends on flight geometry. A straight track gives a smooth sigmoid; a track with a sharp bend gives a steeper drop and a bump after CPA. [shown] [00:15:30] ![straight](frames/M7_001531.png) ![bent](frames/M7_001535.png)
10. Build the curve point by point. Start at t = 0 (CPA). In the example CPA is 07:12:30 from the flight data. This time is illustrative; the recording time is not known. [stated] [00:15:40] to [00:15:51] ![t0](frames/M7_001547.png)
11. Look up the flight data at 07:12:30, get the radial velocity (0 at CPA), put it in the Doppler equation. [stated] [00:15:51] to [00:16:07] ![eq](frames/M7_001607.png) ![eq terms](frames/M7_001609.png)
12. Equation terms: c is the speed of sound constant, v_r is the radial component, f0 is the fundamental frequency. f0 comes from the measured curve fit (the slider you slide up and down). [stated] [00:16:07] to [00:16:21] ![f0 from fit](frames/M7_001619.png)
13. Output 130 Hz at 07:12:30 and plot it. [shown] [00:16:21] ![130 Hz](frames/M7_001625.png)
14. Repeat for 07:12:35: radial velocity 62.73 m/s gives 109.90 Hz. [shown] [00:16:26] to [00:16:39] ![109.9 Hz](frames/M7_001634.png)
15. Repeat for all time steps to get the observer's curve. [stated] [00:16:39] to [00:16:43] ![step 9](frames/M7_001642.png) ![step 11](frames/M7_001645.png)
16. Warning: this position-time version is wrong and would make the search fail. The next milestone replaces it with emission-time (retarded-time) velocity. [stated] [00:16:43] The demo has a "Delayed" toggle for this. [shown] ![step 11](frames/M7_001645.png)

## 3. Components

- Constraint ranges from spectrogram, event 1: 130-154 m/s, 4300-7800 m away at CPA. Event 2: 88-110 m/s, 1390-4690 m away at CPA. Offset 920 sec. [shown] ![ranges](frames/M7_001416.png)
- Event-1 fit panel "Doppler Curve Fit -- 01:50:30 to 01:52:15". Sliders: f0 (fundamental freq), v (plane speed), d (slant distance), t0 (CPA time). Read-outs: f_pre (approach), f_post (recede), max RoC. [shown]
  - Snapshot A: f0 131.50 Hz, v 117.00 m/s, d 4295.0 m, t0 1:51:15.90; f_pre 199.58 Hz, f_post 98.05 Hz, max RoC 1.222 Hz/s. [shown] ![A](frames/M7_001346.png)
  - Snapshot B: f0 133.50 Hz, v 112.00 m/s, d 3460.0 m, t0 1:51:12.90; f_pre 198.23 Hz, f_post 100.64 Hz, max RoC 1.411 Hz/s. [shown] ![B](frames/M7_001402.png)
  - Snapshot C: f0 130.00 Hz, v 107.00 m/s, d 3230.0 m, t0 1:51:15.40; f_pre 188.94 Hz, f_post 99.09 Hz, max RoC 1.343 Hz/s. [shown] ![C](frames/M7_001619.png)
  - Spectrogram axes: frequency about 95-215 Hz, elapsed time HH:MM:SS, colour scale dB from -80 to 0. [shown]
- Speed of sound c = 343 m/s. [shown] ![eq](frames/M7_001634.png)
- Worked-example demo inputs: aircraft speed 140 m/s, CPA distance 980 m, altitude 1020 m, emitted frequency f0 130 Hz. [shown]
- Worked-example time steps, 11 steps, 5 s apart, 07:12:05 to 07:12:50 axis. [shown]

| Step | t (s) | Clock | Aircraft (x, y, z) m | v vector m/s | r(t) m | v_r m/s | f Hz |
|---|---|---|---|---|---|---|---|
| 6 | 0.00 | 07:12:30 | (0, 980, 1020) | (140.0, 16.8, 0.0) | 1419 | 0.00 | 130.00 |
| 7 | 5.00 | 07:12:35 | (700, 1064, 1020) | (140.0, 16.8, 0.0) | 1585 | 62.73 | 109.90 |
| 9 | 15.00 | n/a | (2100, 1232, 1020) | (140.0, 16.8, 0.0) | 2547 | 117.08 | 96.92 |
| 11 | 25.00 | n/a | (3500, 1400, 1020) | (140.0, 16.8, 0.0) | 3800 | 130.80 | 94.11 |

All values [shown] in frames/M7_001625.png, frames/M7_001634.png, frames/M7_001642.png, frames/M7_001645.png. Tooltip speed 141.0 m/s is the magnitude of (140.0, 16.8). [shown]
- Pre-CPA points on the demo plot reach about 210 Hz at 07:12:05. [shown] ![step 11](frames/M7_001645.png)
- Radial-velocity demo: plane speed 90 m/s, plane heading 47 deg. [shown]
- Curve-shape demo: aircraft speed 90 m/s (175 kt), source frequency f0 500 Hz, display window +/-15 s around CPA, altitude 600 ft at path start and end, propagation delay (retarded time) on. Y axis 385-689 Hz. [shown] ![straight](frames/M7_001531.png)

## 4. Systems touched

**S5 Doppler curve forward model.**
- How it works: for each time step t, look up the aircraft position and velocity from the interpolated ADS-B track, form the 3D vector from aircraft to observer, project velocity on it to get v_r, then compute f = f0 c/(c + v_r). [shown] [stated]
- In this milestone t is the reception time and the lookup uses the aircraft state at the same t. [shown] This is flagged as wrong; M8 swaps in the emission-time state. [stated]
- Inputs: flight track (position, velocity, altitude) per time step [stated]; observer position [stated]; f0 from the S2 fit [stated]; c = 343 m/s [shown]; CPA time to anchor t = 0 [stated].
- Outputs: a list of (time, frequency) pairs, the modelled curve. [shown]
- Connections: takes candidate points from S4 [stated]; takes f0 and CPA anchor from S2 [stated]; will take emission time / propagation delay from S3 (M8) [stated]; feeds curves to S6 scoring [stated].
- The track is interpolated ADS-B. [stated] The interpolation method is not shown; see Gaps.

## 5. Code, configs, formulas, and on-screen text

Radial-velocity demo footer, verbatim [shown]:
`radial velocity = full velocity · cos(angle off nose) · this is the ONLY component of velocity that produces a Doppler shift`

Radial-velocity demo panels, verbatim [shown]:
- `plane velocity` / `90.0 m/s` / `fixed by the speed slider, always along the heading`
- `radial velocity` / `approaching -- shifts frequency UP`
- `angle off the nose (to observer)` / `0° = observer dead ahead, 90° = directly off to the side, 180° = dead behind`
- Controls: `plane heading 47°`, `plane speed 90 m/s`, `reset observer position`, `drag the observer`

Step-by-step demo, verbatim [shown]:
- Title `Building the Doppler Curve, Step by Step`, mode badge `position`, buttons `Position`, `Delayed`, `Reset`, `Prev`, `Play`, `Next`, `step 7 / 11`.
- Labels: `reception time (when you hear it)`, `aircraft position (at t)`, `full velocity (at t)`, `distance to observer (at t)`, `radial component (3D, at t)`, `Doppler equation`.
- Legend: `full velocity`, `radial component (used)`. Plot title `Frequency heard by observer`, checkboxes `Position`, `Delayed`.

Doppler equation [shown]:

$$f = f_0 \cdot \frac{c}{c + v_r}$$

- Example: f = 130 · 343 / (343 + 62.73) = 109.90 Hz. [shown]
- Example: f = 130 · 343 / (343 + 130.80) = 94.11 Hz. [shown]
- Radial velocity: v_r = |v| cos(theta), theta = angle off the nose. [shown]
- 3D form: v_r = v · (P_aircraft - P_observer) / |P_aircraft - P_observer|, positive when receding. [inferred] M7-I02

Curve-shape demo, verbatim [shown]: `flightpath (color = altitude)`, `observer`, `drag points to reshape`, `frequency heard by observer, over time`, `±15s around CPA, fixed`, `propagation delay (retarded time)`, `reset to default geometry`. Bottom stats row, partly cut off: `CPA distance`, `altitude at CPA`, `frequency at CPA`, `total shift (approach → recede)`, `flight duration (full path)`, `max transition steepness`.

## 6. Tools and software

- Custom web demos (dark UI): radial-velocity explorer, curve-shape explorer, step-by-step curve builder. Plotly-style chart toolbar visible on the step-by-step plot. [shown]
- Custom "Doppler Curve Fit" web tool with sliders and a spectrogram (Plotly-style toolbar, snapshot log "MIN/MAX auto-calculated, BEST = midpoint"). [shown]
- Google Earth flight sim for illustration only. [shown]
- QGIS map tail at 00:13:36. [shown]
- Implementation language for S5 is not shown; see Gaps.

## 7. Problems and fixes

- Problem: measured curves do not fit the ideal constant-velocity curve. Fix: forward-model from the real ADS-B geometry. [stated]
- Problem: the spectrogram cannot be inverted to a geometry because speed, heading, and altitude changes are confounded. Fix: test each candidate point forward and match. [stated]
- Problem: still about 15,000 points pass all earlier filters (from the slice lead-in). [stated] Fix: this milestone's forward model plus S6 scoring.
- Problem: using the aircraft state at the reception time is wrong and would make the search fail. [stated] Fix deferred to M8 (emission-time velocity). [stated]

## 8. Gaps

- ADS-B interpolation method and time step for the model. Best guess: linear interpolation of lat/lon/alt to 1 s or finer, velocity from finite differences. Confidence: medium. [inferred] M7-I01
- Sign convention of v_r. Best guess: positive when receding, negative when approaching, so pre-CPA points sit above f0 (about 210 Hz). Confidence: high. [inferred] M7-I09
- Implementation language and libraries. Best guess: Python with NumPy. Confidence: medium. [inferred] M7-I03
- Coordinate frame for the 3D geometry. Best guess: local ENU metres around the candidate point, with altitude from ADS-B and ground elevation from the DEM (S3). Confidence: medium. [inferred] M7-I04
- Demo geometry does not add up: (0, 980, 1020) has length 1414.5 m, not 1419 m, and v has a 16.8 m/s y-component yet v_r = 0 at t = 0. The observer is likely not at the origin or at a small height. Treat demo numbers as illustrative only. Confidence: medium. [inferred] M7-I05
- Whether c is fixed at 343 m/s or adjusted for temperature or altitude. Best guess: fixed 343 m/s. Confidence: high. [inferred] M7-I06
- Whether the source's own velocity also changes f0 (engine/prop RPM changes). Best guess: f0 held constant per event. Confidence: medium. [inferred] M7-I07
- Time span modelled around CPA. Best guess: match the spectrogram window, about +/-60 s (the fit panel spans 01:50:30 to 01:52:15). Confidence: low. [inferred] M7-I08
