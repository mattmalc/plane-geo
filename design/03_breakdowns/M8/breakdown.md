# M8 breakdown: Correct the model for sound travel time

Range: 00:16:45 to 00:18:10. Systems: S3, S5.

## 1. Goal and done criteria

Goal: replace the naive Doppler forward model with an emission-time (retarded-time) model. [stated]

The naive model uses the aircraft's radial velocity at the time the observer hears the sound. The creator says this is wrong and "would make our search fail entirely." [stated] [00:16:43]

The correct model uses the radial velocity at the moment the sound was emitted. [stated] [00:17:01]

Done looks like this:
- For each reception time t_r, the model solves for the emission time t_e, takes the aircraft position and velocity at t_e, computes the 3D radial velocity, and applies the Doppler equation. [shown] [00:17:14]
- The emission-time curve has a different shape from the naive curve. A pure time shift cannot make them match. [stated] [00:17:32]
- On a real spectrogram, the emission-time curve overlays the observed Doppler trace and the naive curve does not. [shown] [00:17:53]
- The model runs for every candidate point and every flight. [stated] [00:17:56]

## 2. Procedure

1. Start from the naive curve built in M7. The demo app "Building the Doppler Curve, Step by Step" is in "position" mode. At step 11/11 (t = 25.00 s) the naive model gives 94.11 Hz. [shown] [00:16:45] ![naive curve](frames/M8_001645.png)
2. Note the naive value at CPA. In position mode at t = 0.00 s, v_r = 0.00 m/s and f = 130.00 Hz, which equals f0. [shown] [00:17:00] ![naive t=0](frames/M8_001700.png)
3. Switch the app to "Delayed" mode. For reception time t_r = 0.00 s, solve t_r = t_e + r(t_e)/c for t_e. The result is t_e = -4.539 s. [shown] [00:17:14] ![emission solve](frames/M8_001714.png)
   - The map marks the aircraft's "true position" at reception time and a separate marker at the emission position. A tooltip reads "emission time = -4.54 s (07:12:25)", "velocity = 141.0 m/s", "radial velocity = -57.97 m/s". [shown]
4. Take the aircraft state at t_e: position (-636, 904, 1020) m, velocity (140.0, 16.8, 0.0) m/s, distance r(t_e) = 1557 m, radial component v_r = -57.97 m/s. Apply Doppler: f = 130 * 343/(343 + -57.97) = 156.44 Hz. Plot that at reception time 07:12:30. [shown] [00:17:21] ![emission construction](frames/M8_001721.png)
   - The plot tooltip still shows the naive point at "07:12:30, freq = 130.00 Hz" at this step. [shown]
5. Repeat for every reception time step. At t_r = 15.00 s: t_e = 9.352 s, position (1309, 1137, 1020) m, r(t_e) = 1937 m, v_r = 95.97 m/s, f = 101.58 Hz. [shown] [00:17:24] ![step 9](frames/M8_001724.png) At t_r = 25.00 s: t_e = 16.910 s, position (2367, 1264, 1020) m, r(t_e) = 2775 m, v_r = 121.16 m/s, f = 96.07 Hz. [shown] [00:17:25] ![both curves](frames/M8_001725.png)
6. Compare the two curves. Both "Position" and "Delayed" are checked on the plot. A slider "slide Delayed curve" shifts the delayed curve in time. [shown] [00:17:25]
   - At -1.5 s the curves still differ, by about 25 Hz near t = 0. [shown] [00:17:36] ![slide -1.5 s](frames/M8_001736.png)
   - At -9.5 s the curves cross near 07:12:10 but diverge in the middle. [shown] [00:17:39] ![slide -9.5 s](frames/M8_001739.png)
   - At -5.0 s the curves lie close together over most of the demo window, with small gaps at the ends. [shown] [00:17:48] ![slide -5.0 s](frames/M8_001748.png) The coarse 5 s demo understates the shape difference. The real-data panel shows it clearly. [inferred] M8-I17
   - Conclusion: the naive method "made an entirely wrong curve," not the right curve a few seconds late. [stated] [00:17:43]
7. Check against real data. The panel "Right vs Wrong Model -- Real Data (1:35:52, flightid 1100069709)" shows one spectrogram, one flight, and one candidate location. [shown] [00:17:48]
   - Bare spectrogram, no model toggled. [shown] [00:17:50] ![bare spectrogram](frames/M8_001750.png)
   - Wrong (naive) curve in red, Δt = -21.90 s, f0 = 112.5 Hz. It runs above the trace early and misses the steep middle section. [shown] [00:17:53] ![naive over spectrogram](frames/M8_001753.png)
   - Right (correct) curve in green, Δt = -0.60 s, f0 = 112.5 Hz. It follows the trace across the whole window. A marker "delayed-CPA, from flight geometry" sits on the dashed line "delayed-CPA timestamp, from measurement". [shown] [00:17:54] ![emission-time over spectrogram](frames/M8_001754.png)
