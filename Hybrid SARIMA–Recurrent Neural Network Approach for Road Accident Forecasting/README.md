# Hybrid SARIMA–Recurrent Neural Network Approach for Road Accident Forecasting  

**Description:**  
This dataset contains daily road accident counts used for forecasting with a hybrid **SARIMA–Recurrent Neural Network (RNN)** model. The data covers a multi-year period and includes the following features:

- **Date** — date of the observation  
- **Y** — total number of accidents per day  

The dataset is stored as a **tibble (version 3.2.1)** in R, which is a modern variant of a data frame with enhanced printing and compatibility with the tidyverse.  

**Usage:**  
The data supports:

- Forecasting of daily accident counts  
- Evaluation of seasonal and temporal patterns  
- Training and validation of hybrid SARIMA–RNN models  

**Example R code to load the dataset:**

```r
library(tibble)
df <- readRDS("df_full_daily.rds")  # or your dataset filename
class(df)                     # should return: "tbl_df" "tbl" "data.frame"
```  
⬅️ [Back to main README](../README.md) |
[⬆ Back to top](#hybrid-sarimarecurrent-neural-network-approach-for-road-accident-forecasting)  