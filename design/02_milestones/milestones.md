# Milestones and systems

A geolocation investigation that finds where a security-camera recording was made using only aircraft Doppler curves in its audio. The only known facts are the date, September 8, and that it was filmed somewhere in the continental US. The recording holds two faint propeller-plane Doppler curves 920 seconds apart and no other aircraft between them. The creator downloads a day of ADS-B flight data for the continental US, drops known jet types, and lays candidate observer points on a grid around each flight. CPA is the closest point of approach. For each point he computes the delayed CPA time, when the CPA sound reaches the observer, from the 3D slant distance. A DEM gives ground elevation and the speed of sound gives the delay. Speed, slant distance, CPA time, and fundamental frequency measured from each curve, plus a silence constraint between the events, cut the candidates to about 15,000. He then models the exact curve each candidate would hear from the radial velocity at emission time, scores it against the spectrogram with a locked two-event method on a 100 m grid, and ranks the best point per flight pair. A separate run on a one-minute clip with a known time ranks the same coordinate first, and Street View confirms the camera. The video ends by testing countermeasures. The description states that the code and tools are not released.

The intro runs from 00:00:00 to 00:00:17 and is the hook. The outro runs from 00:28:09 to 00:29:12 and is the wrap-up. The video has no sponsor segment and no YouTube chapters.

## Systems

| ID | Name | Description |
| --- | --- | --- |
| S1 | ADS-B ingest and aircraft filtering | Downloads every flight over the continental US for the target day with a Python scraping package, keeping whole flight paths with position, altitude, speed, timestamp, and type code. Drops known jet types using an ICAO type-code lookup table. Later cuts flight segments to the measured velocity range and, when the recording time is known, to that time window. |
| S2 | Spectrogram measurement | Finds the faint Doppler curves by zooming into the right frequency band at high resolution. Fits an ideal constant-velocity Doppler curve to each event and records generous ranges for velocity, CPA slant distance, CPA time in the audio, and fundamental frequency. Traces a very faint curve as a line. |
| S3 | Acoustic geometry and propagation model | Finds each observer's CPA to a flight and the 3D slant distance, using ADS-B altitude above sea level and DEM ground elevation. Converts distance to sound travel delay, which turns CPA time into delayed CPA time and gives the emission time the Doppler model needs. |
| S4 | Candidate grid and constraint filters | Lays observer points on a 200 m grid, first out to 10 km from each track and later only at the measured slant distance. Keeps points that hear two flights 920 seconds apart, within about 5 seconds, at the measured speeds and distances, and that hear no other flight between the two events. |
| S5 | Doppler curve forward model | For each candidate point and flight, computes the frequency the observer would hear over time. Each time step uses the radial velocity at the moment the sound was emitted, taken from interpolated ADS-B, in the Doppler equation with the measured fundamental frequency. |
| S6 | Spectrogram scoring and ranking | Scores each modelled curve by the spectrogram brightness it covers, or by distance to a traced line. Sweeps CPA time offset and fundamental frequency for event 1, locks event 2's offset to the flight geometry, refines survivors to a 100 m grid, and ranks the best point per flight pair. |
| S7 | Map review and ground-truth confirmation | Shows scored points and per-flight heat maps in QGIS, then checks the top coordinate in Google Maps Street View against the source footage. |
| S8 | Countermeasure tests | Tests whether high-pass filtering, masking noise, cuts, and phone-call compression remove the Doppler signal, by looking for the curve in the spectrogram afterwards. |

## Milestones

