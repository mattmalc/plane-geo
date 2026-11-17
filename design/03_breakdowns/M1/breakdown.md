# M1 breakdown: Problem setup and finding the Doppler curves

Range: 00:00:17 to 00:02:37. Systems: S2.

## 1. Goal and done criteria

Goal: state the geolocation problem and find the two aircraft Doppler curves in the recording.

- The target is a static security-camera video. Nothing changes visually. [stated] [00:00:17]
- The only known facts are "In continental US" and "Filmed 9/8/26". [shown] [00:00:27] ![](frames/M1_000027.png)
- The evidence is two Doppler curves in the audio. Event 1 is faint. Event 2 is louder and has harmonics. [stated] [00:02:21]

Done when:
- The recording is open in a spectrogram viewer with a band of about 5 to 800 Hz and a long FFT window. [shown] [00:01:43]
- Event 1 is visible near 1250 to 1300 s of the 60:00 recording. [shown] [00:01:52]
- Event 2 is visible near 2100 to 2180 s with harmonics. [shown] [00:02:31]
- Both events are flagged as the inputs for later stages (S2 measurement in later milestones). [stated] [00:02:31]

## 2. Procedure

1. Get the target recording. It is a static camera view of sky and trees. [shown] [00:00:18] ![](frames/M1_000018.png)
   The frame at 00:00:17 is black (cut point). The 00:00:18 frame stands in for that visual moment. [shown]
2. Note the constraints: continental US, filmed 9/8/26. [shown] [00:00:27] ![](frames/M1_000027.png)
3. The video shows a disclaimer card at 00:00:40, not the thunder video. It states the video is an educational OSINT demonstration and that locations used are public property. [shown] ![](frames/M1_000040.png)
4. Contrast with the thunder method. Thunder travels far and penetrates structures but gave about 5 km precision. [stated] [00:00:43]
   - A diagram shows thunder passing through a wall to an ear, and bird song blocked by a wall. [shown] [00:00:45] ![](frames/M1_000045.png)
   - The thunder result is a coarse heat map over the southwest Florida coast in QGIS. [shown] [00:00:50] ![](frames/M1_000050.png)
   - The diagram is repeated with a "?" source in place of the thunder cloud. [shown] [00:00:56] ![](frames/M1_000056.png)
   - The Doppler method's precision is shown as a dense point grid over the same coast, at a much finer scale. [shown] [00:00:59] ![](frames/M1_000059.png)
5. Open the recording waveform. The track is 60:00.000 long. Amplitude stays within about +/-0.006 around 1200 to 1380 s. Nothing is audible. [shown] [00:01:20] ![](frames/M1_000120.png)
6. Select a 4.5 s region and read the Selection analysis panel. 81.9% of energy sits in 0 to 250 Hz. [shown] [00:01:28] ![](frames/M1_000128.png)
7. Switch to the spectrogram at full range, 1k to 8k visible. Bands sit near 4 to 4.5 kHz and 6 to 7 kHz. No curve is visible. [shown] [00:01:31] ![](frames/M1_000131.png) ![](frames/M1_000134.png)
   X axis is time, Y axis is frequency. [stated] [00:01:34]
8. Open Settings. Defaults: window size 2048, Hamming, zero padding 1, linear scale, min 5 Hz, max 8000 Hz. [shown] [00:01:42] ![](frames/M1_000142.png)
9. Set max frequency to 800 Hz. A faint diagonal trace starts to appear near 1260 to 1290 s. [shown] [00:01:43] ![](frames/M1_000143.png)
10. Raise the window size: 2048 to 4096 to 8192 to 16384. The curve sharpens at each step. [shown] [00:01:45] ![](frames/M1_000145.png) ![](frames/M1_000146.png) ![](frames/M1_000149.png) ![](frames/M1_000150.png)
11. Select around event 1 (1247.154 to 1314.672 s). The curve falls from about 500 Hz near 1260 s to about 330 Hz near 1290 s. [shown] [00:01:52] ![](frames/M1_000152.png)
    The creator calls it "a Doppler curve from an aircraft". [stated] [00:01:49]
