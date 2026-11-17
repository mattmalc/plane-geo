# M2 breakdown: Download ADS-B data and keep propeller aircraft

Range: 00:02:37 to 00:04:14. Systems: S1.

## 1. Goal and done criteria

Goal: build a flight dataset that can find the two aircraft heard in the recording.

- The first search idea is to keep only places that heard one plane and another plane 920 seconds later. [stated] [00:02:52] ![](frames/M2_000256.png)
- ADS-B data covers nearly every plane in the sky, with position, speed, altitude and other fields. [stated] [00:02:41]
- The dataset must hold every flight over the continental US on September 8, including the two planes in the recording. [stated] [00:03:09] [00:03:19]
- Known jet types must be removed. [stated] [00:04:05]

Done means:
- A local table of all flights seen over the continental US on September 8, with whole tracks. [stated] [00:03:15]
- A per-flight table with typecode, so each flight can be classed. [shown] [00:03:56] ![](frames/M2_000356.png)
- Flights with a known jet typecode are removed. The rest stay, including unknown types. [stated] [00:04:05]
- A map of the remaining tracks. [shown] [00:04:12] ![](frames/M2_000412.png)

## 2. Procedure

1. Find the two Doppler curves in the recording spectrogram. They become the two "events" 920 s apart. [shown] [00:02:42] ![](frames/M2_000242.png) [00:02:56] ![](frames/M2_000256.png)
2. Pick the ADS-B source. Flightradar24 is shown as the example of live ADS-B. Its sidebar offers a paid "B2B: Explore our flight data API". [shown] [00:02:47] ![](frames/M2_000247.png) [00:03:02] ![](frames/M2_000302.png) The creator did not use the paid API. [stated] [00:02:57]
3. Use the Python package `pyfr24` to scrape the data. [shown] [00:03:04] ![](frames/M2_000304.png) He ran it for a few hours. [stated] [00:03:04]
4. Phase 1, flight-ID discovery sweep: step through timestamps across the day, query a target bounding box at each, split any box that hits the flight cap into north and south halves, and save the unique flight IDs. [shown] [00:03:09] ![](frames/M2_000309.png)
5. Drop flights never seen airborne (`max_alt` not > 0). Write the rest to `FLIGHT_IDS_AIRBORNE_CSV`. [shown] [00:03:11] ![](frames/M2_000311.png)
6. Phase 2: for each airborne flight ID, fetch the full trail, explode it into points, normalise column names, and append to a tracks CSV. Log each fetch so reruns skip done work. [shown] [00:03:11] ![](frames/M2_000311.png) [00:03:13] ![](frames/M2_000313.png)
7. Plot all tracks in a GIS view. Whole tracks are downloaded, so lines reach Hawaii and other countries. [shown] [00:03:13] ![](frames/M2_000319.png) [stated] [00:03:15]
8. Listen to the louder curve with boosted frequencies. It sounds like a propeller plane. [stated] [00:03:38] ![](frames/M2_000340.png) ![](frames/M2_000349.png)
9. Read the `typecode` column of the per-flight table. Typecode does not say propeller or jet. [shown] [00:03:56] ![](frames/M2_000356.png) [stated] [00:03:55]
10. Join typecode to the ICAO DOC 8643 Aircraft Type Designators table, which has an Engine Type column. [shown] [00:04:02] ![](frames/M2_000402.png)
11. Remove flights whose type designator has Engine Type = Jet. Keep everything else, because the lookup has gaps. [stated] [00:04:05]
12. Re-plot the filtered tracks. [shown] [00:04:12] ![](frames/M2_000412.png)

## 3. Components

ADS-B and flight data
- Fields named aloud: position, speed, altitude, "a bunch of other things". [stated] [00:02:46]
- Flightradar24 flight panel fields for one example, N4382S: aircraft type PA32 (Piper Saratoga), barometric alt 7,800 ft, ground speed 130 kts, track 358°, data source "Terrestrial ADS-B", category General aviation. [shown] [00:02:47] ![](frames/M2_000247.png)
- Coverage: all flights over the continental US on September 8. [stated] [00:03:09]
- Download time: "a few hours". [stated] [00:03:04]
- Downloads include the entire flight path, not only the US portion. [stated] [00:03:15]

