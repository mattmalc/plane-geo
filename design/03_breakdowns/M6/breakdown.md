# M6: Apply speed, slant-distance, and silence filters

Range: 00:10:38 to 00:13:35. Systems: S1, S3, S4.

## 1. Goal and done criteria

Goal: cut the US-wide set of candidate observer points down using every constraint the spectrogram measurements give. The constraints are speed, CPA slant distance, the 920 s gap between the two events, and the silence between them. [stated]

Done means:
- Flight segments are split into an event 1 set (green) and an event 2 set (pink) by measured velocity range. [shown] [frames/M6_001043.png](frames/M6_001043.png), [frames/M6_001048.png](frames/M6_001048.png)
- Candidate points exist only at the measured slant distance from those segments. [stated] [00:10:59]
- Points pass if they hear a green segment, then a pink segment 920 s later, each at the right speed and distance. About 73,000 points pass (also called "roughly 70,000"). [stated] [00:11:10] [00:12:44]
- A silence filter removes any point that would have heard a flight between the two events. About 15,000 points remain. [stated] [00:12:49]
- The output is a point layer that can be viewed in QGIS. [shown] [frames/M6_001303.png](frames/M6_001303.png)

## 2. Procedure

1. Start from all propeller flights for the day, drawn in orange over the continental US. [shown] [00:10:40] ![all prop flights](frames/M6_001040.png)
2. Keep the flight segments whose speed falls in the event 1 range, 130 to 154 m/s. Draw them green. [shown] [00:10:43] ![event 1 segments](frames/M6_001043.png)
3. Keep the flight segments whose speed falls in the event 2 range, 88 to 110 m/s. Draw them pink. [shown] [00:10:48] ![event 1 and event 2 segments](frames/M6_001048.png)
   - The segments are short pieces of whole flight tracks, not whole tracks. [shown] [00:10:52] ![zoomed segments, Nebraska-like farmland](frames/M6_001052.png)
   - Speed is likely ADS-B ground speed per track point, and a segment is a run of consecutive points inside the range. [inferred] M6-I01
4. State the target pattern: a point that heard a green line, then a pink line 920 s later. [stated] [00:10:49] The ranges graphic gives the numbers. [shown] ![ranges graphic](frames/M6_001055.png)
5. Place candidate points only at the measured slant distance from each segment, not across the full 0 to 10 km grid used earlier. [stated] [00:10:59] Event 1 uses 4300 to 7800 m. Event 2 uses 1390 to 4690 m. [shown] [frames/M6_001055.png](frames/M6_001055.png)
   - The creator measures point-to-track distances with the QGIS Measure tool: 3672.704 m and 3299.240 m (ellipsoidal). [shown] [00:11:01] [00:11:11] ![measure 3672 m](frames/M6_001101.png) ![measure 3299 m](frames/M6_001111.png)
   - Slant distance converts to a horizontal band using ADS-B altitude and DEM ground height: horizontal = sqrt(slant^2 - (alt_msl - ground_elev)^2). [inferred] M6-I02
6. Run the time-offset filter. For each point, find a green segment heard at the right speed and distance, and a pink segment heard 920 s later at the right speed and distance. About 73,000 points pass. [stated] [00:11:10] [00:12:28]
7. Inspect the clusters. Most of the 73,000 points sit near airports, because dense traffic gives more chance of a matching pair. [stated] [00:11:17] [00:11:26]
   - A small airfield with looping pink tracks and a regular grid of red points. [shown] [00:11:20] ![airfield cluster](frames/M6_001120.png)
   - US overview of the 73,000 points over green and pink segments. [shown] [00:11:21] ![US overview](frames/M6_001121.png)
   - City-scale and close-up clusters. [shown] [00:11:22] [00:11:23] ![city clusters](frames/M6_001122.png) ![close-up clusters](frames/M6_001123.png)
   - A large hub airport with a point grid around its runways. [shown] [00:11:30] ![hub airport](frames/M6_001130.png) The layout looks like Dallas/Fort Worth International. [inferred] M6-I03
8. Use the silence in the recording. No Doppler curve appears between the two events, almost 15 minutes. [stated] [00:11:41] ![spectrogram](frames/M6_001141.png)
   - A spot near a major airport would not have 15 quiet minutes. [stated] [00:11:43]
   - All prop flights over a metro area show how dense the traffic is around the clusters. [shown] [00:11:47] ![metro prop traffic](frames/M6_001147.png)