12. Repeat on a second channel view (CH 2) zoomed out to 1080 to 1320 s. Event 1 is visible. A second faint rising trace near 430 to 470 Hz sits at about 1140 to 1200 s. [shown] [00:01:57] ![](frames/M1_000157.png)
13. Project-scale aside: QGIS shows all flight paths over the US in yellow, a script `v31.py` with Doppler code, and a `dem_mosaic_1km` layer. [shown] [00:02:07] ![](frames/M1_000207.png) ![](frames/M1_000208.png) ![](frames/M1_000209.png)
14. Back in the spectrogram (CH 2, 1240 to 1480 s). Event 1 again. A broadband vertical stripe sits at about 1360 s. [shown] [00:02:12] ![](frames/M1_000212.png)
15. Select event 1 again (1256.662 to 1312.101 s, 55.440 s). [shown] [00:02:20] ![](frames/M1_000220.png)
16. Event 1 in the full recording view, 1220 to 1500 s. [shown] [00:02:23] ![](frames/M1_000223.png)
17. Scroll right. At 1770 to 2060 s no clear Doppler curve shows; a broadband burst sits near 1935 to 1960 s. [shown] [00:02:26] ![](frames/M1_000226.png)
18. Event 2 at about 2100 to 2180 s. It is brighter and has stacked harmonics. [shown] [00:02:31] ![](frames/M1_000231.png)
    "It's a lot louder and you can also see the harmonics on top." [stated] [00:02:25]
19. Zoom out to 1600 to 3400 s. A possible third curve sits near 3040 to 3120 s. The selection there runs 3035.322 to 3116.898 s, then 3007.737 to 3131.389 s. [shown] [00:02:34] ![](frames/M1_000234.png) ![](frames/M1_000236.png)
    The creator says "I think we have one more here" but uses only the first two. [stated] [00:02:31]

## 3. Components

| Item | Value | Tag |
|---|---|---|
| Target date | 9/8/26 (September 8) | [shown] |
| Region | Continental US | [shown] |
| Recording length | 60:00.000 | [shown] |
| Channels | CH 1 and CH 2 visible | [shown] |
| Waveform amplitude | about +/-0.006 full scale near events | [shown] |
| Selection, waveform | 1275.518 to 1280.030 s, 4.512 s | [shown] |
| RMS level | -59.6 dBFS | [shown] |
| Peak level | -48.1 dBFS | [shown] |
| Dominant | 22 Hz | [shown] |
| Crest | 11.5 dB | [shown] |
| Noise floor | -63.2 dBFS | [shown] |
| Centroid | 424 Hz | [shown] |
| ZCR | 2129.8/s | [shown] |
| Band energy | 0-250 81.9%, 250-500 5.7%, 0.5-1k 4.2%, 1-2k 3.1%, 2-4k 0.3%, 4-8k 4.8%, 8k+ 0.0% | [shown] |
| Selection, event 1 wide | 1247.154 to 1314.672 s, 67.518 s; RMS -59.4 dBFS; peak -42.2 dBFS; dominant 26 Hz; crest 17.1 dB; noise floor -62.8 dBFS; centroid 470 Hz; ZCR 2192.2/s | [shown] |
| Selection, event 1 tight | 1256.662 to 1312.101 s, 55.440 s; RMS -59.4 dBFS; peak -42.2 dBFS; noise floor -63.0 dBFS; centroid 444 Hz | [shown] |
| Selection, possible third event | 3007.737 to 3131.389 s, 123.653 s; RMS -55.3 dBFS; peak -32.6 dBFS; dominant 74 Hz; centroid 320 Hz; 0-250 70.8% | [shown] |
| Event 1 curve | about 500 Hz falling to about 330 Hz, about 1258 to 1295 s | [shown] (read off axis ticks) |
| Event 2 fundamental | about 170 Hz falling to about 100 Hz, about 2090 to 2170 s | [shown] (read off axis ticks) |
| Event 2 harmonics | traces near 2x and 3x the fundamental, about 330 to 200 Hz and 430 to 300 Hz | [shown] (read off axis ticks) |
| Event spacing | about 880 s between the visible centers; the project uses 920 s | [inferred] M1-I01 |
| Spectrogram band | 5 to 800 Hz | [shown] |
| FFT window sizes offered | 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768 | [shown] |
| Final window size | 16384 | [shown] |
| Window type | Hamming | [shown] |
| Zero padding factor | 1 | [shown] |
| Frequency scale | Linear | [shown] |
| Palette | Rose | [shown] |
| Gain | 20 dB | [shown] |
| Auto brightness | off | [shown] |
| Code size | over 5,000 lines | [stated] |
| Data files | Parquet, about 50 GB | [stated] |
| DEM | countrywide; QGIS layer `dem_mosaic_1km` | [stated], [shown] |
| Build time | months | [stated] |
| Thunder-method precision | about 5 km | [stated] |

