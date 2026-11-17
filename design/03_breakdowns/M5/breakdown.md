# M5 breakdown: measure speed, slant distance, and CPA time from each Doppler curve

Range: 00:08:21 to 00:10:38. System: S2.

## 1. Goal and done criteria

Goal: fit an ideal constant-velocity Doppler curve over each flyover event in the spectrogram. Read off plane speed, CPA slant distance, CPA time, and fundamental frequency. [stated]

The point is to tighten the M4 filter. M4 kept points that heard one aircraft and then another 920 s later. M5 adds a speed and a CPA distance to each event. [stated] [00:09:20]

Done means:
- Each of the two events has a velocity range and a CPA slant distance range. [stated] [00:10:31]
- The ranges are generous, so the true value is not filtered out. [stated] [00:09:56]
- CPA time is known only to within a couple of seconds. [stated] [00:10:16]
- Final ranges shown on screen: event 1 is 130-154 m/s and 4300-7800 m away at CPA. Event 2 is 88-110 m/s and 1390-4690 m away at CPA. Events are 920 s apart. [shown] [00:10:35] ![](frames/M5_001035.png)

## 2. Procedure

1. Start from the full recording spectrogram (60:00 file, 5-800 Hz), where the faint Doppler curves sit below about 300 Hz. [shown] [00:08:38] ![](frames/M5_000838.png) Then build intuition with two comparison clips. Play both. Clip 2 sounds faster because its frequency drop is larger. [stated] [00:08:38]-[00:08:49] ![](frames/M5_000839.png) ![](frames/M5_000843.png) ![](frames/M5_000848.png)
2. Show the two clips side by side with green brackets marking each drop. Clip 1's drop is small, about 60 Hz on each of two harmonics. Clip 2's drop is large, about 720 Hz down to about 470 Hz. [shown] [00:08:49] ![](frames/M5_000849.png) Hz values are read off the bracket positions against the axis. [inferred] M5-I01
3. State the model. Assume linear constant velocity. Velocity sets the size of the drop. CPA slant distance sets how fast the drop happens. [stated] [00:08:58]-[00:09:03]
4. Open the "Doppler Curve Fit" tool on the event window 01:50:30 to 01:52:15. It has four sliders (f0, v, d, t0) and a red model curve over the spectrogram. [shown] [00:08:57] ![](frames/M5_000857.png)
5. Demonstrate the sliders. At v = 62 m/s and d = 390 m the curve is a sharp step. [shown] [00:09:03] ![](frames/M5_000903.png) Dropping d to 95 m makes the step nearly vertical. [shown] [00:09:08] ![](frames/M5_000908.png)
6. Set a plausible fit: f0 131.5 Hz, v 106.5 m/s, d 3130 m, t0 1:51:15.90. The red curve now follows the faint white trace. [shown] [00:09:12] ![](frames/M5_000912.png) ![](frames/M5_000914.png)
7. Show the 920 s diagram and explain that each event now carries a speed and a distance. [stated] [00:09:20]-[00:09:36] ![](frames/M5_000920.png) ![](frames/M5_000936.png) ![](frames/M5_000939.png)
8. Measure one curve. Move v: the drop grows. [shown] [00:09:41] ![](frames/M5_000940.png) ![](frames/M5_000941.png) ![](frames/M5_000942.png) Move d: the slope changes. At d = 2215 m the curve is too steep. At d = 4295 m it is shallower. [shown] [00:09:46]-[00:09:53] ![](frames/M5_000946.png) ![](frames/M5_000953.png)
9. Note the misfit. The right-hand (receding) side matches an ideal curve. The left-hand (approaching) side does not. The creator says this matters later. [stated] [00:09:51] ![](frames/M5_000953.png)
10. Take a generous velocity range. Try 125 m/s ([shown] [00:10:03] ![](frames/M5_001003.png)). A decent right-side fit is 100 m/s at d 2955 m. [shown] [00:10:06] ![](frames/M5_001006.png) At 69.5 m/s the curve clearly misses the trace. [shown] [00:10:13] ![](frames/M5_001013.png) "Can't confidently say ... exactly 100, but ... pretty sure it wasn't going 70." [stated]
11. Adjust CPA time. The creator says "best match 151.15. I'll move it to 151.13." [stated] [00:10:20] On screen t0 steps 1:51:15.90 to 1:51:14.90 to 1:51:13.90 to 1:51:12.90, with v 112 m/s and d 3460 m. [shown] [00:10:18]-[00:10:30] ![](frames/M5_001018.png) ![](frames/M5_001020.png) ![](frames/M5_001024.png)
12. Slide f0 up to compensate: 131.5 Hz to 133.5 Hz. [shown] [00:10:24]-[00:10:30] ![](frames/M5_001030.png) "That could work." CPA time stays uncertain to about a second or two. [stated]
13. Take snapshots in the tool. The log reads "2 snapshot(s) logged" from 10:15 on. [shown] ![](frames/M5_001018.png) The log header reads "MIN/MAX auto-calculated, BEST = midpoint". [shown] So the snapshots likely bracket the range ends and the tool reports min, max, and midpoint. [inferred] M5-I02
14. Repeat for event 1 and event 2. Record the ranges. [stated] [00:10:31] ![](frames/M5_001035.png)