9. Apply the silence filter to the 73,000 points. Disqualify any point that would have heard a flight between event 1 and event 2. [stated] [00:12:02] ![points before silence filter](frames/M6_001207.png)
10. Set the hearing threshold. A point "heard a flight" if that flight came within Max(event1 CPA, event2 CPA). No loudness multiplier is applied. [shown] [00:12:11] ![silence filter logic](frames/M6_001211.png)
11. Recap the chain: velocity-filtered segments, slant-distance candidate points, 920 s offset filter, silence filter. [stated] [00:12:18] ![recap graphic](frames/M6_001223.png)
    - A Measure reading of 167.101 m appears during the recap. [shown] [00:12:24] ![measure 167 m](frames/M6_001224.png) What it measures is not said. [inferred] M6-I04
    - A "CPA Timeline" tool shows CPA times as vertical lines with a 920 s sliding window. [shown] [00:12:29] ![CPA timeline](frames/M6_001229.png)
12. The silence filter drops about 70,000 points to about 15,000. [stated] [00:12:49] ![points after silence filter](frames/M6_001252.png) ![15,000 points map](frames/M6_001303.png)
13. Stop the simple search here. The only other evidence is a static picture with nothing more to extract. Velocity, slant distance, time offset, and silence use up what the simple spectrogram measurements give. [stated] [00:13:15] [00:13:20] ![static source frame](frames/M6_001316.png)
    - The 00:13:16 and 00:13:23 visual moments both show only this treeline frame. It holds no extractable detail. [shown]

## 3. Components

Measured event constraints, read from the ranges graphic [shown] [frames/M6_001055.png](frames/M6_001055.png):

| Item | Event 1 | Event 2 |
|---|---|---|
| Velocity | 130-154 m/s | 88-110 m/s |
| Slant distance at CPA | 4300-7800 m | 1390-4690 m |
| Map colour | green [shown] | pink [shown] |

- Event gap: 920 sec. [shown] [frames/M6_001055.png](frames/M6_001055.png)
- Tolerance on the 920 s gap: about 5 s, per the S4 system description from stage 2. Not shown in this range. [inferred] M6-I05
- Silence window: almost 15 minutes between the events. [stated] [00:11:43]
- Silence hearing threshold: Max(event1 CPA, event2 CPA), multiplier 1.0. A 1.5x or 2x multiplier was considered and rejected. [shown] [frames/M6_001211.png](frames/M6_001211.png)
- Point counts: about 73,000 after the offset filter (also "roughly 70,000"); about 15,000 after the silence filter. [stated] [00:11:10] [00:12:44] [00:12:49]
- Earlier grid extent replaced here: 0 to 10 km from each track. [stated] [00:11:01]
- Candidate grid spacing at the slant-distance band: likely still 200 m, as in S4. Points in the airfield close-up form a regular grid. [inferred] M6-I06
- Spectrogram view: 60:00.000 total length, playhead 38:26.617 (2306.617 s), frequency axis 5 to 800 Hz, time axis about 1980 to 2420 s. [shown] [frames/M6_001141.png](frames/M6_001141.png)
- Ranges-graphic spectrogram: time axis 2100 s to 3100 s, frequency 5 to 400 Hz, cursor at 2585.500 s. [shown] [frames/M6_001055.png](frames/M6_001055.png)
- Measure tool readings (ellipsoidal, metres): 3672.704 m, 3299.240 m, 167.101 m. [shown] [frames/M6_001101.png](frames/M6_001101.png) [frames/M6_001111.png](frames/M6_001111.png) [frames/M6_001224.png](frames/M6_001224.png)
- Measure tool coordinates: -10881946.310, 5154349.972 to -10886834.012, 5153694.668; -10882863.0..., 5162529.339 to -10878984.391, 5160374.541; -10404808.145, 5409624.738 to -10404684.0..., 5409429.766. [shown]
- These coordinates are EPSG:3857 Web Mercator metres. The first two pairs sit near 42.0 N, 97.75 W (northeast Nebraska). The third sits near 43.6 N, 93.5 W (southern Minnesota). [inferred] M6-I07
- CPA Timeline tool: "Window length (s): 920", "left = 18:17:55", "right = 18:33:25", time axis 18:00:00 to past 02:00:00. [shown] [frames/M6_001229.png](frames/M6_001229.png)
- File formats: the QGIS layers are vector point and line layers. The format is not shown. [inferred] M6-I08