Per-flight table (sheet `flight_ids_airborne`) [shown] [00:03:56] ![](frames/M2_000356.png)
- Columns: `flightid`, `registration`, `typecode`, `callsign`, `first_seen_utc`, `last_seen_utc`, `max_alt`, `sample_lat`, `sample_lon`. [shown]
- `flightid` values display as 1.1E+09. `first_seen_utc` and `last_seen_utc` display as 1.789E+09. [shown]
- These are Unix seconds near 1.789e9, which falls in September 2026. [inferred] M2-I01
- Example rows: B78X / KLM225 / max_alt 20000; M20P / N9129X / 6250; PA44 / 5225; B39M / UAL1367 / 34000; COL4 / N40CX / 3225; EC35 / N405TJ / 3900; B752 / UAL2191 / 38000; P28A / N464FA / 1925; C162 / 2800; B772 / UAL983 / 22900; C172 / N6621D / 4200; CL35 / EJA781 / 43000; GALX / 8925; C150 / N8436 / 2400. [shown]
- `max_alt` is in feet. [inferred] M2-I02
- Sample coordinates in the rows shown are mostly near 40.3 to 40.7 N, -75.1 to -76.2 E, with a few elsewhere (37.66, -91.70; 39.75, -90.85). [shown]

Track point fields (from `standardize_rows`) [shown] [00:03:13] ![](frames/M2_000313.png)
- `flightid`, `timestamp`, `latitude`, `longitude`, `altitude`, `ground_speed`, `track`, `vertical_speed`, `source`.

ICAO type lookup [shown] [00:04:02] ![](frames/M2_000402.png)
- Source: ICAO, DOC 8643 - Aircraft Type Designators web page.
- Columns: Manufacturer, Model, Type Designator, Description, Engine Type, Engine Count, WTC.
- 7,261 entries. 727 pages at 10 per page.
- Engine Type values seen: Jet, Piston. Description values seen: LandPlane, Amphibian. WTC values seen: M, L.
- Example rows: 328 SUPPORT SERVICES Dornier 328JET, J328, LandPlane, Jet, 2, M. 3XTRIM 450 Ultra, UL45, LandPlane, Piston, 1, L. A-41 VNS-41, CE22, Amphibian, Piston, 2, L.
- Page shows "Last Updated: 01 October 2026" and "Next Scheduled Update: 29 October 2026".

Recording
- Audacity track name: `oyster bay_20260913T191804Z_60to120min`. [shown] [00:03:55] ![](frames/M2_000355.png)
- Audacity view of the louder curve spans about 33:45 to 38:30 on the timeline, 0 to 790 Hz. The main curve falls from about 180 Hz to about 100 Hz, with harmonics above. [shown] [00:03:49] ![](frames/M2_000349.png)
- Custom spectrogram viewer shows 60:00.000 total length, frequency axis to 800 Hz, cursor at 2139.330 s at [00:03:40] and at 2293.702 s at [00:02:42]. [shown] ![](frames/M2_000340.png) ![](frames/M2_000242.png)
- Interval between events: 920 s. [shown] [00:02:56] ![](frames/M2_000256.png)

## 4. Systems touched

S1: ADS-B ingest and aircraft filtering
- How it works: a two-phase scraper over Flightradar24 via `pyfr24`. Phase 1 sweeps timestamps over the day and collects flight IDs inside a bounding box, splitting saturated boxes. Phase 2 pulls each flight's full trail and writes track points to CSV. [shown] [00:03:09] [00:03:11] A jet filter then drops flights by ICAO Engine Type. [stated] [00:04:05]
- Inputs: target date (September 8), target bounding box `BBOX_TARGET`, sweep window `SWEEP_START_LOCAL` to `SWEEP_END_LOCAL`, snapshot interval `MINUTES_BETWEEN_SNAPSHOTS`, ICAO DOC 8643 table. [shown] [00:03:09] ![](frames/M2_000309.png)
- Outputs: flight-ID CSV, airborne flight-ID CSV (`flight_ids_airborne`), tracks CSV, track log CSV, query log. [shown] [00:03:09] [00:03:11]
- Later the outputs move to 50 GB Parquet files. [stated] [00:02:06]
- Connections: feeds S3 (track positions and altitudes for CPA and slant distance), S4 (flight tracks to lay the grid around), and S5 (interpolated positions for radial velocity). [inferred] M2-I03 S2 supplies the propeller-plane judgement and the 920 s gap that motivate this milestone. [stated] [00:03:38] S7 uses QGIS to view the tracks. [shown] [00:03:13] ![](frames/M2_000319.png)

