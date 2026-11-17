# Transcript: I discovered a sound that leaks your exact location (and it's everywhere)

Model `large-v3` on `cuda`, language `en`, 333 segments.

[00:00:00] I have found off-grid structures in the middle of a rainforest, things 600 meters deep in the ocean,
[00:00:05] and some stuff I can't even share on YouTube. But what I'm going to share today is no exaggeration,
[00:00:11] the single most powerful geolocation clue I've come across. And to illustrate this,
[00:00:17] I'm going to geolocate this. It's a video, but nothing really changes visually. If you want to
[00:00:22] pause and try it yourself, it's linked in the description. The only information you have is
[00:00:27] it was filmed september 8th somewhere in the continental us that's all you get but with that
[00:00:33] information it is possible and i'm going to show exactly how so i did a video geolocating with
[00:00:43] thundersounds the benefit is that they travel really far and they penetrate structures extremely
[00:00:48] well the downside is that we were only able to get about five kilometer precision that could tell you
[00:00:52] basically what city it was filmed in and maybe what side of town what we're using today has those
[00:00:57] same benefits, but here's the precision. So I'm going to play you two sections of audio.
[00:01:09] One has the information required to find this location. The other does not. See if you can
[00:01:14] tell which one does. You probably couldn't tell because it's completely inaudible. But if I open
[00:01:30] this in a spectrogram, here we can see all the frequencies. So if you're not familiar with a
[00:01:34] spectrogram, the X axis is time and the Y axis is frequency. Now, even with this, you still really
[00:01:40] can't see anything. It's only when I zoom into the right frequency and then increase the resolution
[00:01:45] that you start to see it. I'll do one more. This is a Doppler curve from an aircraft and it's what
[00:01:54] we're going to use to locate this video. Now, fair warning, this is insanely powerful, but it also
[00:02:00] requires a lot of complex stuff. This took me months to build over 5,000 lines of code. I was
[00:02:06] working with 50 gigabyte Parquet files, 3D physics modeling, countrywide DEMs, and so much more.
[00:02:12] That's all to say, this is going to be a long video, but I'm going to explain every step in a
[00:02:16] way that anyone can understand it, even if you know nothing about any of this stuff. So with that
[00:02:21] out of the way, let's look at the rest of this audio. We have one Doppler curve here. If I keep
[00:02:25] going to the right, you can see another one. It's a lot louder and you can also see the harmonics on
[00:02:31] top. We'll zoom out a bit. I think we have one more here. So these two are what we'll be using.
[00:02:37] But let's take a step back. Why do we even care about Doppler curves? What are we going to be
[00:02:41] using these for? So there's something called ADS-B data, and it's data on pretty much every
[00:02:46] plane in the sky. It's position, speed, altitude, and a bunch of other things. So my first thought
[00:02:52] was, could I narrow this down to only places that heard a plane and then 920 seconds later
[00:02:57] heard another one. To do that, we need all this ADS-B data first. They have an API you can pay
[00:03:04] for. There's also a Python package just to scrape the data, but it's massive. So I ran this for a
[00:03:09] few hours to get all the flights in the continental US on September 8th. Now here's what that data
[00:03:15] looks like. By default, it downloads the entire flight path. That's why you see things going to
[00:03:19] Hawaii over here or other countries. But anything that flew over the US on that day is in this
[00:03:25] data set, including the two planes in our recording. So now we just need to find them.
[00:03:30] So like I said, I want to narrow down to the locations that hurt a plane,
[00:03:33] and then 920 seconds later, hurt another one. Now these Doppler curves are made by a plane,
[00:03:38] of course, but specifically a propeller plane. I boosted some frequencies so you can hear it
[00:03:43] better. Let me play you a bit of the louder one and you can hear pretty intuitively that
[00:03:46] it's a propeller plane. One of the fields in the ADS-B data is type code. Now this doesn't say
[00:03:59] propeller versus jet plane. But I did some research, found this lookup table, and this does.
[00:04:05] Now there's some missing data in that lookup table. So instead of filtering to the propeller
[00:04:08] planes, I just filtered out all the known jet types. But after doing that, the map looks like
[00:04:13] this. But now time for this time offset filter. So I'll do this on a small area to illustrate
[00:04:21] first. This pink line is the ADS-B data for one flight. You can see the individual flight points
[00:04:27] here, where we have coordinates, altitude, timestamp, things like that. What we do is lay
[00:04:32] a 200 meter grid of points. And then for each point, note the time that it would have heard
[00:04:37] this flight. Now it's time for our first new terminology, CPA. Not that one. Closest point
[00:04:44] of arrival. So for an observer, say here, CPA is where the plane is closest to that observer.
[00:04:51] The reason that's important is when we say heard a plane 920 seconds later, hearing a plane is not
[00:04:56] really a single point in time. If you're standing at this point, you hear the plane here and here
[00:05:02] and here. This whole Doppler curve is almost two minutes. So what we need to use is the CPA time,
[00:05:07] which is roughly the middle of this. It's when the plane was closest and loudest. So for this
[00:05:12] flight, lay a 200 meter grid of points. I did a pretty conservative 10 kilometer radius. Like
[00:05:17] beyond that, you probably wouldn't hear a plane even in like ideal conditions. So let's just make
[00:05:21] sure we don't miss anything. And then for each one of these points, we note the CPA time for this
[00:05:26] flight. Two important things here. First is that CPA time actually means the time when the plane
[00:05:32] was closest. For this example, that would be probably this point. So 22, 46, 36. That's
[00:05:38] actually not what we need though. Now for the second terminology, what we need is the delayed
[00:05:43] CPA time. It's the time that the CPA would have been heard by an observer. And that's because
[00:05:49] the sound has to travel from here all the way three plus kilometers to a listener. That was
[00:05:55] first important thing. The second is that planes are in the sky, meaning the distance that we use
[00:06:01] in this calc needs to be the slant distance, not just the horizontal distance. Luckily, the ADS-B
[00:06:07] data gives the plane's altitude. However, altitude is not the height above the ground. Altitude is
[00:06:13] the height above sea level. So to get this slant distance, we actually need to know the elevation
[00:06:18] for each grid point. And to do that, we'll use a DEM. That'll tell us at any point the elevation.
[00:06:24] so now with that we can actually say for our point here for this flight the cpa time of 22 46 34
[00:06:32] but the delayed cpa time of 22 46 46 so we do this for every point here and that's one flight done
[00:06:41] then we just do that for all flights in the area and we're left with this grid of points
[00:06:45] because basically every point heard at least one flight especially since i gave the 10 kilometer
[00:06:50] radius but for each of these here let me zoom in on one for each of these what i have is a list
[00:06:55] of flight IDs and the associated delayed CPA times. Basically if you were standing here on
[00:07:00] this day at each of these times you could look up and you could hear a plane. So back to our goal
[00:07:05] what we want is somewhere that heard a plane and then 920 seconds later heard another one. So for
[00:07:10] each of these points we then just check for that offset. Here's what that actually looks like. So
[00:07:14] here's an example point and each of those delayed CPA times and then we have a 920 second offset
[00:07:19] window. And we just look here, nothing, 920 seconds later. This one again, not quite. And
[00:07:28] then this one over here. There we go. Now, when we say 920 seconds apart, it matters where we're
[00:07:34] measuring from. Like, are you calling the center here or here or here? And that's like a plus or
[00:07:39] minus five second variance. So that's why if you look closely on this, there's a bit of wiggle
[00:07:44] room that we're allowing for in that 920 second offset. But anyway, that's the methodology. So
[00:07:49] how many of our points survived that filter? It's about 35,000. And that's for this small
[00:07:55] test area, which is less than 0.05% of the continental U.S. land area that we need to
[00:08:00] search. Like just a side tangent, I don't think people understand how much land area there is
[00:08:05] in the U.S. If you divided the continental U.S. into a bunch of football fields and laid them
[00:08:10] end to end, it would wrap all the way around the earth and to the moon and back almost 200 times.
[00:08:18] That's what we're searching for this.
[00:08:21] So we need to do a lot better, and we can, but we need to know some things about Doppler curves.
[00:08:28] All jokes aside, this is actually so cool.
[00:08:31] Doppler curves will give us a ton of additional information.
[00:08:34] And I actually don't need to teach you anything because you already know this intuitively.
[00:08:38] Let me play you two clips.
[00:08:47] You can already tell that clip two was going faster.
[00:08:49] The reason is because the drop in frequency was much larger.
[00:08:53] And that drop in frequency can actually tell us the exact speed that an object was going.
[00:08:58] So assuming linear constant velocity, there are only two things that determine what this Doppler curve looks like.
[00:09:03] The velocity determines how big of a frequency drop, and our CPA distance, remember that one, determines how quickly that drop occurs.
[00:09:12] So for the Doppler curve in our audio, we can fit a curve to that and know how fast the aircraft was going and how far away it was from the listener.
[00:09:20] So now, instead of filtering to points that heard an aircraft and then 920 seconds later
[00:09:25] heard another one, we can filter to points that heard an aircraft going a certain speed
[00:09:30] at a certain CPA distance and then 920 seconds later heard another plane going a certain speed
[00:09:36] at a certain CPA distance. That's a lot more constraining. So let's measure one of the Doppler
[00:09:41] curves. You can see that the velocity makes the frequency drop larger and then the CPA slant
[00:09:46] distance just changes how quickly that drop occurs. What you'll notice on this one is that
[00:09:51] it doesn't fit a perfect Doppler curve though. Like this right hand side does, left hand side
[00:09:56] not so much. That'll be important later, but what we do in the meantime is we just take a pretty
[00:10:01] generous range for velocity so that we don't accidentally filter anything out. So here's
[00:10:05] kind of a decent fit on the right side at 100 meters per second. I can't confidently say this
[00:10:10] plane was going exactly 100, but we can be pretty sure it wasn't going 70. Similarly for the time
[00:10:16] offset, there's still a couple seconds of like potential measurement error here. Okay, best
[00:10:20] match 151.15. I'll move it to 151.13, slide that fundamental frequency up a little bit. And yeah,
[00:10:27] you know, that could work. That's just to say we still can't pin down the offset time precisely to
[00:10:31] the second. But we do this for event one and event two, and we get the measurement ranges for each.
[00:10:38] So the first thing is the speed filters. Here are all of the prop flights, but here are all the ones
[00:10:43] matching the event one velocity range. And then in pink, here are the same ones before event two.
[00:10:49] So now what we're looking for is a point that heard a green line and then 920 seconds later
[00:10:54] heard a pink line. But remember the other thing we know about this too, in addition to the velocity
[00:10:59] is the distance away. So on this green line for event one, we don't need to lay that entire grid
[00:11:04] from zero to 10 kilometers away. We know the pretty precise slant distance that the observer
[00:11:10] was from each of these. So here are those points. They're about 73,000. But if I zoom into any of
[00:11:17] these clusters, what do you notice? Airport. Another airport. Most of those 73,000 points
[00:11:26] are just near airports. And it makes sense because that's where the planes are. More air traffic just
[00:11:31] means higher chance that you happen to have two flights that meet those criteria. But the signal
[00:11:37] in our video is not only what we hear, it's also what we don't hear. There's no Doppler curve
[00:11:43] between these two. That's almost 15 minutes of not hearing a plane. You're not going to get that
[00:11:48] right outside of a major airport. And that's part of why this is so useful. Because if you're near
[00:11:52] an airport, you hear a lot of flights and you get a lot of signal. If you're not, then the silence
[00:11:57] itself is also a signal. So it really works anywhere on that spectrum. So what that means
[00:12:02] for our search, I'll take all of these 73,000 points and I'll apply a silence filter. Feel free
[00:12:09] to pause here if you're interested in the specific thresholds and logic I used, but overall I just
[00:12:13] disqualified any point that would have hurt a flight between our two events. That was pretty
[00:12:18] conservative with the thresholds. So to recap, we took our velocity filtered flight segments for
[00:12:23] event one and event two, laid candidate points based on the slant distance range from the Doppler
[00:12:28] curve measurements. Then for all those candidate points, did the time offset filter, where that
[00:12:33] point would hear a flight of the right speed at the right distance away, and then 920 seconds later,
[00:12:39] hear another flight of the right speed at the right distance away. That gave us this roughly
[00:12:44] 70,000 points. Now adding on to all that logic, the silence filter, where that point doesn't hear
[00:12:49] another flight between the two events. That drops the 70,000 to 15,000. Even with all those
[00:12:58] constraints, there's just so much land area and so many flights that 15,000 points still meet all
[00:13:06] those criteria. And usually at this point in a search, I would just start looking at some of
[00:13:09] the points, seeing why they don't work, and then encoding that logic as another filter.
[00:13:15] The problem here is we just have this picture. There's nothing else we can get from this.
[00:13:20] And we used pretty much everything we could from the spectrogram. The velocity, the slant distance,
[00:13:24] the time offsets, even the absence of the planes between the two. There's just not much more we
[00:13:30] can do. So thanks for watching. I'm just kidding, of course we're going to find it. Remember when
[00:13:36] I said this. So assuming linear constant velocity, there are only two things that determine what this
[00:13:42] Doppler curve looks like and this. What you'll notice on this one is that it doesn't fit a
[00:13:47] perfect Doppler curve though. The reason they don't fit an ideal Doppler curve is because
[00:13:53] planes don't fly in steady perfectly linear motion. They change heading, they speed up,
[00:13:58] they slow down, and all of that info is encoded in this Doppler curve. But to get it out,
[00:14:05] we're going to need to go a layer even deeper. First, we looked at whether a flight occurred
[00:14:12] at this offset. Then we looked at whether a flight of a certain speed occurred at this offset at a
[00:14:18] certain distance. Now what we're going to be asking is how exactly did that flight pass over?
[00:14:23] Now you can't go from spectrogram to knowing the exact flight geometry. Multiple things can cause
[00:14:28] variations in this. It could be a change in speed, heading, altitude, any combination of those.
[00:14:34] So instead of trying to reconstruct what flight geometry would have produced this,
[00:14:39] what we can do instead is model what the exact Doppler curve would have been
[00:14:43] for the actual flight geometry of each flight.
[00:14:46] We then do this for each candidate point on each flight path,
[00:14:50] and then we find the one that matches.
[00:14:53] So, how do we model a Doppler curve?
[00:14:57] The Doppler curve is a function of the radial velocity of the plane
[00:15:01] with respect to the observer.
[00:15:03] That sounds complicated. All it means is how fast was the plane moving directly toward or away from
[00:15:09] the observer? So if this is us and we're right in front of the plane, plane velocity is 90,
[00:15:14] radial velocity is 90. If we're directly to the side, plane velocity is 90, radial is basically
[00:15:19] zero. It's not going toward or away from us. So at this point, there's no Doppler effect.
[00:15:24] And anywhere in between, we can see that red line representing the radial component of the
[00:15:29] plane's velocity. You can see here how the Doppler curve would change depending on the actual flight
[00:15:34] geometry. So how we'd actually create this Doppler curve. What we want to know is what frequency did
[00:15:40] the observer hear over time. So we'll start at t equals zero or CPA. In this specific example from
[00:15:46] the flight data that's 7 12 30. We don't know the actual time from the recording. This is just an
[00:15:51] example to illustrate. So for that time we go look at the flight data at 7 12 30 and we get the plane's
[00:15:57] radial velocity. In this case, since it's at CPA, the radial component is 0. But we then take that
[00:16:02] radial component and run it through the Doppler equation, and it outputs a frequency. The Doppler
[00:16:07] equation looks complicated. It's not really. C is just a constant for the speed of sound. V sub r,
[00:16:13] that's the radial component that we just calculated. The only other term in here is f sub 0.
[00:16:17] That's the fundamental frequency. And that just comes from here, where we measure the curve.
[00:16:21] Just remember how we slide this up and down. So that's all the components. It outputs 130 hertz,
[00:16:26] and then we plot that for 7, 12, 30. Then we just do the same thing again for 7, 12, 35. Check where
[00:16:33] the plane is, get its radial velocity, 62.7, run that through the Doppler equation and get 109.9
[00:16:39] and then plot that there. If you do that for all these points, you end up with the Doppler curve
[00:16:43] for this observer. However, that's actually wrong and it would make our search fail entirely. I'll
[00:16:50] give you a second to pause and think about why. The reason is we want to model the frequency heard
[00:16:55] by the observer at each of these times. So the frequency heard by the observer at 71230 is not
[00:17:01] based on the plane's radial velocity at 71230. It's actually based on the plane's velocity when
[00:17:08] it produced the sound that we then hear at 71230. So the correct flow is for t equals zero, find
[00:17:14] where the plane was when it produced that sound, take that radial velocity, run it through the
[00:17:18] Doppler equation, and then plot that frequency. And so here's what that looks like. Now if we
[00:17:24] just do that to the end. We're left with two curves. One is the wrong way. One is the right
[00:17:27] way. And you might just think, okay, sound takes time to travel. So just delay the curve. What's
[00:17:32] the difference? It's not just the same curve delayed in time. See, if I match up like this
[00:17:37] point, very different curve, same thing over here, match up that point. So that first methodology
[00:17:43] didn't just make the right curve, but a few seconds late, it made an entirely wrong curve.
[00:17:48] Here's an actual example. So this is our spectrogram. This is what that wrong curve
[00:17:52] would have plotted versus this is the right methodology. So that's how we model this Doppler
[00:17:56] curve for a given observer. We then just repeat this process for all the candidate points and all
[00:18:02] the flights. But what we're left with from that is the exact Doppler curve that each point would
[00:18:08] have heard based on real flight geometry. So then we have all these curves. The question is,
[00:18:14] how do we score them? So we take the Doppler curve, we plot it on a spectrogram. And then
[00:18:18] based on how close it looks, I raise up the scorecard kind of like gymnastics. I'm just
[00:18:22] kidding. We do plot it on a spectrogram, but we just sum the brightness values that each curve
[00:18:26] covers. There's two things we have to account for though. One is that the fundamental frequency that
[00:18:31] we used to model this curve was based on a measurement here. So that could introduce
[00:18:36] some source of error. The second is, similarly, the CPA time is as well. So the first thing,
[00:18:42] we have this modeled Doppler curve. How do we know where to put it on the spectrogram for scoring?
[00:18:47] Well, for the modeled curve, we have a delayed CPA point.
[00:18:50] That's just from flight geometry.
[00:18:52] But remember, we don't know the time of filming.
[00:18:54] So we could know the delayed CPA time for this flight.
[00:18:57] But on our spectrogram, we have no idea where that is.
[00:19:00] But we do have the CPA time in terms of just the timestamp of the audio.
[00:19:04] So that lets us say, put the delayed CPA time right at this timestamp.
[00:19:08] But back to what I was saying, that is a measurement and it's a source of error.
[00:19:12] So the way we account for this is when we place the curve on the spectrogram,
[00:19:15] we do a sweep of a few seconds on both of those variables that we measured. So the slight time
[00:19:21] offset, and then same thing for the fundamental frequency. And then we just take the highest
[00:19:25] scoring combination of those. That's how we score event one here. Event two is a little bit
[00:19:30] different. We still do the fundamental frequency sweep because that is still a measurement.
[00:19:34] However, event two's temporal placement relative to event one is entirely determined by the flight
[00:19:40] geometry. Meaning if we correct for that error, when we place event one and event two is still
[00:19:45] placed at a bad offset time, that genuinely just means that this is not a good candidate.
[00:19:51] And we want to capture that too. So that's the combined locked scoring methodology,
[00:19:55] where the offset between these two, because it's determined only by flight geometry,
[00:20:00] is entirely locked. We correct for measurement error on event one, and then event two falls
[00:20:05] wherever it does. That's how we eliminate any potential measurement error, but still get really
[00:20:10] precise temporal offset scoring. The one downside of this is that 200 meter grid resolution that
[00:20:16] we've been using is just a little bit too coarse for this. Like the actual correct candidate could
[00:20:21] be up to 141 meters off and like kind of score pretty bad. That's good because it means it's
[00:20:27] really precise, but it also just means we have to take our 200 meter grid points and expand them
[00:20:32] into 100 meter resolution and just score more points. All of this is done for one candidate
[00:20:38] point. So we need to do this for the 15,000 times whatever to make them 100 meter resolution. So
[00:20:44] probably like 30, 40,000. So super computationally expensive. And that's why you see all the steps
[00:20:50] we did prior to this to narrow down are still extremely important. Like you just could not do
[00:20:54] this on the full US for the full day. So that's the entire methodology. I ran this for all the
[00:21:00] points. Let's take a look at the results. So each candidate point has an event one score and an
[00:21:06] event to score. So I placed them on the scatter plot here. Higher scores are better. So we're
[00:21:10] looking for things in the top right quadrant. So there's some high scoring ones here, but there's
[00:21:14] not really one that stands out a ton. But for each combination of flight IDs, there's kind of a
[00:21:19] cluster of points. And really within each cluster, what we care about is the highest scoring point.
[00:21:24] So I can do basically that on the scatter plot, group them by flight pair, and then just take the
[00:21:29] highest scoring point for each flight pair. And now you can see there is one that scores a lot
[00:21:34] higher. And I'll show you the actual spectrograms and modeled curves for a couple of these top ones.
[00:21:39] So this highest scoring point with 20.48, that's this one here. For event one, I mean, you can't
[00:21:45] even see the Doppler curve because it's perfectly covered. And then for event two, very similar.
[00:21:51] But let's also look at the second best scoring one. So you kind of see the difference between
[00:21:54] a 20 versus a 15 score. So for event one, it's pretty close. It misses this top bit right here,
[00:22:01] as well as being a little bit off in the center. But I mean, as far as event one, this is a nine,
[00:22:05] five, this is a 10, six. What really brings down the score is it's event two. And you can see it's
[00:22:11] event two is pretty badly off, but this is the second best scoring point. And it's kind of
[00:22:15] similar for three, worse on event one, a little bit better on two. Like none of these are even
[00:22:20] close. And then first place is spot on. So let's go look at this point in QGIS. So here are the
[00:22:26] scored points. Now that I know the flight IDs though, what I can do is run much finer resolution
[00:22:31] with just that flight. So like here's the heat map when you just score event one. And then for
[00:22:35] event two you can see its flight path and its heat map. And then combined we have this. But all this
[00:22:42] has just been dots and curves and scores. We still haven't found this location. I want to do one more
[00:22:48] thing before we hop into Street View because this is probably the most insane part of the entire
[00:22:52] project. Do you remember this Doppler curve? The one that you couldn't hear even when you were
[00:22:57] listening for it. What if you just had this one minute clip, but you knew the time that it was
[00:23:02] recorded? Could you still find this? So say I told you this was 8.37 PM UTC. We could do the same
[00:23:09] spectrogram measurement, get the velocity bounds for the flight, but then also filter down to only
[00:23:15] the segments at that time. So that's the view I have here. So here are the scores for that. Since
[00:23:20] it's only one flight, there's no scatter plot. It's just a histogram, but right-hand side is
[00:23:24] better. And here's the view if you only take the highest scoring point per flight. So we have a
[00:23:29] couple of high scoring points here. And here's the spectrograms. I did one thing slightly different
[00:23:34] on this, which is because this Doppler curve is so faint, I just kind of traced it with a line
[00:23:39] and then scored each candidate's curve based on how close it was to that line rather than based
[00:23:44] on the actual brightness. So the top scoring point is spot on. Second place is close, but I mean,
[00:23:49] you can definitely see where it's off. And beyond that, it gets pretty bad. But what you might
[00:23:53] notice about this coordinate, if we go back to our original two event scoring, the highest scoring
[00:23:58] point, 40.87, 40.87, negative 73.5, negative 73.5. The same location scoring first by a significant
[00:24:08] margin across two different methodologies with entirely different flights. And if I were to
[00:24:13] generalize this, you can kind of pick two things here that are bad. So in our first example, we
[00:24:17] didn't know what time the video was filmed or where in the US, but we had two flights. In the
[00:24:22] second example, we only had one flight. We still did the full US search, but we had a much tighter
[00:24:26] temporal constraint. So you kind of just need one of these things to be good. The thing is though,
[00:24:31] I've never had a search where all I knew was that it was just somewhere in the US. You typically
[00:24:36] know a city or a state or even, oh, okay, I'm looking north at some body of water. Like I chose
[00:24:41] this picture just to demonstrate the extremes of like, even knowing absolutely nothing, you can
[00:24:46] still find the location. If you knew the city, a city is like 0.01% of the land area. So when you
[00:24:51] constrain the spatial bounds that much, it allows you to open up the temporal bounds and you don't
[00:24:56] need to know the minute or the hour or even the day of filming. I just want you to grasp how
[00:25:01] powerful this is. We got the location of that recording within a couple hundred feet from one
[00:25:06] minute of audio where you cannot hear the plane. And I mean, these flyovers happen all the time
[00:25:12] and those frequencies go through walls. Like any video you take could have that in there.
[00:25:17] but anyway we still have not found this exact photo so let's go back here in QGIS I'll zoom
[00:25:23] into kind of the center of this I mean it's honestly in water so it'd be like right on this
[00:25:26] bank grab this coordinate and let's take a look in Google Maps and let's see what we got for street
[00:25:31] view all right let's zoom in here so what we're looking at is a super pixelated tree line and we
[00:25:37] kind of want this v-shaped tree followed by a point and then this big rounded part so from this
[00:25:42] location. Nothing really that way. I'm not seeing any V-shaped trees here. Here's kind of one,
[00:25:51] but we need it to go up and to the right. There's one more here where we have this V-shape with a
[00:25:58] point and then this rounded part. Here they are side by side. And if I zoom out and look at the
[00:26:04] top of this pole, here's the exact security camera that took this footage. So how do you protect
[00:26:10] yourself? Well, the first thing people might think is a high pass filter. There are two reasons that
[00:26:15] this doesn't work. First, the frequencies of these Doppler curves are pretty much the same
[00:26:19] frequencies of the human voice. You'd be removing a good chunk of what you actually want to record.
[00:26:24] Second, depending on how you high pass, it might not even work anyway. So say this is my recording,
[00:26:30] I have the Doppler curve here, I'll apply the high pass and cut off the Doppler curve.
[00:26:34] I'll export this as an mp3, open that mp3, and the Doppler curve is completely gone.
[00:26:40] Now let me just boost all the frequencies and the curve is back.
[00:26:45] The next thing you might think, while I would be talking during my video, there'd be other
[00:26:48] loud things going on, so the mic would pick up on that, not background plane sounds.
[00:26:54] What if I told you, for the past 15 seconds, I've had a JBL speaker across the room playing
[00:26:59] a Doppler curve?
[00:27:03] So highpass doesn't work, you can't drown it out.
[00:27:06] One thing that works is just making cuts.
[00:27:08] That way you can't use the time offset between these.
[00:27:11] But remember when we found the location with just one minute of audio?
[00:27:14] If it's a large search area, you might need to know the pretty precise time of recording.
[00:27:18] And you might think, when are you ever going to know the exact time of a recording?
[00:27:22] How about any phone call you've ever had?
[00:27:25] But phone calls compress audio.
[00:27:27] They apply noise reduction.
[00:27:29] Surely a Doppler curve won't survive that.
[00:27:31] Now you're listening through another phone speaker under a bunch of Squishmallows.
[00:27:37] I'm in a different room with that same JBL speaker playing the Doppler curve.
[00:27:43] No leakage.
[00:27:43] I'm going to go on.
[00:27:44] Doppler curve is going through the phone and only through the phone.
[00:27:52] what you should have seen there was a gap in the Doppler curve. And then when I started talking
[00:27:56] again. So high pass doesn't work, you can't drown it out, and it can survive phone compression.
[00:28:04] So what can you actually do? Like I said, you could make cuts in your videos or apply some
[00:28:09] additional noise cancellation. But look, I'm not trying to fearmonger with this video. The odds
[00:28:12] that someone can and does actually do this is pretty slim. In reality, there's probably 100
[00:28:18] easier ways to find you than this. The one real use case I could see, I mean, the audio we used
[00:28:23] is just from some random security camera, but it could adjust as well, Ben, but it's from a
[00:28:28] investigation or a video online. Something with literally zero visual clues could be located
[00:28:36] using this. And maybe that makes you feel optimistic, maybe a bit uneasy, or maybe like me,
[00:28:42] you just find all this fascinating. That when you hear a plane fly over, you're probably in the only
[00:28:48] place on Earth hearing that exact curve, and all the information needed to recreate that
[00:28:53] exists.
[00:28:56] And 30 minutes ago, all of this was just background noise.
