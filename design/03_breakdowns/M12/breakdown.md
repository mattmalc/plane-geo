# M12 breakdown: Test countermeasures

Range: 00:26:08 to 00:28:09. Systems: S8, S2.

## 1. Goal and done criteria

Goal: test whether common audio countermeasures remove an aircraft Doppler curve from a recording. [stated]
The four candidates are a high-pass filter, drowning the curve out with louder sound, cuts, and phone-call compression. [stated]
The test for each one is whether the curve is still visible in a spectrogram afterwards. [shown]

Done criteria:
- High-pass test: the curve is invisible after high-pass and MP3 export, then visible again after a gain boost. [shown]
- Masking test: a curve played under speech is visible in the spectrogram of that speech. [shown]
- Phone-call test: a curve played on the sending side of a call is visible in the recording of the receiving phone. [shown]
- A summary list marks which measures fail. [shown] ![](frames/M12_002759.png)

## 2. Procedure

1. Open with the question of protection. [00:26:08] The first frame still shows the earlier spectrogram viewer at 2216.308 s of a 60:00 recording. It holds no countermeasure content. [shown] ![](frames/M12_002613.png)
2. Argue that high-pass filtering removes voice. [00:26:13] Speech in a zoomed Audacity spectrogram fills roughly 100 to 750 Hz. [shown] Doppler curves sit in the same band. [stated] ![](frames/M12_002618.png) ![](frames/M12_002619.png)
3. Load a test recording with Doppler curves in Audacity. [00:26:24] Track "audio", about 4:50 long, log-ish frequency axis 10 to 2900 Hz. Curves are visible between about 70 and 300 Hz. [shown] ![](frames/M12_002628.png)
4. Apply a high-pass filter. [00:26:31] Path: Effect menu > EQ and Filters > High-Pass Filter... [shown] ![](frames/M12_002631.png) ![](frames/M12_002632.png)
5. Check the result. Everything below about 400 to 460 Hz is greyed out and the curves are gone from view. [shown] ![](frames/M12_002634.png) The cutoff value itself is not shown. [inferred] M12-I01
6. Export as MP3. [00:26:35] The Audacity export dialog appears ("How would you like to export?", "Export to computer"). [shown] ![](frames/M12_002635.png)
7. Reopen the MP3. [00:26:37] Track "audio3", two channels, axis 70 to 990 Hz. The band below about 400 Hz is black. The curve looks gone. [shown] ![](frames/M12_002637.png)
8. Boost gain. [00:26:41] Path: Effect menu > Volume and Compression > Amplify... [shown] ![](frames/M12_002641.png) After the boost, diagonal Doppler lines reappear between about 140 and 370 Hz. [shown] ![](frames/M12_002642.png) A selection from about 1:30 to 3:30 and 140 to 370 Hz highlights the recovered curves. [shown] ![](frames/M12_002644.png)
9. Reveal the masking test. [00:26:54] A JBL speaker across the room played a Doppler curve during the previous 15 s of narration. [stated] The Audacity spectrogram of that narration (axis 40 to 290 Hz, time 8 to 43 s) shows a straight descending line from about 100 Hz at 10 s to about 60 Hz at 29 s, under the speech harmonics. [shown] ![](frames/M12_002658.png)
10. Highlight the masked curve with a spectral selection. [00:27:01] ![](frames/M12_002701.png) ![](frames/M12_002702.png)
11. Name cuts as a working measure. [00:27:06] Cuts remove the time offset between events. [stated] The on-screen frame is a long Audacity spectrogram (33:00 to 57:00, 0 to 600 Hz) with several curves; no cut is performed on screen. [shown] ![](frames/M12_002703.png) ![](frames/M12_002706.png)
12. Note that one minute with a known time can still work, and that phone calls give a known time. [00:27:11]–[00:27:22] [stated] Frame at 00:27:22 shows the earlier viewer at about 1336 s. [shown] ![](frames/M12_002722.png)
13. Show why a call might seem to destroy the curve. [00:27:25] A TikTok image lists what the phone activates: echo cancellation, noise gating, voice detection, dynamic compression. "All TERRIBLE for music" has "music" crossed out and "Doppler Curves" written in red. [shown] ![](frames/M12_002725.png)
14. Set up the phone-call test. [00:27:31] Right room: receiving phone on a bed, a handheld microphone pointed at it, cabled to a laptop. [shown] ![](frames/M12_002733.png) Squishmallows cover the phone and mic. [shown] ![](frames/M12_002738.png) Left room: the creator with the sending phone and the JBL speaker. A door separates the rooms. [shown] ![](frames/M12_002744.png)
15. Play the Doppler curve through the JBL, then mute the call. [00:27:43] The call UI shows the mute button highlighted. Overlay text: "im gonna go on mute". [shown] ![](frames/M12_002744.png) ![](frames/M12_002746.png) The curve travels "through the phone and only through the phone". [stated]
16. Inspect the recording. [00:27:46] Track "2026-10-29 17-21-55", about 48 s long, waveform with speech bursts. [shown] ![](frames/M12_002747.png) Spectrogram (axis 100 to 490 Hz) shows a curve falling from about 200 Hz near 3 s to about 175 Hz near 15 s. [shown] ![](frames/M12_002753.png)
17. Point out the gap. [00:27:52] Overlay text: "was a gap in the doppler curve", then "and then when i started talking again". A spectral selection spans about 145 to 200 Hz over about 3 to 35 s. [shown] ![](frames/M12_002756.png) The cause of the gap is not explained. [inferred] M12-I02
18. Summarise. [00:27:56] On-screen list with items 1 and 2 struck through. [shown] ![](frames/M12_002759.png) Suggested measures: cuts and extra noise cancellation. [stated] [00:28:04] Closing frame returns to a long spectrogram. [shown] ![](frames/M12_002806.png)