## 5. Code, configs, formulas, and on-screen text

File: `scripts/download flightpaths v6.py`, project `Planev2`, Python 3.14 (Planev2). [shown] [00:03:09] ![](frames/M2_000309.png)

Phase 1 excerpt, transcribed from screen. Indentation reconstructed. [shown] [00:03:09] ![](frames/M2_000309.png)

```python
async def process_query(fr24, bbox: BoundingBox, ts: int, limiter: Phase1RateLimiter, ...):
    ...
    n = len(table)

    if n >= FLIGHT_LIMIT:
        log(f"{indent}{label}  ⚠ {n} flight(s), saturated at cap ({FLIGHT_LIMIT}) -- splitting north/south")
        append_query_log(bbox, ts, "truncated_split", n, True)
        done.add(key)

        mid = (bbox.south + bbox.north) / 2
        south_half = BoundingBox(south=bbox.south, north=mid, west=bbox.west, east=bbox.east)
        north_half = BoundingBox(south=mid, north=bbox.north, west=bbox.west, east=bbox.east)

        await process_query(fr24, south_half, ts, limiter, done, flights, depth + 1, local_dt)
        await process_query(fr24, north_half, ts, limiter, done, flights, depth + 1, local_dt)
        return

    log(f"{indent}{label}  ✓ {n} flight(s)")
    append_query_log(bbox, ts, "ok", n, False)
    done.add(key)
    merge_flight_ids(flights, table, ts)
    save_flight_ids(flights)


def build_timestamps():
    step = timedelta(minutes=MINUTES_BETWEEN_SNAPSHOTS)
    out = []
    t = SWEEP_START_LOCAL
    while t <= SWEEP_END_LOCAL:
        utc = t.astimezone(ZoneInfo("UTC"))
        out.append((t, utc, int(utc.timestamp())))
        t += step
    return out


async def run_phase1(fr24):
    log("=== PHASE 1: flight-ID discovery sweep ===")
    timestamps = build_timestamps()
    log(f"Sweep: {SWEEP_START_LOCAL.isoformat()} -> {SWEEP_END_LOCAL.isoformat()} local, "
        f"every {MINUTES_BETWEEN_SNAPSHOTS} min -> {len(timestamps)} timestamp(s) total")

    done = load_query_log()
    flights = load_flight_ids()
    log(f"Loaded {len(done)} previously-logged quer(y/ies), "
        f"{len(flights)} previously-known flight_id(s).\n")

    limiter = Phase1RateLimiter()
    for local_dt, utc_dt, ts in timestamps:
        await process_query(fr24, BBOX_TARGET, ts, limiter, done, flights, local_dt=local_dt)

    log(f"✓ Phase 1 done. {len(flights)} unique flight_id(s) written to {FLIGHT_IDS_CSV}")

    airborne = {fid: row for fid, row in flights.items() if float(row["max_alt"] or 0) > 0}
    ground_only = len(flights) - len(airborne)
    log(f"  {ground_only} flight_id(s) never observed airborne -- excluded")
    log(f"  {len(airborne)} flight_id(s) observed airborne -- writing to {FLIGHT_IDS_AIRBORNE_CSV}")

    with open(FLIGHT_IDS_AIRBORNE_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FLIGHT_ID_FIELDS)
        w.writeheader()
        for row in airborne.values():
            w.writerow(row)
```

Phase 2 excerpt. [shown] [00:03:11] ![](frames/M2_000311.png) [00:03:13] ![](frames/M2_000313.png)