## 3. Components

| Item | Value | Tag |
|---|---|---|
| Comparison clip 1 length | 0:09.079 | [shown] 000839 |
| Comparison clip 2 length | 1:51.061 | [shown] 000843 |
| Comparison spectrogram band | 5 to 800 Hz | [shown] 000839 |
| Overview recording length | 60:00.000 | [shown] 000838 |
| Overview spectrogram band | 5 to 800 Hz (cursor at 2306.617 s) | [shown] 000838 |
| 920 s diagram spectrogram | 5 to 400 Hz, x axis about 2050-3150 s, cursor 2585.500 s | [shown] 001035 |
| Fit window | 01:50:30 to 01:52:15 (105 s) | [shown] 000857 |
| Fit plot frequency axis | about 90 to 215 Hz | [shown] 000857 |
| Fit plot colour scale | 0 to -80 dB | [shown] 000857 |
| Hover readout | x 6,679.823, y 134.5833, z -24.64252 | [shown] 000953 |
| Fit x axis unit | seconds from the start of the recording (6679.8 s = 1:51:19.8) | [inferred] M5-I03 |
| Speed of sound in tool | 343 m/s, back-solved from readouts | [inferred] M5-I04 |
| Event 1 range | 130-154 m/s, 4300-7800 m at CPA | [shown] 001035 |
| Event 2 range | 88-110 m/s, 1390-4690 m at CPA | [shown] 001035 |
| Event separation | 920 s | [shown] 000920 |

Slider settings read off screen:

| Frame | f0 (Hz) | v (m/s) | d (m) | t0 | f_pre (Hz) | f_post (Hz) | max RoC (Hz/s) |
|---|---|---|---|---|---|---|---|
| 000857 / 000903 | 133.00 | 62.00 | 390.0 | 1:51:15.90 | 162.35 | 112.64 | 3.822 |
| 000908 | 133.00 | 60.00 | 95.0 | 1:51:15.90 | 161.20 | 113.20 | 14.694 |
| 000912 | 131.50 | 106.50 | 3130.0 | 1:51:15.90 | 190.72 | 100.34 | 1.389 |
| 000942 | 131.50 | 110.50 | 3130.0 | 1:51:15.90 | 194.00 | 99.46 | 1.496 |
| 000946 | 131.50 | 117.00 | 2215.0 | 1:51:15.90 | 199.58 | 98.05 | 2.369 |
| 000953 | 131.50 | 117.00 | 4295.0 | 1:51:15.90 | 199.58 | 98.05 | 1.222 |
| 001003 | 131.50 | 125.00 | 4295.0 | 1:51:15.90 | 206.90 | 96.38 | 1.395 |
| 001006 | 130.50 | 100.00 | 2955.0 | 1:51:15.40 | 184.20 | 101.04 | 1.288 |
| 001013 | 130.50 | 69.50 | 2290.0 | 1:51:15.40 | 163.66 | 108.51 | 0.803 |
| 001018 | 131.50 | 112.00 | 3460.0 | 1:51:13.90 | 195.26 | 99.13 | 1.390 |
| 001020 | 131.50 | 112.00 | 3460.0 | 1:51:14.80 | 195.26 | 99.13 | 1.390 |
| 001024 | 131.50 | 112.00 | 3460.0 | 1:51:12.90 | 195.26 | 99.13 | 1.390 |
| 001030 | 133.50 | 112.00 | 3460.0 | 1:51:12.90 | 198.23 | 100.64 | 1.411 |

All rows are [shown].

## 4. Systems touched

**S2 Spectrogram measurement.**
- How it works: a zoomed spectrogram of one event window is overlaid with an ideal constant-velocity Doppler curve. Four sliders set f0, v, d, and t0. The tool prints the approach and recede asymptotes and the peak rate of change. [shown] ![](frames/M5_000857.png)
- Inputs: the event audio window and a user's slider settings. [shown]
- Outputs: per-event ranges for velocity and CPA slant distance, plus a CPA time and f0 estimate. [stated] The snapshot log gives MIN/MAX/BEST. [shown]
- Connections: the velocity ranges feed the S1 speed filter on flight segments, shown right after at 00:10:38. [stated] The slant distance ranges feed S4, which lays the candidate grid only at the measured distance. [stated] [00:10:59] CPA time and f0 feed S6 as starting values. S6 sweeps both to absorb this measurement error. [inferred] M5-I05 The left-side misfit is flagged for later. [stated] Which later system uses it is not said here. [inferred] M5-I06

## 5. Code, configs, formulas, and on-screen text

