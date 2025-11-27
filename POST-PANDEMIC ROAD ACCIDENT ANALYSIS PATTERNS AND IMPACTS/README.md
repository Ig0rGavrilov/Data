# POST-PANDEMIC ROAD ACCIDENT ANALYSIS: PATTERNS AND IMPACTS

**R Version:** 4.4.2 (2024-10-31 ucrt)  

This dataset contains detailed road accident data for the Czech Republic, as well as regional area and population information, used to analyze post-pandemic trends in traffic accidents.

## Data Files

### 1. `dataSet.rds`
- **Type:** list / tibble  
- **Description:** Main dataset of road accidents.  
- **Columns (example):**

| Column               | Type   | Description |
|---------------------|--------|-------------|
| `Date`              | Date   | Date of the accident |
| `AccidentTimeFull`  | Time   | Exact time of the accident |
| `AccidentTimeHour`  | Time   | Hour of the accident |
| `Region`            | Char   | Administrative region of the accident |

**Example rows:**

| Date       | AccidentTimeFull | AccidentTimeHour | Region                    |
|------------|-----------------|-----------------|---------------------------|
| 2023-01-10 | 11:30:00        | 11:00:00        | Capital City of Prague    |
| 2023-08-30 | 06:15:00        | 06:00:00        | Capital City of Prague    |
| 2021-05-20 | NA              | 16:00:00        | Capital City of Prague    |

---

### 2. `dataRegionArea.rds`
- **Type:** list / tibble  
- **Description:** Area of each administrative region in km².  

**Example rows:**

| Region                  | Area      |
|-------------------------|-----------|
| Capital City of Prague  | 496.2679  |
| Central Bohemia         | 10945.8381|
| Hradec Kralove          | 4758.9407 |

---

### 3. `dataPopulationCSUMonthly.rds`
- **Type:** tsibble / tibble  
- **Description:** Monthly population of each region according to the Czech Statistical Office (CSU).  

**Example rows:**

| Region                  | Month       | Population |
|-------------------------|------------|-----------|
| Capital City of Prague  | 2006 Jul    | 1,183,576 |
| Capital City of Prague  | 2006 Aug    | 1,184,256 |
| Capital City of Prague  | 2006 Sep    | 1,184,951 |

---

## Usage
- Analyze temporal trends and regional patterns in post-pandemic road accidents.  
- Merge `dataSet.rds` with `dataRegionArea.rds` and `dataPopulationCSUMonthly.rds` for population- and area-normalized analyses.  
- Compatible with R `tibble`, `tsibble`, and tidyverse packages.  

**Example R code to load datasets:**

```r
df <- readRDS('data/dataSet.rds')
df_Area <- readRDS('data/dataRegionArea.rds')
df_RegionPopulationCSU <- readRDS('data/dataPopulationCSUMonthly.rds')

class(df)   # list / tibble
class(df_Area)
class(df_RegionPopulationCSU)  # tsibble / tibble  
```  

[⬆ Back to top](#post-pandemic-road-accident-analysis-patterns-and-impacts)  