8. Repeat the model for all candidate points and all flights. [stated] [00:17:56] The screen shows a grid of small spectrograms, each labelled "FlightID:<id> <lat>, <lon>" with a yellow modelled curve. [shown] [00:18:06] ![per-candidate grid](frames/M8_001806.png) Zoomed out, the grid holds hundreds of tiles. [shown] [00:18:09] ![grid zoomed out](frames/M8_001809.png)

## 3. Components

Demo parameters (synthetic flight in the step-by-step app):
- Aircraft speed slider: 140 m/s. [shown] [00:16:45]
- CPA distance slider: 980 m. [shown]
- Altitude slider: 1020 m. [shown]
- Emitted frequency f0 slider: 130 Hz. [shown]
- Speed of sound c = 343 m/s. [shown]
- Velocity vector (140.0, 16.8, 0.0) m/s, magnitude 141.0 m/s. [shown]
- 11 steps, plotted at 5 s spacing on axis labels 07:12:05 to 07:12:50. t = 0 corresponds to 07:12:30. [shown]
- Reception times run from -25 s to +25 s in 5 s steps. [inferred] M8-I01
- Aircraft z stays at 1020 m, so the demo flight is level. [shown]
- The demo track is a constant-velocity straight line: x = 140 t, y = 980 + 16.8 t matches the emission positions shown. [inferred] M8-I02

Emission-time values read off screen:

| t_r (s) | t_e (s) | position at t_e (m) | r(t_e) (m) | v_r (m/s) | f (Hz) |
|---|---|---|---|---|---|
| 0.00 | -4.539 | (-636, 904, 1020) | 1557 | -57.97 | 156.44 |
| 15.00 | 9.352 | (1309, 1137, 1020) | 1937 | 95.97 | 101.58 |
| 25.00 | 16.910 | (2367, 1264, 1020) | 2775 | 121.16 | 96.07 |

All values [shown]. Each row satisfies t_r = t_e + r(t_e)/343 to within 1 ms. [inferred] M8-I03

Naive values read off screen:
- t = 0.00 s: position (0, 980, 1020) m, r = 1419 m, v_r = 0.00 m/s, f = 130.00 Hz. [shown] [00:17:00]
- t = 25.00 s: position (3500, 1400, 1020) m, r = 3800 m, v_r = 130.80 m/s, f = 94.11 Hz. [shown] [00:16:45]

Real-data panel:
- Recording timestamp 1:35:52, flight id 1100069709. [shown] [00:17:48]
- x axis "elapsed recording time (s)", about 5690 to 5880 s. [shown]
- y axis "frequency (Hz)", about 80 to 190 Hz. [shown]
- f0 = 112.5 Hz for both curves. [shown]
- Naive Δt = -21.90 s. Correct Δt = -0.60 s. [shown]
- Dashed line labelled "delayed-CPA timestamp, from measurement" at about 5752 s, which equals 1:35:52. [shown]
- Legend: "RIGHT (retarded emission-time)". [shown] [00:17:54]

Grid view labels (sample): FlightID:1100069709 at 40.87736, -73.52257; FlightID:1100092122 at 42.93450, -78.84147; FlightID:1100029918 at 36.45408, -94.45483; FlightID:1100088546 at 45.69860, -73.64376; FlightID:1100065108 at 42.01283, -81.43261. [shown] [00:18:06]

## 4. Systems touched

S3, acoustic geometry and propagation model.
- How it works: for each reception time it solves t_r = t_e + r(t_e)/c for t_e, where r is the 3D slant distance from the aircraft at t_e to the observer. [shown]
- Inputs: aircraft track (position against time), observer position, c = 343 m/s. [shown]
- Outputs: emission time t_e, emission position, and r(t_e). [shown]
- Connections: gets the track from S1 (interpolated ADS-B) and the observer point from S4. Passes the emission state to S5. [stated in the methodology description]
- The demo uses a flat z with no terrain. The real pipeline uses ADS-B altitude above sea level and DEM ground elevation. [stated in the description]

S5, Doppler curve forward model.
- How it works: projects the aircraft velocity at t_e onto the line from the aircraft to the observer to get the 3D radial component v_r. Then f = f0 * c/(c + v_r). [shown]
- Sign: v_r is negative when the aircraft approaches (f > f0) and positive when it recedes (f < f0). [shown]
- Inputs: emission state from S3, f0 from the S2 measurement. [stated] (f0 "comes from here, where we measure the curve," [00:16:17], just before this milestone.)
- Outputs: a modelled frequency curve against reception time for each candidate point and flight. [stated] [00:18:02]
- Connections: the curves feed S6 scoring. Δt and f0 sliders on the real-data panel preview the S6 sweep over CPA time offset and fundamental frequency. [inferred] M8-I04

## 5. Code, configs, formulas, and on-screen text

Formulas, verbatim from the app [shown]:

```
reception time (when you hear it)      t_r = 0.00 s
solve for emission time                t_r = t_e + r(t_e) / c
emission time                          t_e = -4.539 s
aircraft position (at t_e)             (x, y, z) = (-636, 904, 1020) m
full velocity (at t_e)                 v = (140.0, 16.8, 0.0) m/s
distance to observer (at t_e)          r(t_e) = 1557 m
radial component (3D, at t_e)          v_r = -57.97 m/s
Doppler equation                       f = f0 * c / (c + v_r) = 130 * 343 / (343 + -57.97) = 156.44 Hz
```

In LaTeX:

$$t_r = t_e + \frac{r(t_e)}{c}$$
$$f(t_r) = f_0 \cdot \frac{c}{c + v_r(t_e)}$$

Radial velocity as a formula is not shown. The standard form is v_r = v · (p_aircraft - p_observer) / |p_aircraft - p_observer|. [inferred] M8-I06

Real-data panel caption, verbatim [shown] [00:17:48]:

> Same real spectrogram, same flight, same candidate location. Green is the correct model (solves for when the sound actually left the aircraft); red is the naive model (uses the aircraft's position at the moment the sound is heard, as if sound traveled instantly). Sliders move whichever curve(s) are currently toggled on, together, at the same dt/f0.

Other UI text [shown]: "Building the Doppler Curve, Step by Step"; buttons "Position", "Delayed", "Reset", "Prev", "Play", "Next", "step 11 / 11"; plot title "Frequency heard by observer"; legend "full velocity", "radial component (used)"; checkboxes "Position", "Delayed"; "slide Delayed curve: -9.5s"; checkboxes "Right (correct)", "Wrong (naive)".

## 6. Tools and software

- Interactive browser demo with a top-down map, a formula panel, and a frequency plot. [shown]
- The plot toolbar (camera, zoom, pan, box select, lasso, autoscale, home icons) matches Plotly. [inferred] M8-I07
- Formulas are typeset like KaTeX or MathJax. [inferred] M8-I08
- The real-data panel is a separate page with a spectrogram heat map and toggled overlay curves. [shown] [00:17:48]
- No code or tools are released. [stated in the description]

## 7. Problems and fixes

- Problem: the naive model uses radial velocity at hearing time. This ignores sound travel time and gives the wrong curve shape. The creator says it would make the search fail. [stated] [00:16:43]
- Wrong fix the creator rules out: delaying the naive curve in time. Shifting by -1.5 s or -9.5 s leaves visible mismatches. [shown] [00:17:36] [00:17:39]
- Fix: solve for emission time per reception step and use v_r at emission time. [stated] [00:17:08]
- Evidence on real data: the naive curve misfits even with a -21.90 s offset. The emission-time curve fits with a -0.60 s offset. [shown] [00:17:53] [00:17:54]

## 8. Gaps

- G1. How the creator solves t_r = t_e + r(t_e)/c. Best guess: fixed-point iteration t_e ← t_r - r(t_e)/c, starting at t_e = t_r, for 3 to 5 iterations. It converges because aircraft speed is well below c. Bisection or Newton also works. Confidence: medium. [inferred] M8-I09
- G2. How the track is interpolated between ADS-B samples to get position and velocity at t_e. Best guess: linear interpolation of lat, lon, and altitude in time, converted to a local ENU frame in metres. Velocity comes from finite differences or from the ADS-B ground speed and track. Confidence: medium. [inferred] M8-I10
- G3. Observer coordinates in the demo. The demo shows v_r = 0 at t = 0, but r = 1419 m does not equal sqrt(980² + 1020²) = 1414.5 m. The observer is probably not at the origin, or has a small elevation. Rebuild impact is nil because the demo is illustrative. Confidence: low. [inferred] M8-I11
- G4. Time step of the real model. The demo uses 5 s steps. The real curve looks smooth across about 190 s. Best guess: evaluate at the spectrogram frame times, around 0.1 to 0.5 s spacing. Confidence: low. [inferred] M8-I12
- G5. Speed of sound in the real pipeline. The demo uses 343 m/s, the value at about 20 °C. Best guess: a constant 343 m/s with no temperature or wind correction. Confidence: medium. [inferred] M8-I13
- G6. Altitude reference for r. The demo uses a flat z. Best guess: aircraft altitude above sea level (geometric or barometric ADS-B) minus DEM ground elevation at the observer, per S3. Confidence: medium. [inferred] M8-I14
- G7. Doppler sign convention. The demo uses f = f0 c/(c + v_r), with v_r positive when receding. This is a moving-source, stationary-observer form with no wind term. Best guess: the real pipeline uses the same form. Confidence: high. [inferred] M8-I15
- G8. Meaning of the real-data Δt values. Best guess: Δt is a time offset applied to the modelled curve. The naive curve was moved to its best visual fit, and the correct curve needed only -0.60 s. This matches the S6 CPA-time sweep. Confidence: medium. [inferred] M8-I05
- G9. Compute cost and batching for "all candidate points and all flights." This is not shown. Best guess: vectorise over candidates with NumPy and evaluate only over each flight's audible window. Confidence: low. [inferred] M8-I16