## 4. Systems touched

### S1 ADS-B ingest and aircraft filtering
- How it works here: the propeller-only flight set (jets dropped earlier) is cut into segments by velocity range. [shown] [frames/M6_001040.png](frames/M6_001040.png) [frames/M6_001048.png](frames/M6_001048.png)
- Inputs: whole prop flight tracks with position, altitude, speed, and timestamp. Event velocity ranges from S2.
- Outputs: two segment layers, event 1 (green) and event 2 (pink). [shown]
- Connects to: S4, which lays points along these segments. S3, which needs segment altitude and time.
- The layer panel lists "all_fligh...", "prop_fl...", and pink layer "15113_...". Names are truncated. [shown] [frames/M6_001303.png](frames/M6_001303.png)

### S3 Acoustic geometry and propagation model
- How it works here: slant distance at CPA defines where points go. CPA time sets the 920 s pairing. [stated] [00:11:04]
- Inputs: segment positions and altitudes, DEM ground elevation (layer "dem_m..." in the panel [shown]), speed of sound.
- Outputs: per point and flight, CPA slant distance and CPA time.
- The 920 s pairing likely uses delayed CPA times (CPA time plus slant distance divided by speed of sound), as the project summary describes. [inferred] M6-I09
- Connects to: S4 for the offset and silence tests. S5 later for emission-time modelling.

### S4 Candidate grid and constraint filters
- How it works here: three filters in sequence.
  1. Placement: points only in the measured slant-distance band of each segment. [stated] [00:12:23]
  2. Offset: the point hears a green segment then a pink segment 920 s later, each at the right speed and distance. [stated] [00:12:28]
  3. Silence: the point hears no flight between the two events within the threshold distance. [stated] [00:12:44]
- Inputs: segment layers from S1, CPA geometry from S3, ranges and the 920 s gap from S2.
- Outputs: about 73,000 points after step 2, about 15,000 after step 3. [stated]
- Connects to: S5 and S6, which model and score curves for the 15,000 survivors in later milestones. S7, which displays the point layers in QGIS.

## 5. Code, configs, formulas, and on-screen text

Silence filter slide, verbatim [shown] [00:12:11] [frames/M6_001211.png](frames/M6_001211.png):

```
Silence filter logic:
• Goal is to disqualify any candidate point which heard one or more flights between event 1 and event 2
• But how do you determine whether a point 'Heard a flight'?
• At what distance do you set the threshold of hearing?
• Any heuristic would not take into account the microphone's sensitivity and actual acoustics
• To account for this, we conservatively set the audible threshold distance as Max(event1 CPA, event2 CPA)
• All we know confidently is that we heard both events, so the further of the two is still audible.
• You could assume that since both events are fairly loud, potentially a 1.5x or 2x multiplier is reasonable
• However, not all planes are the same loudness, so to not potentially disqualify the correct point, no multiplier was added.
```

Ranges graphic, verbatim [shown] [frames/M6_001055.png](frames/M6_001055.png):

```
920 sec
130-154m/s                    88-110m/s
4300-7800m away at CPA        1390-4690m away at CPA
```

CPA Timeline tool, verbatim [shown] [frames/M6_001229.png](frames/M6_001229.png):

```
CPA Timeline
Window length (s): 920    left = 18:17:55    right = 18:33:25
slide window
18:00:00  20:00:00  22:00:00  00:00:00  02:00:00
time
```

Filter logic as formulas. These restate the stated logic in symbols. [inferred] M6-I10

```
v1_min <= v(seg_g) <= v1_max,  v1 = [130, 154] m/s
v2_min <= v(seg_p) <= v2_max,  v2 = [88, 110] m/s
d1_min <= d_slant(P, seg_g) <= d1_max,  d1 = [4300, 7800] m
d2_min <= d_slant(P, seg_p) <= d2_max,  d2 = [1390, 4690] m
| (t_cpa(P, seg_p) - t_cpa(P, seg_g)) - 920 | <= tol
silence: no flight f with t_cpa(P, seg_g) < t_cpa(P, f) < t_cpa(P, seg_p)
         and d_slant_cpa(P, f) <= max(d_slant(P, seg_g), d_slant(P, seg_p))
```

