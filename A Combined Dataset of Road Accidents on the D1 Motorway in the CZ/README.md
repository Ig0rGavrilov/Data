# A Combined Dataset of Road Accidents on the D1 Motorway in the Czech Republic (2025) with Average Annual Daily Traffic (AADT) and Spatial Attributes

## Description
This dataset contains a **processed and integrated dataset** combining **road accident records**, **Average Annual Daily Traffic (AADT)**, and **road geometry attributes** for the D1 motorway in the Czech Republic for the year **2025**.

The data are structured as **linear road sectors of approximately 10 meters**, enabling **high-resolution spatial analysis** of accident occurrence in relation to **traffic intensity and road infrastructure characteristics**.

The dataset is derived from multiple publicly available sources and includes only **processed and combined data**, suitable for analysis and reproducibility.

- **Files:**
  - `D1_1_Prague-Rikovice_Combined_2025.csv`
  - `D1_2_Rikovice-Prague_Combined_2025.csv`
  - `D1_3_Border-Prerov_Combined_2025.csv`
  - `D1_4_Prerov-Border_Combined_2025.csv`

- **Format:** CSV (Comma-Separated Values)  
- **Granularity:** One row per ~10 m road sector  
- **Spatial Reference System:** EPSG:4326 (WGS 84)

---

## Dataset Structure

Each file represents a **directional segment** of the D1 motorway:

- **D1_1:** Prague → Říkovice  
- **D1_2:** Říkovice → Prague  
- **D1_3:** Czech/Polish border → Přerov  
- **D1_4:** Přerov → Czech/Polish border  

Each record corresponds to a **single road sector (~10 m)** and includes accident counts, traffic intensity, and geometric attributes.

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Index` | `<int>` | Sequential identifier of the road sector |
| `Accidents` | `<int>` | Number of police-reported accidents assigned to the sector |
| `PS` | `<int>` | AADT of passenger vehicles [veh/day] |
| `LCV` | `<int>` | AADT of light commercial vehicles [veh/day] |
| `HV` | `<int>` | AADT of heavy vehicles [veh/day] |
| `MC` | `<int>` | AADT of motorcycles [veh/day] |
| `Angle` | `<float>` | Angular change (degrees) between consecutive sectors (local curvature) |
| `Start Width` | `<float>` | Road width at the beginning of the sector (meters) |
| `End Width` | `<float>` | Road width at the end of the sector (meters) |
| `Start Lanes` | `<int>` | Number of lanes at the beginning of the sector |
| `End Lanes` | `<int>` | Number of lanes at the end of the sector |
| `Geometry` | `<str>` | Road sector geometry (LINESTRING, WKT, EPSG:4326) |

---

## Example (first rows)

| Index | Accidents | PS | LCV | HV | MC | Angle | Start Width | End Width | Start Lanes | End Lanes |
|------|-----------|----|-----|----|----|--------|--------------|------------|--------------|------------|
| 289  | 1 | 4575 | 580 | 2687 | 67 | 0.0 | 7.5 | 7.5 | 2 | 2 |
| 956  | 1 | 7499 | 838 | 3741 | 57 | 0.0 | 7.5 | 7.5 | 2 | 2 |
| 1199 | 1 | 8847 | 893 | 3794 | 85 | 0.0 | 7.4 | 7.4 | 2 | 2 |
| 1940 | 1 | 11895 | 2308 | 3161 | 145 | 0.0 | 10.5 | 10.5 | 2 | 2 |

*Note: Geometry column is omitted here for readability.*

---

## Usage

- Spatial analysis of accident distribution along the motorway  
- Analysis of relationships between **traffic intensity (AADT)** and accidents  
- Investigation of **road curvature and infrastructure effects**  
- Integration with GIS tools such as **QGIS, PostGIS, GeoPandas**  
- Feature engineering for **machine learning models**  
- Visualization using mapping libraries (e.g., Leaflet)

---

## Notes

- The dataset is derived from **publicly available sources**, but redistributed in **processed and integrated form**.  
- Only **police-reported accidents** are included, which may introduce reporting bias.  
- Minor spatial inaccuracies may exist due to source data limitations.

---

## License & Availability

The dataset is publicly available via **Mendeley Data**  
**DOI:** *[https://doi.org/10.17632/2FNM628HBP.1](https://doi.org/10.17632/2FNM628HBP.1)*

---

⬅️ [Back to main README](../README.md) |