## 3. Components

- Test recording for high-pass: mono track "audio", about 4:50, curves about 70 to 300 Hz. [shown]
- High-pass cutoff: not shown. Greyed band ends near 400 to 460 Hz. [inferred] M12-I03
- MP3 export: bitrate and settings not shown. [shown] Result reopened as stereo track "audio3". [shown]
- Amplify gain: value not shown. [shown] Spectrogram turns saturated pink-orange after the boost, so the gain was large. [inferred] M12-I04
- Masking test: JBL speaker across the room, about 15 s duration. [stated] Masked curve about 100 Hz to 60 Hz over about 19 s. [shown]
- Phone-call test recording: track "2026-10-29 17-21-55", about 48 s. [shown] Curve about 200 Hz to 175 Hz. [shown]
- Phone-call test rig: two phones, JBL speaker, handheld mic, laptop, Squishmallows, two rooms with a door. [shown]
- Phone processing named on screen: echo cancellation, noise gating, voice detection, dynamic compression. [shown]
- Speech band in the zoomed view: about 100 to 750 Hz. [shown]

## 4. Systems touched

### S8 Countermeasure tests
- How it works: apply a countermeasure to audio that contains a known Doppler curve, then look for the curve in a spectrogram. [shown]
- Inputs: a recording with a curve, or a synthetic curve played from a speaker. [shown] The source of the synthetic curve audio is not shown. [inferred] M12-I05
- Outputs: a pass or fail verdict per countermeasure, summarised in the on-screen list. [shown]
- Connections: depends on S2 to see the curve. Feeds the closing advice of the video. The "known time" point ties to S1, which cuts flights to a time window when recording time is known. [stated]

### S2 Spectrogram measurement
- How it works here: Audacity spectrogram view, zoomed to the curve band, with spectral selection boxes to highlight the curve. [shown]
- Inputs: the processed audio. Outputs: visual confirmation of the curve. [shown]
- No fitting or tracing is done in this milestone. [shown]
- Connections: same view the main pipeline uses for measurement (S2), and S6 scores against such spectrograms. [inferred] M12-I06

## 5. Code, configs, formulas, and on-screen text

No code or formulas appear. [shown]

