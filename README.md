# plane-geo

A rebuild of the project in [I discovered a sound that leaks your exact location (and it's everywhere)](https://www.youtube.com/watch?v=UytYrhYLOKI) by colsto.

The video locates where an audio recording was made from the aircraft audible in its background. It measures the Doppler shift of each passing plane in a spectrogram. It then matches those measurements against public ADS-B flight tracks over a grid of candidate locations, and reports the cells that fit.

This repo holds two things:

- `design/` contains the pipeline that turned the video into a design document, plus everything it produced. Start with [design/04_design/design_document.md](design/04_design/design_document.md). [design/README.md](design/README.md) explains how to rerun each stage.
- `src/` is reserved for the rebuild itself and is empty for now.