| ID | Start | End | Title | Systems | Summary |
| --- | --- | --- | --- | --- | --- |
| M1 | 00:00:17 | 00:02:37 | Problem setup and finding the Doppler curves | S2 Spectrogram measurement | The target is a security-camera video in which nothing changes visually. The only facts given are the date, September 8, and that it was filmed in the continental US. A previous thunder-based method reached about 5 km precision. Two audio sections play and the signal is inaudible. In a spectrogram, with time on x and frequency on y, it only appears after zooming into the right frequency band and raising the resolution. It is a Doppler curve from an aircraft. A second, louder curve with harmonics follows later, and these two curves are the evidence for the search. The creator states the project took months and over 5,000 lines of code, with 50 GB Parquet files, 3D physics modelling, and countrywide DEMs. |
| M2 | 00:02:37 | 00:04:14 | Download ADS-B data and keep propeller aircraft | S1 ADS-B ingest and aircraft filtering | The first idea is to keep only places that heard a plane and then another plane 920 seconds later. ADS-B data gives nearly every aircraft's position, speed, and altitude. A paid API exists, but the creator ran a Python scraping package for a few hours to get every flight over the continental US on September 8. The package downloads whole flight paths, so tracks reach Hawaii and other countries. Played with boosted frequencies, the louder curve sounds like a propeller plane. The ADS-B type code does not say propeller or jet, so he used a lookup table that does. The table has gaps, so he removed known jet types rather than keeping known propeller types. |
| M3 | 00:04:14 | 00:07:04 | Grid candidate points and compute delayed CPA times | S3 Acoustic geometry and propagation model, S4 Candidate grid and constraint filters | This step is shown on a small test area. Each ADS-B point of a flight has coordinates, altitude, and a timestamp. The creator lays a 200 m grid of observer points within 10 km of the flight path, a conservative limit for hearing a plane. Hearing a plane spans almost two minutes, so the event time is the CPA, which he calls closest point of arrival, when the plane is nearest and loudest. The time that matters is the delayed CPA time, when the CPA sound reaches the observer. The delay uses the 3D slant distance. ADS-B altitude is above sea level, so a DEM gives each grid point's ground elevation. In the worked example the CPA time is 22:46:34 and the delayed CPA time is 22:46:46. Repeating this for every flight gives each grid point a list of flight IDs and delayed CPA times. |
| M4 | 00:07:04 | 00:08:21 | Filter grid points by the 920-second offset | S4 Candidate grid and constraint filters | For each grid point the creator checks whether any two delayed CPA times sit 920 seconds apart. The window allows about 5 seconds either way, because where the centre of a curve is measured varies. About 35,000 points pass in the test area, which is under 0.05% of the continental US land area. A football-field comparison makes the point that this filter alone cannot search the whole country. |
| M5 | 00:08:21 | 00:10:38 | Measure speed, slant distance, and CPA time from each Doppler curve | S2 Spectrogram measurement | Two comparison clips show that a larger frequency drop means a faster object. With constant linear velocity, velocity sets the size of the drop and CPA slant distance sets how quickly it happens. The creator fits an ideal Doppler curve over each event on the spectrogram. Event 1 fits on the right side but not the left, which matters later. He records generous ranges instead of single values. The right side fits at about 100 m/s, and 70 m/s clearly does not. CPA time keeps a few seconds of error, with a best match at 151.15 nudged to 151.13 after sliding the fundamental frequency up. The output is a measurement range for each event. |
| M6 | 00:10:38 | 00:13:35 | Apply speed, slant-distance, and silence filters | S1 ADS-B ingest and aircraft filtering, S3 Acoustic geometry and propagation model, S4 Candidate grid and constraint filters | Flight segments are cut to the event 1 velocity range, drawn green, and the event 2 range, drawn pink. Candidate points now sit only at the measured slant distance from each segment, not across the full 10 km grid. A point passes if it hears a green segment and then a pink segment 920 seconds later at the right distances. About 73,000 points pass, mostly in clusters at airports where traffic is dense. The recording has no other aircraft for almost 15 minutes between the events, so a silence filter removes any point that would have heard a flight in between. The thresholds are shown on screen and are conservative. About 70,000 points drop to 15,000. The creator notes that this uses up everything the simple spectrogram measurements can give. |
| M7 | 00:13:35 | 00:16:45 | Forward-model the Doppler curve from real flight geometry | S5 Doppler curve forward model | The measured curves are not ideal because planes change heading, speed, and altitude. Several geometries can produce the same variation, so the spectrogram cannot be inverted. Instead the creator models the exact curve each candidate point would hear from each flight's real ADS-B track and looks for the match. The heard frequency depends on radial velocity, the part of the plane's velocity toward or away from the observer. Head-on it equals the plane's speed, side-on it is zero and there is no shift. The Doppler equation takes the speed of sound c, the radial velocity v_r, and the measured fundamental frequency f0. In the worked example v_r is 0 at CPA, 7:12:30, giving 130 Hz, and 62.7 at 7:12:35, giving 109.9 Hz. These numbers fit f = f0 * c / (c + v_r) with c = 343 m/s for a receding source, which is inferred and not stated. Repeating this per time step gives a curve. |
| M8 | 00:16:45 | 00:18:10 | Correct the model for sound travel time | S3 Acoustic geometry and propagation model, S5 Doppler curve forward model | Using the radial velocity at the hearing time is wrong and would make the search fail. The frequency heard at time t comes from the plane's velocity when it emitted the sound heard at t. So for each time step the model finds where the plane was when it emitted that sound, takes the radial velocity there, and applies the Doppler equation. The result is a different curve shape, not the naive curve shifted later. On the real spectrogram the emission-time curve matches and the naive curve does not. The model runs for every candidate point and every flight. |
| M9 | 00:18:10 | 00:20:59 | Score modelled curves with locked two-event scoring | S6 Spectrogram scoring and ranking | Each modelled curve is drawn on the spectrogram and scored by summing the brightness values it covers. Fundamental frequency and CPA time both come from measurements, so both carry error. Event 1 is placed by putting its modelled delayed CPA at the measured CPA timestamp in the audio. The scorer then sweeps a few seconds of time offset and a range of fundamental frequency and keeps the best combination. Event 2 gets its own fundamental-frequency sweep, but its time offset from event 1 is locked to what the flight geometry predicts, so a bad event 2 placement counts against the candidate. The scoring is sharp enough that on the 200 m grid the true point could sit up to 141 m away and score badly. So the survivors are resampled to 100 m, about 30,000 to 40,000 points. This is expensive, which is why the earlier filters matter. |
| M10 | 00:20:59 | 00:22:41 | Rank candidates by flight pair and inspect the top hits | S6 Spectrogram scoring and ranking, S7 Map review and ground-truth confirmation | Each candidate has an event 1 score and an event 2 score, shown as a scatter plot where the top right is best. No single point stands out at first. Grouping by flight pair and keeping the best point per pair leaves one clear leader at 20.48, whose modelled curves cover both observed curves. The second best, about 15, is close on event 1 but badly off on event 2, and the third is worse. In QGIS the creator views the scored points, then reruns at finer resolution for only the winning flights and shows heat maps for event 1, event 2, and both combined. |
| M11 | 00:22:41 | 00:26:08 | Confirm with a one-minute known-time clip and Street View | S1 ADS-B ingest and aircraft filtering, S2 Spectrogram measurement, S5 Doppler curve forward model, S6 Spectrogram scoring and ranking, S7 Map review and ground-truth confirmation | A second test uses only the first, inaudible curve, one minute of audio, with a known time of 8:37 PM UTC and the whole continental US as the search area. The same spectrogram measurement gives velocity bounds, and only flight segments at that time are kept. With one event the scores form a histogram, not a scatter plot. The curve is too faint for brightness scoring, so the creator traces it with a line and scores each modelled curve by its distance to that line. The top point matches, at the same coordinates the two-event search found, 40.87, -73.5. He generalises that a search needs either several events or a tight time, and that a city-sized area, about 0.01% of US land, allows much looser time bounds. He then zooms to the heat-map centre in QGIS, which sits at the edge of water, opens the coordinate in Google Maps, and matches a V-shaped tree line in Street View. Zooming out shows the security camera on a pole. |
| M12 | 00:26:08 | 00:28:09 | Test countermeasures | S8 Countermeasure tests, S2 Spectrogram measurement | A high-pass filter fails for two reasons. The Doppler curves sit in the same band as the human voice, and after high-passing, exporting to MP3, and boosting all frequencies, the curve comes back. Masking fails too, because a JBL speaker across the room had been playing a Doppler curve under the last 15 seconds of speech. Cutting the audio removes the offset between events, but one minute with a known time can still work, and phone calls give known times. In a phone-call test the JBL speaker plays a Doppler curve in another room, and the receiving phone sits under Squishmallows to block leakage. The curve survives the call's compression and noise reduction. He points out a gap in the curve around when he starts talking again, and the transcript does not make the cause clear. His suggested measures are cuts and extra noise cancellation. |