## 4. Systems touched

### S2 Spectrogram measurement
- How it works: load the audio, show a spectrogram, cut the display to 5 to 800 Hz, and raise the FFT window to 16384 for frequency resolution. The faint curve then appears as a falling diagonal line. [shown]
- Inputs: the 60-minute recording. [shown]
- Outputs in M1: two event locations in time, event 1 near 1260 to 1295 s and event 2 near 2090 to 2170 s, with rough frequency ranges. [shown] Fitted velocity, CPA distance, CPA time, and fundamental come in later milestones. [stated] (milestone summary for S2)
- Connections: event times feed S4 (920 s spacing filter) and S6 (scoring against the spectrogram). [inferred] M1-I02
- Code visible in M1 belongs to S3/S5 (`geometry_and_doppler_vec`, `solve_emission_time_vec`, `solve_doppler_factor`). It is shown as B-roll only. [shown]

## 5. Code, configs, formulas, and on-screen text

On-screen text at 00:00:27 [shown]:
```
In continental US
Filmed 9/8/26
```

Disclaimer at 00:00:40 [shown]:
```
Disclaimer: The following is an educational demonstration of
open-source intelligence (OSINT) techniques.

This video is intended to increase awareness of the
data unknowingly contained in recordings and how
unintended information can be ascertained therefrom

Locations used in this video are public property. Respect privacy.
```

Spectrogram Settings panel at 00:01:42 to 00:01:50 [shown]:
```
Default view
  View: Multi-view
Spectrogram display
  Window size: 2048 -> 4096 -> 8192 -> 16384
  Window type: Hamming
  Zero padding factor: 1
  Frequency scale: Linear
Frequency range (display only)
  Min frequency (Hz): 5
  Max frequency (Hz): 8000 -> 800
  [ ] Max follows Nyquist
Amplitude range (waveform)
  [x] Auto (fit each channel)
  Min amplitude: -1
  Max amplitude: 1
Spectrogram appearance
  Palette: Rose
  [ ] Auto brightness
  Gain (dB): 20
```

