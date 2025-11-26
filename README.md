# Source data for the Articles and Conference papers:  

## Articles  

### POST-PANDEMIC ROAD ACCIDENT ANALYSIS PATTERNS AND IMPACTS  

**Abstract**: This study analyzes the impact of COVID-19 restrictions on road accident trends in the Czech Republic from 2015 to 2024, utilizing a comprehensive
dataset of over one million recorded accidents. The research highlights a significant decline in accident rates during the strict lockdown periods, correlating reduced
mobility with fewer traffic incidents. As restrictions eased, accident rat es rose again, revealing seasonal variations and regional disparities, particularly in urban
areas like Prague. Findings suggest that the pandemic has reshaped commuting patterns and could influence future traffic management strategies. The analysis
underscores the need for targeted policies to enhance road safety, especially during high-risk seasons.  

**Keywords**: COVID-19, Road accidents, Traffic safety, Lockdown effects, Urban mobility, Seasonal trends, Data analysis  
**DOI**: [10.14311/NNW.2024.34.017](https://doi.org/10.14311/NNW.2024.34.017)  
**Authors**: I. Gavrilov ([ORCID](https://orcid.org/0009-0006-5341-8373))  
**Data**: [Data](https://github.com/Ig0rGavrilov/Data/tree/main/POST-PANDEMIC%20ROAD%20ACCIDENT%20ANALYSIS%20PATTERNS%20AND%20IMPACTS)  

### Hybrid SARIMA–Recurrent Neural Network Approach for Road Accident Forecasting  

**Abstract**: This study investigates the forecasting of daily road traffic accidents using time series models, with a focus on enhancing prediction accuracy through hybrid methodologies. We employ a Seasonal Autoregressive Integrated Moving Average (SARIMA) model to capture linear and seasonal patterns in accident data from 2010 to 2023. To address potential non-linearities, we extend the approach by modelling SARIMA residuals using Recurrent Neural Networks (RNNs), including bidirectional RNN (BiRNN) and Long Short-Term Memory (LSTM) variants, to develop a hybrid SARIMA-RNN framework. The hybrid model integrates SARIMA forecasts with RNN-based residual predictions to improve overall accuracy.
The unidirectional LSTM outperformed other RNN architectures, achieving the lowest RMSE (0.184) and MAPE (1.0966%), confirming its effectiveness in modelling temporal dependencies. A hybrid SARIMA-LSTM model was also evaluated to enhance the prediction of residuals; however, for one-step-ahead forecasting, it did not improve accuracy compared to the baseline SARIMA, with only minor increases in RMSE and MAPE.  

**Keywords**: Road accidents, time series forecasting, SARIMA, recurrent neural networks (RNN), hybrid models, BiRNN, BiLSTM, transport safety, residual modelling  
**DOI**: [TBD]()  
**Authors**:  I. Gavrilov ([ORCID](https://orcid.org/0009-0006-5341-8373)), P. Hrubeš ([ORCID](https://orcid.org/0000-0002-8823-0673)), E. Pelikan  
**Data**: [Data](https://github.com/Ig0rGavrilov/Data/tree/main/Hybrid%20SARIMA%E2%80%93Recurrent%20Neural%20Network%20Approach%20for%20Road%20Accident%20Forecasting)  

### Accident Forecasting Using SARIMA A Case Study on Temporal Trends from 2010 to 2024  

**Abstract**: Road traffic accidents are a critical public safety concern, with global disparities in accident rates driven by variations in law enforcement, infrastructure quality, and emergency response. This study explores the application of Seasonal Autoregressive Integrated Moving Average (SARIMA) models to forecast monthly road traffic accidents from January 2010 to October 2024. Using a dataset of over 1.2 million accidents, the research identifies strong seasonal trends and evaluates the impact of COVID-19-related restrictions on traffic patterns. Following data transformation and stationarity testing, SARIMA models were optimized based on criteria such as AIC, AICc, BIC, and RMSE. The findings demonstrate the efficacy of SARIMA in accurately capturing complex temporal dynamics, offering valuable insights for traffic safety planning and policy formulation. This paper underscores the importance of robust forecasting tools in mitigating future road accidents and enhancing global road safety strategies.  

**Keywords**: SARIMA, road accidents, time-series forecasting, seasonal trends, traffic safety  
**DOI**: [TBD]()  
**Authors**:  I. Gavrilov ([ORCID](https://orcid.org/0009-0006-5341-8373)), E. Pelikan  
**Data**: [Data](https://github.com/Ig0rGavrilov/Data/tree/main/Accident%20Forecasting%20Using%20SARIMA%20A%20Case%20Study%20on%20Temporal%20Trends%20from%202010%20to%202024)  

### A Neural Network–Based Framework for Identifying Hazardous Road Segments Using Geometrical Road Attributes

**Abstract**: Accurate identification of hazardous road segments is essential for improving road safety and prioritising preventive interventions. This study proposes a neural network–based framework for predicting hazardous road segments by leveraging detailed geometrical properties of roads, including lane number, lane width, and curvature. The proposed framework was applied to the D1 highway in the Czech Republic, using geospatial data and reported road accidents from 2024.
The road geometry was divided into 10 m sectors, from which sequences of 300 m were generated to form input for a Long Short-Term Memory (LSTM) network. The model was trained using a weighted binary cross-entropy loss function to address class imbalance, where hazardous segments represented only 29.2% of samples. The trained model demonstrated strong predictive performance, achieving a weighted F1 score of 0.895 and a macro F1 score of 0.906, which effectively distinguished between hazardous and non-hazardous highway segments.
The results demonstrate that integrating detailed road attributes within an LSTM-based framework can effectively capture spatial dependencies and non-linear relationships associated with accident occurrence. The framework provides a scalable approach for identifying high-risk segments across various road types, offering valuable support for data-driven decision-making in transportation safety management.  

**Keywords**: Road accidents; LSTM; Hazardous road segments; Road geometry; Traffic safety prediction  
**DOI**: [TBD]()  
**Authors**:  I. Gavrilov ([ORCID](https://orcid.org/0009-0006-5341-8373)), P. Hrubeš ([ORCID](https://orcid.org/0000-0002-8823-0673)), E. Pelikan  
**Data**: [Data](https://github.com/Ig0rGavrilov/Data/tree/main/A%20Neural%20Network%E2%80%93Based%20Framework%20for%20Identifying%20Hazardous%20Road%20Segments%20Using%20Geometrical%20Road%20Attributes)  

## Conference papers

### PROSTOROVÁ ANALÝZA MÍST DOPRAVNÍCH NEHOD NA DÁLNICÍCH I. A II. TŘIDY V ČESKÉ REPUBLICE

**Abstract**: Tento článek se zaměřuje na statistickou analýzu vzdálenosti mezi místy dopravních nehod na dálnicíchprvní a druhé třídy v České republice. Analyzovaná data zahrnují široké spektrum dopravních nehod, kterése staly na těchto komunikacích v období 2007-2024. Cílem je identifikovat oblasti se zvýšenou koncentracíincidentů, které vyžadují další bezpečnostní opatření. Využití lokalizace nehod v GIS poskytuje přehled oprostorovém rozmístění nehod a pomáhá odhalit segmenty silnic, kde je pravděpodobnost nehody vyšší.Klasifikace typu silniční komunikace na základě vektorových dat z OpenStreetMap přispívá k rozlišení mezidálnicemi první a druhé třídy. V analýze se statisticky hodnotí vzdálenosti mezi místy nehod. Výsledky studieslouží jako podklad pro tvorbu preventivních opatření zaměřených na snížení rizika nehod na klíčovýchúsecích české dálniční sítě.

**Keywords**: Dopravní nehody; GIS; prostorová analýza; Modelování; Vizualizace  
**DOI**: [10.31490/9788024847955-4](https://doi.org/10.31490/9788024847955-4)  
**Authors**:  I. Gavrilov ([ORCID](https://orcid.org/0009-0006-5341-8373))  
**Data**: [Data](https://github.com/Ig0rGavrilov/Data/tree/main/PROSTOROV%C3%81%20ANAL%C3%9DZA%20M%C3%8DST%20DOPRAVN%C3%8DCH%20NEHOD%20NA%20D%C3%81LNIC%C3%8DCH%20I.%20A%20II.%20T%C5%98IDY%20V%20%C4%8CESK%C3%89%20REPUBLICE)  