```python
# -- Phase 2 functions ---

def load_targets():
    rows = []
    with open(FLIGHT_IDS_AIRBORNE_CSV, newline="") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    rows.sort(key=lambda r: int(r["first_seen_utc"]))
    return rows


def load_done_flights() -> set:
    """Keyed by (flightid, target_ts), NOT flightid alone -- FR24 numeric
    IDs get RECYCLED across genuinely different real-world flights over
    time. Keying on flightid alone would silently skip pulling the
    correct track for a flight that happens to share a recycled ID with
    something already logged from a totally different date."""
    done = set()
    if TRACK_LOG_CSV.exists():
        with open(TRACK_LOG_CSV, newline="") as f:
            for row in csv.DictReader(f):
                if row["status"] == "ok":
                    done.add((row["flightid"], int(float(row["target_ts"]))))
    return done


def append_track_log(flightid: str, status: str, n_points, target_ts):
    is_new = not TRACK_LOG_CSV.exists()
    with open(TRACK_LOG_CSV, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=TRACK_LOG_FIELDS)
        if is_new:
            w.writeheader()
        w.writerow({
            "flightid": flightid, "status": status,
            "n_points": n_points if n_points is not None else "",
            "target_ts": target_ts,
            "fetched_at_utc": datetime.now(ZoneInfo("UTC")).isoformat(),
        })


def append_tracks(rows: list[dict]):
    is_new = not TRACKS_CSV.exists()
    with open(TRACKS_CSV, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=TRACK_FIELDS)
        if is_new:
            w.writeheader()
        for r in rows:
            w.writerow(r)


def explode_trail(table: pl.DataFrame) -> pl.DataFrame | None:
    if "flight_trail_list" not in table.columns:
        return None
    trail = (
        table.select(["flightid", "flight_trail_list"])
        .explode("flight_trail_list")
        .unnest("flight_trail_list")
    )
    return trail


def standardize_rows(trail: pl.DataFrame) -> list[dict]:
    cols = trail.columns
    lat_col = "latitude" if "latitude" in cols else "lat"
    lon_col = "longitude" if "longitude" in cols else "lon"
    alt_col = "altitude" if "altitude" in cols else "alt"
    ts_col = "timestamp" if "timestamp" in cols else "timestamp_ms"

    out = []
    for row in trail.iter_rows(named=True):
        out.append({
            "flightid": row.get("flightid"),
            "timestamp": row.get(ts_col),
            "latitude": row.get(lat_col),
            "longitude": row.get(lon_col),
            "altitude": row.get(alt_col),
            "ground_speed": row.get("ground_speed") or row.get("spd") or row.get("gspeed"),
            "track": row.get("track") or row.get("heading"),
            "vertical_speed": row.get("vertical_speed") or row.get("vspeed"),
            "source": row.get("source"),
        })
    return out


def extract_flight_meta(table: pl.DataFrame, raw: dict):
    row = table.row(0, named=True)
    aircraft_info = raw.get("aircraft_info", {}) or {}
    ...
```

Other script names visible in the project tree, relevant to S1: `download DEM.py`, `check jets in output`, `remove jets from ca...`, `save filtered flightp...`, `flights to GPKG poi...`, `flight ID to gpkg do...`, `all flightpaths as gp...`. Editor tabs include `1.1 v8 CRS fix.py`, `1.1b v2 aggregate.py`, `1.2a v9.py`, `1.2a v10.py`. [shown] [00:03:09] ![](frames/M2_000309.png)

pyfr24 GitHub page: repo `stiles/pyfr24`, "A Python client for the Flightradar24 API with CLI support. Fetch, plot and analyze flight data with ease." Release v0.3.0 (Latest), CC0-1.0 license, 85 commits, docs at pyfr24.readthedocs.io. [shown] [00:03:04] ![](frames/M2_000304.png)

Jet filter rule, written as a formula:
keep(flight) = NOT (EngineType(typecode) == "Jet"). Unknown or missing typecodes are kept. [stated] [00:04:05]

QGIS layer panel names (truncated): `dem_...`, `all_flig...`, `prop_...`, `single ...`, `post si...`, `data en...`, `test are...`, `flightpa...`, `event s...`, `google...`, `carto`, `bing`, `norway...`. [shown] [00:03:19] ![](frames/M2_000319.png)

On-screen diagram: two cartoon planes on a timeline marked "920 sec". [shown] [00:02:56] ![](frames/M2_000256.png)

## 6. Tools and software