Code in `scripts/v31.py`, project `Planev2`, Python 3.14, at 00:02:08 [shown]. Lines 623 to 680. Transcribed where legible:
```python
    date_str = target_dt_utc.strftime("%Y-%m-%d")
    rows = fetch_or_load_wind_day(date_str)
    sknt, drct, valid = _nearest_wind_observation(rows, target_dt_utc)
    wind_speed_ms = sknt * KT_TO_MS
    toward_rad = math.radians((drct + 180) % 360)
    east_ms = wind_speed_ms * math.sin(toward_rad)
    north_ms = wind_speed_ms * math.cos(toward_rad)
    log(f"  [{label}] wind: {sknt:.0f}kt from {drct:.0f}° (observed {valid} UTC, target "
        f"{target_dt_utc.strftime('%Y-%m-%d %H:%M:%S')} UTC) -> east={east_ms:+.2f}m/s, north={north_ms:+.2f}m/s")
    return east_ms, north_ms


def geometry_and_doppler_vec(state, cand_lat, cand_lon):
    ac_lat, ac_lon = state["lat"], state["lon"]
    alt_m = state["alt_ft"] * FT_TO_M
    gs_ms = state["gs_kt"] * KT_TO_MS
    vs_ms = state["vs_fpm"] * FPM_TO_MS
    track_deg = state["track_deg"]

    east_m = (ac_lon - cand_lon) * 111320.0 * np.cos(np.radians(ac_lat))
    north_m = (ac_lat - cand_lat) * 111320.0
    up_m = alt_m - get_elevation_scalar(cand_lat, cand_lon)
    dist = np.sqrt(east_m ** 2 + north_m ** 2 + up_m ** 2)
    dist = np.where(dist <= 1e-6, 1e-6, dist)

    vx = gs_ms * np.sin(np.radians(track_deg)) - WIND_EAST_MS
    vy = gs_ms * np.cos(np.radians(track_deg)) - WIND_NORTH_MS
    vz = vs_ms
    ux, uy, uz = east_m / dist, north_m / dist, up_m / dist
    range_rate = vx * ux + vy * uy + vz * uz
    doppler_factor = C_SOUND / (C_SOUND + range_rate)
    return dist, doppler_factor


def solve_emission_time_vec(track_arrs, cand_lat, cand_lon, t_r_arr, iters=6):
    t_e = t_r_arr.copy()
    valid = np.ones(len(t_r_arr), dtype=bool)
    for _ in range(iters):
        state = interpolate_state_vec(track_arrs, t_e)
        valid &= state["valid"]
        dist, _ = geometry_and_doppler_vec(state, cand_lat, cand_lon)
        t_e = t_r_arr - dist / C_SOUND
    return t_e, valid


def solve_doppler_factor(track_arrs, cand_lat, cand_lon, t_recept):
    t_e, valid = solve_emission_time_vec(track_arrs, cand_lat, cand_lon, t_recept)
    state = interpolate_state_vec(track_arrs, t_e)
    valid &= state["valid"]
    _, doppler_factor = geometry_and_doppler_vec(state, cand_lat, cand_lon)
    if valid.sum() < 5:
        return None, None
    frame_idx = np.arange(len(t_recept))[valid]
    return doppler_factor[valid], frame_idx


def compute_dense_doppler_curve(track_arrs, cand_lat, cand_lon, frame_centers_s, point_offset,
                                dt_range, oversample=3):
```
The function name on line 623 is cut off at the top as `compute_wind_vector_for_timestamp(target_utc_s: float, label: str)`. [shown]

Formulas from the code [shown]:
- Flat-earth offset: east = (lon_ac - lon_c) * 111320 * cos(lat_ac); north = (lat_ac - lat_c) * 111320; up = alt_ac - elev(c).
- Slant distance: d = sqrt(east^2 + north^2 + up^2).
- Range rate: r_dot = v . u, with v = air-relative velocity (ground speed minus wind) and u = unit vector observer to aircraft.
- Doppler factor: f_obs / f_src = c / (c + r_dot).
- Emission time, fixed point, 6 iterations: t_e = t_r - d(t_e) / c.

Editor tabs visible [shown]: `v31.py`, `1.1 v8 CRS fix.py`, `1.1b v2 aggregate.py`, `1.2a v9.py`, `1.2a v10.py`, `doppler explorer html drag point and curve.py`, `funnel charts.py`, `spectro measurer v3.py`.

Project files visible include [shown]: `v17.py` to `v31.py`, `v20 - best.py`, `v22 plus elev test.py`, `v23 scoring based...`, `doppler_explorer.html`, `radial_velocity_explor...`, `download DEM.py`, `download flightpaths...`, `all flightlines to gpkg...`, `all flightpaths as gpkg...`, `check jets in outputs.py`, `curve trace v1.py`, `audio measure temp.py`, `audio trim.py`, `event candidate polyli...`, `event_data.py`, `crop vid.py`, `csv check.py`, `3d demo.py`.