Slant-to-horizontal conversion: d_h = sqrt(d_slant^2 - (h_aircraft_msl - h_ground)^2). [inferred] M6-I11

QGIS layer panel names, truncated [shown] [frames/M6_001303.png](frames/M6_001303.png) [frames/M6_001224.png](frames/M6_001224.png): dem_m..., all_fligh..., prop_fl..., single ev..., post off..., post sile..., 135..., 15113_..., post sile..., data erro..., test area..., flightpat..., event sc..., 1:35:52, 1:21:20, 1:51:1..., old, old, th, google, carto, bing, norway.

## 6. Tools and software

- QGIS: map display, layer panel, Measure tool in ellipsoidal mode. [shown] [frames/M6_001101.png](frames/M6_001101.png)
- Basemaps: Google satellite, with Carto and Bing layers present. [shown] [frames/M6_001303.png](frames/M6_001303.png)
- A custom spectrogram viewer with playhead, time axis in seconds, and a "Claude Code" label in its status bar. [shown] [frames/M6_001141.png](frames/M6_001141.png)
- A custom "CPA Timeline" web tool with a window-length field and slide control. [shown] [frames/M6_001229.png](frames/M6_001229.png)
- Python for the filters, per the description's methodology. [stated]

## 7. Problems and fixes

- Problem: 73,000 points pass the offset filter, mostly clustered at airports. [stated] [00:11:26] Fix: the silence filter, using the 15 quiet minutes as a constraint. [stated] [00:12:02]
- Problem: there is no reliable way to set a hearing distance, since microphone sensitivity and acoustics are unknown. [shown] [frames/M6_001211.png](frames/M6_001211.png) Fix: use the farther of the two event CPAs as the threshold, with no multiplier, so the true point is not lost. [shown]
- Problem: 15,000 points still remain because the land area and flight count are large. [stated] [00:12:58] The usual fix of inspecting points and writing new filters is not possible, since the only other evidence is a static picture. [stated] [00:13:06] Resolution comes in the next milestone with full Doppler curve modelling. [stated] [00:13:35]

## 8. Gaps

- G1. Speed source and segment definition. Best guess: ADS-B ground speed per point, segments are runs of in-range points. Confidence medium. [inferred] M6-I12
- G2. Tolerance on the 920 s gap. Best guess: about 5 s, from the S4 description, to cover CPA-time measurement error. Confidence medium. [inferred] M6-I13
- G3. Whether CPA times in the pairing and silence test are delayed by sound travel time. Best guess: yes, delayed CPA times using slant distance and a fixed speed of sound near 343 m/s. Confidence medium. [inferred] M6-I14
- G4. The silence threshold Max(event1 CPA, event2 CPA): per-point modelled CPAs or the range upper bound (7800 m). Best guess: per-point CPA distances of the matched pair. Confidence medium. [inferred] M6-I15
- G5. Which flights count in the silence test: all flights including jets, or props only. Best guess: props only, since jets were dropped at ingest. Confidence low. [inferred] M6-I16
- G6. Handling of multiple green-pink pairs per point. Best guess: a point passes if any pair passes the offset and silence tests. Confidence medium. [inferred] M6-I17
- G7. Silence window bounds: open interval between the two CPA times, or a buffer around each event. Best guess: strictly between the two CPA times with a few seconds of margin. Confidence low. [inferred] M6-I18
- G8. Point spacing in the slant-distance band. Best guess: 200 m grid clipped to the band. Confidence medium. [inferred] M6-I19
- G9. CPA Timeline shows left 18:17:55 and right 18:33:25, a 930 s span, while the window is 920 s. Best guess: the display pads the window or rounds. Confidence low. [inferred] M6-I20
- G10. The 73,000 and 15,000 counts are rounded. Exact values are not shown. The pink layer name "15113_..." may be an id, not a count. Confidence low. [inferred] M6-I21
- G11. Altitude datum. Best guess: ADS-B barometric or geometric altitude treated as MSL and differenced with DEM elevation. Confidence medium. [inferred] M6-I22
- G12. Storage format for segments and points. Best guess: GeoPackage or GeoJSON loaded in QGIS, in EPSG:3857 for display. Confidence low. [inferred] M6-I23