Menu paths, verbatim [shown]:
- `EQ and Filters > Bass and Treble... | Filter Curve EQ... | Graphic EQ... | High-Pass Filter... | Low-Pass Filter... | Notch Filter... | Shelf Filter...`
- `Volume and Compression > Amplify... | Auto Duck... | Compressor... | Limiter... | Loudness Normalization... | Normalize...`
- Top of menu: `Repeat High-Pass Filter`, later `Repeat Amplify`.

Export dialog, verbatim [shown]: "How would you like to export?" / "Share to audio.com" / "On your computer" / "Export MP3s, WAVs, FLACs and other formats to your computer." / "Export to computer".

TikTok image, verbatim [shown]: "Even on loudspeaker or regular audio:" / "The phone activates:" / "Echo cancellation" / "Noise gating" / "Voice detection" / "Dynamic compression" / "All great for voice." / "All TERRIBLE for ~~music~~." with handwritten "Doppler Curves".

Overlay captions [shown]: "right now you're listening through", "im in a different room", "im gonna go on mute", "through the phone", "was a gap in the doppler curve", "and then when i started talking again".

Summary list [shown]:
```
1. ~~High pass filter~~
2. ~~Drown out with louder sounds~~
3. Compression / lossy recording
```

## 6. Tools and software

- Audacity: spectrogram view, High-Pass Filter, Amplify, MP3 export, spectral selection. [shown]
- A custom dark spectrogram viewer with a seconds timeline and "Multi-view", seen in transition frames. Its status bar reads "Claude Code". [shown]
- JBL Bluetooth speaker. [stated]
- Two smartphones on a voice call; iPhone-style call UI with mute. [shown]
- Handheld dynamic mic into a laptop. [shown]
- Squishmallows as acoustic cover. [stated]

## 7. Problems and fixes

- Problem: high-pass filtering would remove voice, since curves share the voice band. [stated] No fix; rejected.
- Problem: high-pass plus MP3 export only hides the curve. Amplify brings it back. [shown] No fix; rejected.
- Problem: louder foreground sound does not mask the curve. [shown] No fix; rejected.
- Problem: leakage from the JBL to the receiving phone would spoil the call test. Fix: separate rooms and Squishmallows over the receiving phone. [stated]
- Problem: the phone call does not remove the curve. It survives compression and noise reduction. [stated] [shown]
- Working measures: cuts, which break the inter-event time offset, and extra noise cancellation. [stated] Neither is demonstrated. [shown]

## 8. Gaps

- High-pass cutoff frequency and roll-off. Best guess: about 400 Hz, default Audacity roll-off. Confidence: medium. [inferred] M12-I07
- Amplify gain in dB. Best guess: +30 to +50 dB, allow clipping on. Confidence: low. [inferred] M12-I08
- Source of the synthetic Doppler curve played on the JBL. Best guess: a tone generated from the S5 forward model or a clip of a real flyover. Confidence: low. [inferred] M12-I09
- Whether the spectrograms here use the same view settings as S2/S6 (window size, scale). Best guess: Audacity defaults with a zoomed band, not the S6 scorer. Confidence: medium. [inferred] M12-I10
- Cause of the gap in the phone-call curve. Best guess: muting or voice-activity gating suppressed the curve while no one spoke, and it returned when speech resumed. Confidence: low. [inferred] M12-I11
- MP3 bitrate and encoder settings. Best guess: Audacity default, 128 to 192 kbps. Confidence: low. [inferred] M12-I12
- Phone codec and network (cellular, VoLTE, FaceTime audio). Best guess: standard iPhone cellular or FaceTime audio call. Confidence: low. [inferred] M12-I13
- Whether "extra noise cancellation" defeats the curve. It is suggested but not tested. Best guess: aggressive broadband denoise lowers but may not remove the curve. Confidence: low. [inferred] M12-I14
- How much audio a cut must remove to defeat the method. Best guess: any cut that destroys the 920 s offset between two events; a single minute with a known time can still work. Confidence: medium. [inferred] M12-I15
