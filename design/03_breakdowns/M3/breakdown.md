# M3 breakdown: Grid candidate points and compute delayed CPA times

Range: 00:04:14 to 00:07:04. Systems: S3, S4.

## 1. Goal and done criteria

Goal: give every candidate observer point a list of the flights it could hear and the time each flight's CPA sound arrived there. This list feeds the 920 s offset filter that starts at 00:07:04. [stated]

The goal is set up by the "920 sec" graphic: two plane events on one spectrogram timeline, 920 s apart. [shown] [frames/M3_000417.png](frames/M3_000417.png)

Done looks like this:
- A 200 m grid of points covers 10 km around each flight track. [stated]
- Each grid point has, per flight, a `retarded_cpa_time`, a `cpa_distance_m`, and a `ground_elevation_m`. [shown] [frames/M3_000450.png](frames/M3_000450.png)
- After all flights in the area are processed, each grid point holds `n_flights`, a list of `flight_ids`, and a matching list of `retarded_cpa_times`. [shown] [frames/M3_000658.png](frames/M3_000658.png)
- Acceptance check: rebuilding the worked example on flight 1099966250 gives grid point fid 43956 a delayed CPA time of 22:46:46 and a CPA distance of about 3364.77 m. [inferred] M3-I01

## 2. Procedure

1. Pick a small test area and one flight to illustrate. [stated] [00:04:13] The flight track is the pink line. [shown] [00:04:21] ![](frames/M3_000421.png)
2. Inspect the ADS-B track points. Each point has coordinates, altitude, timestamp, and more. [stated] [00:04:21] The layer is `flight_1099966250_track_1sec`. [shown] [00:04:26] ![](frames/M3_000425.png) ![](frames/M3_000426.png)
3. Lay a 200 m grid of candidate observer points. [stated] [00:04:32] The grid shows as orange dots over the satellite basemap. [shown] ![](frames/M3_000432.png) ![](frames/M3_000434.png)
4. Define the event time as the CPA. The creator expands CPA as "Closest Point of Arrival", after a joke slide that rejects another meaning of CPA. [shown] [00:04:42] ![](frames/M3_000442.png) ![](frames/M3_000445.png) These two frames are slides, not the map. The observer-to-track geometry is in step 6.
5. Explain why a single time is needed. The "920 sec" graphic returns for "heard a plane 920 seconds later". [shown] [00:04:51] ![](frames/M3_000451.png) An observer hears the plane over many track points. [stated] [00:04:56] The creator measures distances from one grid point to several track points: 2873.018 m and 2171.493 m. [shown] [00:05:00] ![](frames/M3_000500.png) ![](frames/M3_000502.png) The whole Doppler curve lasts almost two minutes. [stated] [00:05:02] ![](frames/M3_000503.png) ![](frames/M3_000506.png) The CPA time is roughly the middle of the curve, when the plane is closest and loudest. [stated] [00:05:07]
6. For the flight, lay the grid out to a 10 km radius. [stated] [00:05:12] The buffer around the track shows as an orange grid region. The measure tool reads 9765.382 m from the track to the buffer edge. [shown] [00:05:18] ![](frames/M3_000511.png) ![](frames/M3_000514.png) ![](frames/M3_000518.png) The creator calls 10 km conservative: beyond it you probably would not hear a plane even in ideal conditions. [stated] [00:05:14]
7. For each grid point, find the CPA on the track. The track point nearest the example observer has `utc_time` 22:46:36. [shown] [00:05:36] ![](frames/M3_000536.png) The creator says "22, 46, 36". [stated] [00:05:32]
8. Convert CPA time to delayed CPA time. This is the time the CPA sound reaches the observer. [stated] [00:05:38] The example sound path is "three plus kilometers". [stated] [00:05:49] The measure tool reads 3255.499 m horizontal from the grid point to the track. [shown] [00:05:52] ![](frames/M3_000552.png)
9. Use the 3D slant distance, not the horizontal distance. [stated] [00:05:55] The sketch shows a plane, a stick-figure listener, and a red hypotenuse from plane to listener. [shown] [00:06:02] ![](frames/M3_000555.png) ![](frames/M3_000558.png) ![](frames/M3_000602.png)
10. Correct the altitude datum. ADS-B altitude is height above sea level, not above ground. [stated] [00:06:07] The sketch adds a cliff down to the sea, with a tall bar from sea level to the plane and a bar for the ground height under the listener. [shown] [00:06:13] ![](frames/M3_000613.png) ![](frames/M3_000618.png)
11. Sample a DEM at each grid point for ground elevation. [stated] [00:06:18] The DEM layer is `dem_mosaic_1km`. One identify click reads Band 1 = 907.984. [shown] [00:06:22] ![](frames/M3_000620.png) ![](frames/M3_000622.png)
12. Write the per-flight result to each grid point. For the example point: CPA time 22:46:34, delayed CPA time 22:46:46. [stated] [00:06:24] The track point panel shows `utc_time` 22:46:34, and the grid point panel shows `retarded_cpa_time` 22:46:46. [shown] [00:06:29] ![](frames/M3_000629.png) ![](frames/M3_000632.png) See Problems: 22:46:34 does not match the 12 s delay.
13. Repeat for every grid point of the flight. That finishes one flight. [stated] [00:06:32] ![](frames/M3_000638.png)
14. Repeat for every flight in the area. [stated] [00:06:41] Other flights include a looping track. [shown] ![](frames/M3_000642.png) ![](frames/M3_000644.png) The test area is a purple rectangle of grid points crossed by many orange flight tracks. [shown] [00:06:44] ![](frames/M3_000646.png) ![](frames/M3_000651.png) Nearly every point heard at least one flight, because of the 10 km radius. [stated] [00:06:45]
15. Each grid point now holds a list of flight IDs and delayed CPA times. [stated] [00:06:50] Layer `gridpoints_heard_multiple`, fid 203833, `n_flights` 8. [shown] [00:06:58] ![](frames/M3_000658.png) If you stood there that day, at each of these times you would hear a plane. [stated] [00:06:55]

