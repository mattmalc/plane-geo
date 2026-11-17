# plane-geo

A rebuild of the project in [I discovered a sound that leaks your exact location (and it's everywhere)](https://www.youtube.com/watch?v=UytYrhYLOKI) by colsto.

The video finds where a security-camera recording was made. The propeller aircraft in its audio cannot be heard, but they show up as Doppler curves in a zoomed spectrogram. The creator measures each curve's speed, slant distance, closest-approach time, and fundamental frequency. The creator then filters ADS-B flight tracks for the filming day over a grid of candidate ground points. For each surviving point and flight, the pipeline models the curve that point would hear and scores it against the spectrogram. The best-scoring flight pair leads to Oyster Bay, New York, where Street View shows the camera on a utility pole.

This repo holds two things:

- `design/` contains the pipeline that turned the video into a design document, plus everything it produced. Start with [design/04_design/design_document.md](design/04_design/design_document.md). [design/README.md](design/README.md) explains how to rerun each stage.
- `src/` is reserved for the rebuild itself and is empty for now.
