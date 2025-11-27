# Accident Forecasting Using SARIMA: A Case Study on Temporal Trends from 2010 to 2024

**Description:**  
This dataset contains monthly road accident counts in the Czech Republic from **2010 to 2024**, used for **SARIMA-based forecasting** of temporal trends.  

- **File:** `df_full.rds`  
- **Class:** `tbl_df` / `tibble` (version 3.2.1)  
- **Format:** tsibble (time series tibble), 6 columns shown in example, full dataset covers all months from 2010–2024.  

**Columns:**

| Column     | Type  | Description |
|------------|-------|-------------|
| `YearMonth`| `<mth>` | Month and year of observation |
| `Total`    | `<int>` | Total number of accidents in that month |
| `Y`        | `<dbl>` | Logarithm of total accidents (`log(Total)`) |

**Example (first 6 rows):**

| YearMonth | Total | Y    |
|-----------|-------|------|
| 2010 Jan  | 4693  | 8.45 |
| 2010 Feb  | 4467  | 8.40 |
| 2010 Mar  | 4650  | 8.44 |
| 2010 Apr  | 4551  | 8.42 |
| 2010 May  | 5211  | 8.56 |
| 2010 Jun  | 5045  | 8.53 |

**Usage:**  
- Used for SARIMA modeling of temporal trends in monthly accident counts.  
- Supports visualization of long-term trends, seasonal patterns, and forecasting.  
- Compatible with R's `tsibble`, `fable`, `forecast`, and `tidyverse` packages.  

**Example R code to load the dataset:**

```r
library(tibble)
library(tsibble)

df <- readRDS("df_full.rds")
class(df)       # returns "tbl_df" "tbl" "data.frame"
head(df)        # inspect first rows