On-screen text, verbatim:
- `Doppler Curve Fit -- 01:50:30 to 01:52:15` [shown]
- Slider labels: `f0 (fundamental freq)`, `v (plane speed)`, `d (slant distance)`, `t0 (CPA time)` [shown]
- Readouts: `f_pre (approach):`, `f_post (recede):`, `max RoC:` [shown]
- Plot axes: `frequency (Hz)`, `elapsed time (HH:MM:SS)`, colour bar `dB` [shown]
- `Snapshot log -- MIN/MAX auto-calculated, BEST = midpoint` with buttons `Take snapshot`, `Clear log`, and status `no snapshots yet` / `2 snapshot(s) logged` [shown]
- Diagram: `920 sec`, `130-154m/s`, `4300-7800m away at CPA`, `88-110m/s`, `1390-4690m away at CPA` [shown]

Formulas. None are shown on screen. These reproduce every readout in the table above, with c = 343 m/s: [inferred] M5-I07

```
f_pre  = f0 * c / (c - v)          # approach asymptote
f_post = f0 * c / (c + v)          # recede asymptote
maxRoC = f0 * v^2 / (c * d)        # |df/dt| at CPA
```

Check: f0 133, v 62, d 390 gives 162.35, 112.64, 3.822. f0 131.5, v 112, d 3460 gives 195.26, 99.13, 1.390. Both match the screen.

Model curve over time, constant-velocity straight-line pass: [inferred] M5-I08

```
r(t)   = sqrt(d^2 + (v*(t - t0))^2)
v_r(t) = -v^2 (t - t0) / r(t)              # radial velocity, positive = approaching
f(t)   = f0 * c / (c - v_r(t))
```

Whether the tool uses emission time (retarded time) or plain receive time is not shown. [inferred] M5-I09

## 6. Tools and software

- A desktop audio viewer with waveform and spectrogram per channel (CH 1, CH 2), Mute/Solo, and Multi-view. A "Claude Code" label sits in its status bar. [shown] ![](frames/M5_000839.png)
- A custom "Doppler Curve Fit" page. It has a Plotly-style toolbar (camera, zoom, pan, reset icons) and hover readouts. [shown] ![](frames/M5_001006.png) It is likely a Python Plotly or Dash app. [inferred] M5-I10
- A slide editor for the 920 s diagram. Frame 000936 shows the text "88-110m/s" selected mid-edit. [shown] ![](frames/M5_000936.png)

## 7. Problems and fixes

- Left side of the curve does not fit an ideal Doppler curve. Fix for now: take a generous velocity range so nothing true is filtered out. The issue returns later. [stated] [00:09:51]-[00:10:01]
- Velocity is not precise. 100 m/s fits the right side. 70 m/s is clearly wrong. Fix: record a range, not a value. [stated] [00:10:06]
- CPA time has a couple of seconds of error, and it trades off against f0. Moving t0 earlier and raising f0 from 131.5 to 133.5 Hz still fits. Fix: accept the uncertainty and carry it forward. [stated] [shown] [00:10:16]-[00:10:31]
- The trace is faint against noise at -40 to -50 dB. [shown] ![](frames/M5_000914.png)

## 8. Gaps

- [inferred] M5-I11 Which event is demonstrated. The milestone summary calls it event 1. The demo values (100-117 m/s, 2955-4295 m) sit inside the event 2 range (88-110 m/s, 1390-4690 m), not event 1's (130-154 m/s, 4300-7800 m). Best guess: the demo is event 2, or the event 1 range was widened after the left-side issue. Confidence: low.
- [inferred] M5-I12 Time base. The fit tool shows 01:50:30-01:52:15 (about 6630-6735 s). The overview diagram puts the events near 2160 s and 3080 s of a 60:00 file. Best guess: the fit tool indexes a longer original recording and the overview is a cropped clip. Confidence: low.
- [inferred] M5-I13 How ranges are set. Best guess: snapshot the loosest acceptable fit at each end, and the tool takes MIN/MAX of the snapshot values with BEST as midpoint. Confidence: medium.
- [inferred] M5-I14 Spectrogram settings in the fit tool (FFT size, hop, window) are not shown. Best guess: 105 s window at about 0.1-0.25 Hz bin width, so a long FFT (about 4-8 s) with heavy overlap. Confidence: low.
- [inferred] M5-I15 Slider ranges and steps. Best guess from readouts: f0 step 0.5 Hz, v step 0.5 m/s, d step 5 m, t0 step 0.1 s. Ranges not shown. Confidence: medium.
- [inferred] M5-I16 Ranges for t0 and f0 per event are not shown. Best guess: about plus or minus 2 s on t0 and plus or minus 2 Hz on f0. Confidence: medium.
- [inferred] M5-I17 Speed of sound and atmosphere. Readouts fit c = 343 m/s, a 20 C standard. No wind or temperature correction is shown. Confidence: high for 343, medium that nothing else is applied.
- [inferred] M5-I18 Whether f0 is the blade-pass fundamental or a harmonic is not said. The trace sits at about 100-200 Hz, consistent with a propeller blade-pass tone. Confidence: medium.