## Parts, tools, and software

| ID | Item |
| --- | --- |
| M1 | Source recording, a static security-camera video filmed September 8 in the continental US |
| M1 | Spectrogram viewer with frequency zoom and resolution control, not named |
| M1 | Code base of over 5,000 lines, stated |
| M1 | Parquet files of about 50 GB, stated |
| M1 | Countrywide DEMs, stated |
| M2 | ADS-B data with position, speed, altitude, timestamp, and type code |
| M2 | Paid ADS-B API, mentioned and not used |
| M2 | Python package that scrapes ADS-B data, not named |
| M2 | ICAO type-code lookup table marking propeller or jet |
| M2 | Audio frequency boost to make the propeller sound audible |
| M2 | Map view of flight tracks, tool not named |
| M3 | ADS-B track points with coordinates, altitude, and timestamp |
| M3 | 200 m grid of candidate observer points |
| M3 | 10 km radius around each flight path |
| M3 | DEM for ground elevation |
| M3 | Speed of sound for the propagation delay |
| M4 | Per-point list of flight IDs and delayed CPA times |
| M4 | 920 s offset window with about 5 s tolerance either way |
| M4 | Test area under 0.05% of continental US land area |
| M5 | Spectrogram with an adjustable ideal Doppler curve overlay for velocity, slant distance, CPA time, and fundamental frequency |
| M5 | Two comparison audio clips at different speeds |
| M6 | Flight segments filtered by event 1 and event 2 velocity ranges |
| M6 | Candidate points placed at the measured slant distance |
| M6 | Silence filter with thresholds shown on screen |
| M7 | Interpolated ADS-B flight track |
| M7 | Doppler equation with speed of sound c, radial velocity v_r, and fundamental frequency f0 |
| M7 | Radial velocity diagram |
| M8 | Emission-time solve for each time step |
| M8 | Spectrogram overlay comparing the naive and emission-time curves |
| M9 | Spectrogram brightness sum along each modelled curve |
| M9 | Sweep over CPA time offset and fundamental frequency |
| M9 | Locked two-event scoring |
| M9 | 100 m resampling of surviving candidates |
| M10 | Scatter plot of event 1 against event 2 scores |
| M10 | Grouping by flight pair |
| M10 | Spectrogram overlays of modelled curves |
| M10 | QGIS |
| M10 | Fine-resolution heat maps per flight |
| M11 | One-minute clip with a known time, 8:37 PM UTC |
| M11 | Flight segments filtered to that time |
| M11 | Score histogram |
| M11 | Traced line over the faint curve, used for distance scoring |
| M11 | QGIS |
| M11 | Google Maps and Street View |
| M12 | High-pass filter in an audio editor, not named |
| M12 | MP3 export |
| M12 | Gain boost across all frequencies |
| M12 | JBL speaker playing a Doppler curve |
| M12 | Two phones on a call |
| M12 | Squishmallows covering the receiving phone |