- Flightradar24 web map, used to illustrate ADS-B. [shown] [00:02:47]
- Flightradar24 paid API, mentioned and not used. [stated] [00:02:57]
- `pyfr24` Python package (stiles/pyfr24, v0.3.0). [shown] [00:03:04]
- Python 3.14, Polars (`pl.DataFrame`), `csv`, `asyncio`-style `async def`, `zoneinfo`. [shown] [00:03:09]
- PyCharm-style IDE, project `Planev2`. [shown] [00:03:09]
- QGIS with Google satellite basemap, used to map tracks. [shown] [00:03:13]
- A spreadsheet app showing `flight_ids_airborne`. [shown] [00:03:56]
- Audacity spectrogram view with frequency-boosted playback. [shown] [00:03:49] [stated] [00:03:38]
- A custom web spectrogram viewer with a Claude Code status bar. [shown] [00:02:42] ![](frames/M2_000242.png)
- ICAO DOC 8643 Aircraft Type Designators web page. [shown] [00:04:02]

## 7. Problems and fixes

- Problem: the dataset is large. Fix: run the scraper for a few hours. [stated] [00:03:04]
- Problem: a bounding-box query can hit a flight cap. Fix: split the box into north and south halves and recurse. [shown] [00:03:09] ![](frames/M2_000309.png)
- Problem: FR24 numeric flight IDs are recycled across different flights. Fix: key the done-log on (flightid, target_ts). [shown] [00:03:11] ![](frames/M2_000311.png)
- Problem: some flight IDs were never seen airborne. Fix: drop rows with `max_alt` not above 0. [shown] [00:03:11]
- Problem: trail column names vary (lat/latitude, spd/gspeed/ground_speed, and so on). Fix: `standardize_rows` maps them to one schema. [shown] [00:03:13] ![](frames/M2_000313.png)
- Problem: whole flight paths are downloaded, so tracks reach Hawaii and other countries. Fix: none in this milestone. Later time and range cuts handle it. [stated] [00:03:15]
- Problem: ADS-B typecode does not say propeller or jet. Fix: join to the ICAO lookup table. [stated] [00:03:55] [00:03:59]
- Problem: the lookup table has missing data. Fix: remove known jets instead of keeping known propellers. [stated] [00:04:05]

## 8. Gaps

- Exact `pyfr24` calls used (function names, auth, whether a paid FR24 token was needed for historical playback). Best guess: pyfr24's FR24 API client with an API token, since historical trails need API access. Confidence: low. [inferred] M2-I04
- Values of `BBOX_TARGET`, `FLIGHT_LIMIT`, `MINUTES_BETWEEN_SNAPSHOTS`, `SWEEP_START_LOCAL`, `SWEEP_END_LOCAL`. Best guess: a continental-US box (about 24 to 50 N, -125 to -66 E), a 5 to 15 min snapshot interval, and a sweep over the local calendar day of September 8. Confidence: low. [inferred] M2-I05
- Rate-limit settings in `Phase1RateLimiter`. Best guess: a fixed delay of about 1 s per request. Confidence: low. [inferred] M2-I06
- How the ICAO table was exported and joined. Best guess: scraped or downloaded as CSV, joined on `typecode` = Type Designator, with Engine Type "Jet" dropped. Confidence: medium. [inferred] M2-I07
- Whether turboprops count as propeller. The table shows only Jet and Piston. ICAO also lists Turboprop/Turboshaft. Best guess: only "Jet" was removed, so turboprops and helicopters stay. Confidence: medium. [inferred] M2-I08
- Recording filename date `20260913` differs from the stated September 8. Best guess: 20260913 is the export or download time of the clip, not the recording date. Confidence: medium. [inferred] M2-I09
- Track point time resolution and altitude reference. Best guess: FR24 trail points every few seconds to about a minute, altitude in feet barometric. Confidence: medium. [inferred] M2-I10
- Storage format at this stage. The code writes CSV. Parquet is mentioned elsewhere. Best guess: CSV first, converted to Parquet later for the 50 GB set. Confidence: medium. [inferred] M2-I11
- How the boosted-frequency playback was made. Best guess: an Audacity EQ or band boost around 100 to 400 Hz plus gain. Confidence: low. [inferred] M2-I12
- The sample coordinates in `flight_ids_airborne` cluster near 40.4 N, -75.7 E. This may be a test-area subset, not the full US set. Confidence: low. [inferred] M2-I13