## 3. Components

| Item | Value | Tag |
|---|---|---|
| Date of ADS-B data | 2026-09-08 (epoch 1788907594 = 22:46:34 UTC) | [shown] timestamp; date conversion [inferred] M3-I02 |
| Track layer | `flight_1099966250_track_1sec` | [shown] |
| Track point fields | fid, timestamp, utc_time, lat, lon, alt_ft, gs_kt, vs_fpm, track_deg, valid | [shown] |
| Track resolution | one point per second (name `track_1sec`; consecutive points 22:46:34, 36, 37, 38 shown) | name [shown]; 1 s resampling [inferred] M3-I03 |
| Example track point fid 35312 | timestamp 1788907598, utc_time 22:46:38, lat 33.133577200082634, lon -85.95641385591946, alt_ft 4600, gs_kt 115.96153846153847, vs_fpm 0, track_deg 260.5, valid true | [shown] |
| Example track point fid 35310 | timestamp 1788907596, utc_time 22:46:36, lat 33.1335464868..., lon -85.955188849..., alt_ft 4600, gs_kt 116.076923076..., vs_fpm 0, track_deg 261, valid true | [shown] |
| Example track point fid 35308 | timestamp 1788907594, utc_time 22:46:34, lat 33.133157736..., lon -85.95396384..., alt_ft 4600, gs_kt 116.19..., vs_fpm 0, track_deg 261.5, valid true | [shown] |
| Altitude unit | feet, above sea level | units [shown] (`alt_ft`); datum [stated] |
| Grid spacing | 200 m | [stated] |
| Grid radius around track | 10 km | [stated]; measured 9765.382 m to buffer edge [shown] |
| Grid layer | `flight_1099966250_candidate_gridpoints` | [shown] (name truncated "...candidate_gridpoints — c...") |
| Grid point fid 43956 | retarded_cpa_time 22:46:46, cpa_distance_m 3364.7698672..., ground_elevation_m 257.477575286... | [shown] |
| Example horizontal distances | 3105.784 m, 2873.018 m, 2171.493 m, 3255.499 m (QGIS measure tool, ellipsoidal) | [shown] |
| DEM | `dem_mosaic_1km`, single band, continental US; sample value 907.984 | [shown] |
| DEM resolution | 1 km, from the layer name | [inferred] M3-I04 |
| DEM units | metres | [inferred] M3-I05 |
| Speed of sound | not shown or stated in M3 | see Gaps |
| Aggregate layer | `gridpoints_heard_multiple — points`; fields fid, n_flights, flight_ids, retarded_cpa_times | [shown] |
| Aggregate example fid 203833 | n_flights 8; flight_ids 1100037924, 1100049757, 1100043136, 1100041036, 1099966250, 1100102896, 1100... (truncated); retarded_cpa_times 19:13:28, 19:08:49, 19:09:00, 18:30:20, 22:44:51, 23:49:35, 00:36:59, 01:16:28 | [shown] |
| List storage format | comma-separated strings in one attribute field, ordered to match flight_ids | [shown] comma-separated; positional pairing [inferred] M3-I06 |
| Map CRS | Web Mercator (measure tool shows x around -9568413, y around 3916821 near lat 33.13) | [inferred] M3-I07 |
| Example location | near lat 33.13, lon -85.96 (east Alabama) | coordinates [shown]; place name [inferred] M3-I08 |
| Audio clip in spectrogram view | 60:00.000 long; selection 2082.529 s to 2085.787 s, duration 3.258 s, dominant 96 Hz, centroid 241 Hz, 88.0% energy in 0-250 Hz; frequency axis 5 to 800 Hz | [shown] |