QGIS layers at 00:02:09 [shown]: `dem_mosaic_1km`, `all_flight_paths`, `prop_flight_paths`, `single ev`, `post offset pre sil...`, `post silence + offs...`, `13552_candidat...`, `15113_candidate_...`, `data error`, `test area`, `flightpaths`, `event scores`, `1:35:52_candidat...`, `1:21:20_candidat...`, `old`, `th`, `google`, `carto`, `bing`, `norway`.

## 6. Tools and software

- Audio/spectrogram viewer: a dark-theme app with waveform plus spectrogram "Multi-view", a Selection analysis panel, and a Settings panel. Name not shown. The status bar shows "Claude Code", so it is likely a custom tool built with Claude Code. [shown] Name and build: [inferred] M1-I03
- QGIS for maps, with Google, Carto, and Bing basemaps. [shown]
- An IDE with a Project panel and Python 3.14 interpreter "Planev2". Looks like a JetBrains IDE (PyCharm). [shown] IDE identity: [inferred] M1-I04
- Python with NumPy (`np.`). [shown]
- Parquet files. [stated]

## 7. Problems and fixes

- Problem: the signal is inaudible and invisible in the waveform. [stated] [00:01:14] Fix: open a spectrogram. [stated]
- Problem: the full 5 to 8000 Hz spectrogram still shows nothing. [stated] [00:01:35] Fix: cut the display to 5 to 800 Hz. [shown]
- Problem: at 2048 window size the curve is buried in noise. [shown] [00:01:43] Fix: raise the window to 16384 for finer frequency bins. [shown]
- Problem: thunder geolocation only reaches about 5 km. [stated] Fix: use aircraft Doppler curves instead. [stated]

## 8. Gaps

- Sample rate of the recording is not shown. Best guess 16 kHz, since the default max is 8000 Hz and "Max follows Nyquist" is off. Confidence medium. [inferred] M1-I05
- FFT hop or overlap is not shown. Best guess 75% overlap, a common default for Hamming. Confidence low. [inferred] M1-I06
- Frequency resolution at window 16384 is not shown. If the sample rate is 16 kHz, bin width is about 0.98 Hz and the window spans about 1.02 s. Confidence medium. [inferred] M1-I07
- The spectrogram viewer is not named. Best guess: a custom web or Electron tool made with Claude Code. A rebuild can use any viewer that allows a 5 to 800 Hz band and a 16384 window, such as Audacity, Sonic Visualiser, or scipy plus matplotlib. Confidence medium. [inferred] M1-I08
- Which channel to use is not stated. CH 1 and CH 2 both show. Best guess: either works; event 1 appears in CH 2 views. Confidence low. [inferred] M1-I09
- The recording start time of day is not shown here. Event times are offsets into a 60-minute file. A rebuild needs the absolute time later, or must solve for it. Confidence high that it is unknown at this stage. [inferred] M1-I10
- The exact event centers and frequencies are not read out on screen. Values here come from axis ticks and may be off by about 5 s and 20 Hz. Confidence medium. [inferred] M1-I11
- The third possible curve near 3040 to 3120 s is dropped without a stated reason. Best guess: too faint or ambiguous to measure. Confidence low. [inferred] M1-I12
- Wind correction appears in code (`WIND_EAST_MS`, `WIND_NORTH_MS`, `fetch_or_load_wind_day`) but is not described in M1. The wind data source is unknown. Best guess: hourly surface observations (METAR/ASOS, e.g. from the Iowa Environmental Mesonet), since the fields are `sknt`, `drct`, and `valid`. Confidence medium. [inferred] M1-I13
- Constants `C_SOUND`, `KT_TO_MS`, `FT_TO_M`, `FPM_TO_MS` are not shown. Best guess: 343 m/s, 0.514444, 0.3048, 0.00508. Confidence medium for C_SOUND, high for unit factors. [inferred] M1-I14
