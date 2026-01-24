# Impact of Road Geometry and Temporal Factors on Number of Vehicles in Accidents. A GIS Study

**Description:**  
This dataset contains **individual road accident records** enriched with **road geometry, damage estimates, traffic characteristics, and spatial context** for the Czech Republic in **2025**. Each accident is paired with a **300 m road segment (150 m before and 150 m after the accident location)**, enabling analysis of how **local road geometry influences accident occurrence and severity**.

- **File:** `data.parquet`  
- **Format:** Apache Parquet (Pandas DataFrame)  
- **Granularity:** One row per accident event  
- **Spatial Reference System:** EPSG:4326 (WGS 84)  

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `died` | `<float>` | Number of fatalities in the accident |
| `heavy` | `<float>` | Number of heavily injured persons |
| `soft` | `<float>` | Number of lightly injured persons |
| `total_cars` | `<int>` | Total number of vehicles involved |
| `total_damage` | `<int>` | Estimated total property damage (in CZK) |
| `lanes` | `<int>` | Number of traffic lanes at the accident location |
| `width` | `<float>` | Road width in meters |
| `date` | `<date>` | Date of the accident |
| `time` | `<time>` | Time of the accident |
| `angle` | `<float>` | Road segment angle, derived from the line geometry |
| `line_geog4326` | `<str>` | Road segment geometry (LINESTRING, EPSG:4326, WKB-encoded), 150 m before and 150 m after the accident |
| `accident_geog4326` | `<str>` | Accident point geometry (POINT, EPSG:4326, WKB-encoded) |

---

## Example (first 5 rows)

| died | heavy | soft | total_cars | total_damage | lanes | width | date       | time     | angle  |
|------|--------|------|------------|---------------|--------|--------|------------|-----------|---------|
| 0.0  | 0.0    | 0.0  | 1          | 200000        | 3      | 11.0   | 2025-09-25 | 09:00:00 | 0.5059  |
| 0.0  | 1.0    | 1.0  | 3          | 960000        | 2      | 7.5    | 2025-08-28 | 08:00:00 | -0.0228 |
| 0.0  | 0.0    | 1.0  | 4          | 100000        | 2      | 7.5    | 2025-02-27 | 07:00:00 | -0.2562 |
| 0.0  | 0.0    | 1.0  | 2          | 120000        | 2      | 7.5    | 2025-06-12 | 06:00:00 | -1.7363 |
| 0.0  | 0.0    | 2.0  | 2          | 320000        | 2      | 7.5    | 2025-08-24 | 14:00:00 | -1.3448 |

*Note: Geometry columns (`line_geog4326`, `accident_geog4326`) are omitted here for readability.*

---

## Usage

- Spatial analysis of accident distribution using **GeoPandas / GIS tools**
- Modeling relationships between **local road geometry and accident severity**
- Temporal analysis by **date and time of day**
- Feature engineering for **machine learning and deep learning models**
- Map visualization using **Leaflet, QGIS, or PostGIS**

---

⬅️ [Back to main README](../README.md) |