## 4. Systems touched

### S3 Acoustic geometry and propagation model
- How it works: for each grid point and flight, find the track point closest in 3D. That point's time is the CPA time. Compute the 3D slant distance from plane to observer. Divide by the speed of sound to get the delay. Add the delay to the CPA time to get the delayed CPA time. [stated]
- Height: plane height above sea level comes from ADS-B `alt_ft`. Observer height comes from the DEM at the grid point. [stated]
- Inputs: 1 s track points (lat, lon, alt_ft, timestamp), grid point lat/lon, DEM. [shown]
- Outputs per grid point per flight: `retarded_cpa_time`, `cpa_distance_m`, `ground_elevation_m`. [shown]
- Connections: takes tracks from S1. Feeds S4's offset filter. The same slant distance and delay give the emission time used by S5. [stated] (project summary)

### S4 Candidate grid and constraint filters
- How it works in M3: a 200 m point grid within 10 km of each track. [stated] Per-flight results are merged into one layer where each point lists every flight it heard. [shown]
- Inputs: flight tracks after jet filtering from S1. [stated]
- Outputs: `gridpoints_heard_multiple` with n_flights, flight_ids, retarded_cpa_times. [shown]
- Connections: the next step (M4, from 00:07:04) checks each point's list for two delayed CPA times 920 s apart. [stated]

## 5. Code, configs, formulas, and on-screen text

No code is shown in this range. [shown]

On-screen text:
- "920 sec" (timeline graphic). [shown]
- "CPA", then "Closest Point of Arrival". [shown]
- Identify Results, track point: `flight_1099966250_track_1sec — track_1sec [2]`, fields as in Components. [shown]
- Identify Results, grid point: `flight_1099966250_candidate_gridpoints`, `retarded_cpa_time 22:46:46`, `fid 43956`, `cpa_distance_m 3364.7698672...`, `ground_elevation_m 257.477575286...`. [shown]
- Identify Results, DEM: `dem_mosaic_1km 0`, `Band 1 907.984`. [shown]
- Identify Results, aggregate: `gridpoints_heard_multiple — points [2]`, `fid 203833`, `n_flights 8`. [shown]
- Measure dialog: "Cartesian / Ellipsoidal", Ellipsoidal selected, unit "meters". [shown]

Formulas (the creator names the quantities but shows no equations):