## Visual moments

| ID | Time | Reason |
| --- | --- | --- |
| M1 | 00:00:17 | Target security-camera footage on screen. |
| M1 | 00:00:27 | The only known facts, date and continental US, likely as on-screen text. |
| M1 | 00:00:40 | Reference to the earlier thunder geolocation video. |
| M1 | 00:00:50 | Thunder method's 5 km precision, likely on a map. |
| M1 | 00:00:59 | Precision of the Doppler method shown for comparison. |
| M1 | 00:01:20 | Two audio sections playing, with no audible plane. |
| M1 | 00:01:31 | Recording opened in a spectrogram at full frequency range. |
| M1 | 00:01:34 | Spectrogram axes explained. |
| M1 | 00:01:43 | Zoom into the frequency band that holds the curve. |
| M1 | 00:01:45 | Higher resolution reveals the faint curve. |
| M1 | 00:01:49 | First Doppler curve visible. |
| M1 | 00:02:07 | Project-scale claims, likely over B-roll of data and DEMs. |
| M1 | 00:02:23 | Event 1 curve in the full recording. |
| M1 | 00:02:26 | Event 2 curve, louder, with harmonics above it. |
| M1 | 00:02:31 | Zoomed-out view with a possible third curve. |
| M2 | 00:02:42 | ADS-B introduced, likely with a flight-tracking visual. |
| M2 | 00:02:47 | ADS-B fields listed. |
| M2 | 00:02:56 | First search idea, a plane heard and another 920 s later. |
| M2 | 00:03:02 | ADS-B API and Python scraping package mentioned, likely on screen. |
| M2 | 00:03:13 | Map of every flight track on September 8. |
| M2 | 00:03:19 | Tracks extending to Hawaii and other countries. |
| M2 | 00:03:40 | Louder curve about to play with boosted frequencies. |
| M2 | 00:03:49 | Propeller sound playing, likely over its spectrogram. |
| M2 | 00:03:55 | ADS-B type code field. |
| M2 | 00:04:02 | Type-code lookup table that marks propeller or jet. |
| M2 | 00:04:12 | Map after removing known jet types. |
| M3 | 00:04:21 | Single flight track in pink on the test area. |
| M3 | 00:04:25 | Individual ADS-B points with coordinates, altitude, timestamp. |
| M3 | 00:04:32 | 200 m grid of candidate points around the flight. |
| M3 | 00:04:42 | CPA joke image for a different CPA. |
| M3 | 00:04:45 | Observer and its CPA on the flight track. |
| M3 | 00:05:00 | Hearing spans many points along the track. |
| M3 | 00:05:02 | Full event curve, almost two minutes long. |
| M3 | 00:05:14 | 10 km radius grid around the flight. |
| M3 | 00:05:36 | CPA time read from the closest ADS-B point. |
| M3 | 00:05:52 | Sound path from plane to listener. |
| M3 | 00:06:02 | Slant distance against horizontal distance. |
| M3 | 00:06:13 | Altitude above sea level against height above ground. |
| M3 | 00:06:20 | DEM elevation layer. |
| M3 | 00:06:29 | Worked example, CPA time 22:46:34. |
| M3 | 00:06:32 | Worked example, delayed CPA time 22:46:46. |
| M3 | 00:06:44 | Grid after processing all flights in the area. |
| M3 | 00:06:51 | One grid point with its flight IDs and delayed CPA times. |
| M4 | 00:07:13 | Offset check for an example point. |
| M4 | 00:07:19 | Timeline of delayed CPA times with the 920 s window. |
| M4 | 00:07:23 | Window sliding across CPA times with no match. |
| M4 | 00:07:30 | Matching pair found. |
| M4 | 00:07:36 | Choices for where the centre of a curve is measured. |
| M4 | 00:07:43 | Tolerance on the 920 s window. |
| M4 | 00:07:52 | About 35,000 points pass in the test area. |
| M4 | 00:07:56 | Test area against continental US land area. |
| M4 | 00:08:09 | Football-field land-area comparison graphic. |
| M5 | 00:08:38 | Two comparison clips introduced. |
| M5 | 00:08:43 | Comparison clips playing, likely as spectrograms. |
| M5 | 00:08:48 | Clip 2 has the larger frequency drop. |
| M5 | 00:09:03 | Velocity sets the drop size, distance sets its speed. |
| M5 | 00:09:14 | Curve fit over the recording's Doppler curve. |
| M5 | 00:09:39 | Measurement overlay on event 1. |
| M5 | 00:09:41 | Velocity control changing the drop. |
| M5 | 00:09:46 | Slant distance control changing the slope. |
| M5 | 00:09:53 | Fit matches the right side but not the left. |
| M5 | 00:10:06 | Fit at 100 m/s. |
| M5 | 00:10:13 | Fit at 70 m/s, clearly wrong. |
| M5 | 00:10:20 | CPA time best match 151.15, nudged to 151.13. |
| M5 | 00:10:24 | Fundamental frequency adjusted. |
| M5 | 00:10:35 | Measurement ranges for event 1 and event 2. |
| M6 | 00:10:40 | All propeller flights on the map. |
| M6 | 00:10:43 | Event 1 velocity-filtered segments in green. |
| M6 | 00:10:45 | Event 2 velocity-filtered segments in pink. |
| M6 | 00:10:52 | Green-then-pink criterion. |
| M6 | 00:11:11 | Candidate points at the measured slant distance, about 73,000. |
| M6 | 00:11:20 | Point clusters sit on airports. |
| M6 | 00:11:41 | Spectrogram gap of almost 15 minutes between the events. |
| M6 | 00:12:07 | Silence filter introduced. |
| M6 | 00:12:11 | Silence filter thresholds and logic on screen, a pause point. |
| M6 | 00:12:19 | Recap of the filter chain. |
| M6 | 00:12:52 | Points after the silence filter, about 15,000. |
| M6 | 00:13:03 | Map of the remaining 15,000 points. |
| M6 | 00:13:16 | Static source frame with nothing more to extract. |
| M6 | 00:13:23 | Summary of spectrogram-derived constraints. |
| M7 | 00:13:36 | Replay of the earlier constant-velocity explanation. |
| M7 | 00:13:46 | Replay of the imperfect event 1 fit. |
| M7 | 00:13:56 | Non-linear flight with heading and speed changes. |
| M7 | 00:14:09 | Progression of constraint layers. |
| M7 | 00:14:29 | Several geometries can cause the same variation. |
| M7 | 00:14:40 | Forward modelling from real flight geometry. |
| M7 | 00:14:47 | Candidate points along each flight path. |
| M7 | 00:15:09 | Radial velocity diagram with the observer ahead of the plane. |
| M7 | 00:15:15 | Observer to the side, radial velocity near zero. |
| M7 | 00:15:26 | Red line for the radial component. |
| M7 | 00:15:30 | Curve shape changing with flight geometry. |
| M7 | 00:15:47 | Worked example at CPA, 7:12:30. |
| M7 | 00:16:07 | Doppler equation on screen. |
| M7 | 00:16:09 | Equation terms c, v_r, and f0. |
| M7 | 00:16:19 | f0 taken from the measured curve. |
| M7 | 00:16:25 | First modelled point at 130 Hz. |
| M7 | 00:16:34 | Second point, 62.7 radial velocity gives 109.9 Hz. |
| M7 | 00:16:42 | Modelled curve built from the hearing-time velocity. |
| M8 | 00:16:45 | Naive curve flagged as wrong. |
| M8 | 00:17:14 | Emission position for time t. |
| M8 | 00:17:21 | Emission-time construction. |
| M8 | 00:17:25 | Naive and emission-time curves together. |
| M8 | 00:17:36 | Curves aligned at one point with different shapes. |
| M8 | 00:17:39 | Curves aligned at another point. |
| M8 | 00:17:48 | Real spectrogram with both models. |
| M8 | 00:17:50 | Naive curve over the spectrogram. |
| M8 | 00:17:53 | Emission-time curve over the spectrogram. |
| M9 | 00:18:16 | Modelled curve over the spectrogram. |
| M9 | 00:18:20 | Gymnastics scorecard joke. |
| M9 | 00:18:25 | Brightness summed along the curve. |
| M9 | 00:18:33 | Where the f0 measurement comes from. |
| M9 | 00:18:43 | Placing the curve in time. |
| M9 | 00:19:05 | Delayed CPA aligned to the audio timestamp. |
| M9 | 00:19:15 | Sweep over time offset and f0. |
| M9 | 00:19:25 | Best combination kept. |
| M9 | 00:19:28 | Event 2 placement. |
| M9 | 00:19:45 | Event 2 at a wrong offset. |
| M9 | 00:19:54 | Locked two-event scoring diagram. |
| M9 | 00:20:22 | Grid coarseness, true point up to 141 m away. |
| M9 | 00:20:32 | 100 m resampling. |
| M9 | 00:20:44 | Candidate count after resampling. |
| M10 | 00:21:01 | Results introduced. |
| M10 | 00:21:07 | Scatter plot of event 1 against event 2 scores. |
| M10 | 00:21:11 | Top-right quadrant. |
| M10 | 00:21:19 | Clusters per flight pair. |
| M10 | 00:21:26 | Best point per flight pair. |
| M10 | 00:21:32 | One clear leader. |
| M10 | 00:21:39 | Top point, score 20.48. |
| M10 | 00:21:47 | Event 1 curve fully covered by the model. |
| M10 | 00:21:48 | Event 2 overlay for the top point. |
| M10 | 00:21:59 | Second-best event 1 overlay. |
| M10 | 00:22:04 | Second-best and best event 1 scores compared. |
| M10 | 00:22:11 | Second-best event 2 overlay. |
| M10 | 00:22:15 | Third-best overlays. |
| M10 | 00:22:22 | Scored points in QGIS. |
| M10 | 00:22:32 | Event 1 heat map. |
| M10 | 00:22:36 | Event 2 flight path and heat map. |
| M10 | 00:22:40 | Combined heat map. |
| M11 | 00:22:53 | Faint event 1 curve again. |
| M11 | 00:23:06 | Known recording time given. |
| M11 | 00:23:16 | Flight segments at that time. |
| M11 | 00:23:22 | Score histogram. |
| M11 | 00:23:26 | Best point per flight. |
| M11 | 00:23:31 | Spectrogram overlays for the top points. |
| M11 | 00:23:38 | Traced line over the faint curve. |
| M11 | 00:23:45 | Top point overlay. |
| M11 | 00:23:47 | Second-place overlay. |
| M11 | 00:23:58 | Same coordinates from both methods. |
| M11 | 00:24:14 | Tradeoff between number of events and time constraint. |
| M11 | 00:24:48 | City-sized area against US land area. |
| M11 | 00:25:04 | Accuracy claim for one minute of audio. |
| M11 | 00:25:20 | Heat-map centre in QGIS. |
| M11 | 00:25:24 | Centre at the edge of water. |
| M11 | 00:25:27 | Coordinate opened in Google Maps. |
| M11 | 00:25:35 | Tree line in the source footage. |
| M11 | 00:25:38 | Target features, a V-shaped tree, a point, and a rounded part. |
| M11 | 00:25:49 | Street View candidate view. |
| M11 | 00:25:54 | Matching V-shape in Street View. |
| M11 | 00:25:59 | Source footage and Street View side by side. |
| M11 | 00:26:05 | Security camera on the pole. |
| M12 | 00:26:13 | High-pass filter introduced. |
| M12 | 00:26:19 | Voice band overlaps the Doppler band. |
| M12 | 00:26:28 | Recording with the Doppler curve in the editor. |
| M12 | 00:26:31 | High-pass applied. |
| M12 | 00:26:37 | MP3 export spectrogram with the curve gone. |
| M12 | 00:26:41 | Gain boost brings the curve back. |
| M12 | 00:26:58 | Hidden Doppler curve under this video's own speech. |
| M12 | 00:27:01 | Spectrogram reveal of the masked curve. |
| M12 | 00:27:06 | Cuts as a working measure. |
| M12 | 00:27:22 | Phone calls give known times. |
| M12 | 00:27:33 | Receiving phone under Squishmallows. |
| M12 | 00:27:38 | JBL speaker in another room. |
| M12 | 00:27:46 | Curve passing through the phone call. |
| M12 | 00:27:53 | Gap in the curve on the spectrogram. |