- Observer height: z_obs = DEM(lat, lon). [stated] in words; form [inferred] M3-I09
- Plane height: z_ac = alt_ft * 0.3048. [inferred] M3-I10
- Slant distance: d(t) = sqrt(h(t)^2 + (z_ac(t) - z_obs)^2), where h(t) is the horizontal ground distance from observer to the track point at time t. [inferred] M3-I11
- CPA: t_cpa = argmin_t d(t). [inferred] M3-I12
- Delay and delayed CPA time: t_delayed = t_cpa + d(t_cpa) / c. [inferred] M3-I13

Check with shown values: z_ac - z_obs = 4600 * 0.3048 - 257.48 = 1144.6 m. With d = 3364.77 m, h = sqrt(3364.77^2 - 1144.6^2) = 3164 m. The delay is 3364.77 / 343 = 9.8 s. [inferred] M3-I14

## 6. Tools and software

- QGIS: layers panel, Identify Results panel, Measure tool, satellite basemaps (layers named google, bing, carto). [shown]
- A custom spectrogram viewer with a "Selection analysis" panel. The status bar shows "Claude Code". [shown] That it was built with Claude Code is [inferred] M3-I15
- Python for the grid and CPA computation. [stated] (description: "filtered in Python"); that the M3 grid code is Python [inferred] M3-I16
- A DEM. [stated] Source dataset not named. [shown]

## 7. Problems and fixes

- Hearing a plane is not a single moment. The curve lasts almost two minutes. Fix: use the CPA time as the event time. [stated] [00:04:51]
- Sound takes time to travel from plane to listener. Fix: use the delayed CPA time. [stated] [00:05:38]
- Horizontal distance understates the path. Fix: use 3D slant distance. [stated] [00:05:55]
- ADS-B altitude is above sea level. Fix: sample a DEM for ground elevation. [stated] [00:06:07]
- Risk of missing a flight. Fix: a conservative 10 km radius. [stated] [00:05:12]
- Unresolved inconsistency: the worked example states CPA time 22:46:34 and delayed 22:46:46, a 12 s gap. The shown distance 3364.77 m gives about 9.8 s at 343 m/s. At 00:05:32 the creator named 22:46:36 as the CPA point, and 22:46:36 + 9.8 s rounds to 22:46:46. The true CPA is probably near 22:46:36, and 22:46:34 is a misclick or loose wording. [inferred] M3-I17

## 8. Gaps

- Speed of sound value. Best guess: a constant 343 m/s, not temperature- or altitude-dependent. Confidence: medium. [inferred] M3-I18
- CPA search method. Best guess: brute-force minimum of 3D distance over 1 s track points, without sub-second interpolation, since delayed times are whole seconds. Confidence: medium. [inferred] M3-I19
- Delayed time rounding. Best guess: rounded to the nearest second for display; stored as a time string. Confidence: low. [inferred] M3-I20
- Altitude type. Best guess: `alt_ft` is barometric altitude, treated as height above mean sea level without a pressure correction. Confidence: medium. [inferred] M3-I21
- DEM source and resolution. Best guess: a 1 km mosaic of a public DEM such as SRTM or Copernicus GLO-90, resampled. Confidence: low. [inferred] M3-I22
- Grid construction. Best guess: a regular 200 m lattice in a metric projected CRS, clipped to a 10 km buffer of each track line, generated per flight. Confidence: medium. [inferred] M3-I23
- Distance computation. Best guess: geodesic or local-projected horizontal distance combined with height difference; earth curvature ignored at 10 km. Confidence: medium. [inferred] M3-I24
- Multiple passes. A track that loops (00:06:42) can pass a point more than once. Best guess: one global minimum per flight per point, so a second pass is lost. Confidence: low. [inferred] M3-I25
- Test area extent and how it scales to the continental US. Best guess: the shown rectangle is a demo; the full run tiles the US or works per flight. Confidence: low. [inferred] M3-I26
- Grid alignment across flights. Best guess: a shared global 200 m lattice, so points from different flights coincide and can be merged into `gridpoints_heard_multiple`. Confidence: medium. [inferred] M3-I27
- Aggregate time ordering. The shown list is not sorted by time (19:13:28 comes before 18:30:20, and times run past midnight to 01:16:28). Best guess: ordered by flight processing, with UTC times that roll past midnight into Sept 9. Confidence: medium. [inferred] M3-I28
