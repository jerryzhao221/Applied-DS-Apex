<div align="center">

# NYC Citi Bike Demand Forecasting

*Forecasting Daily Ride Volume with Time-Series Models*

**CUSP-GX 7023 - Applied Data Science - Spring 2026**

</div>

---

## Group - Apex

Jerry Zhao - Clement Mo - Keyang Yan

---

## Abstract

We forecast daily NYC Citi Bike ride volume using full-year 2025 trip data. Three naive baselines (moving average, previous day, previous week same day) are compared against a linear regression model with calendar and lag features and a rolling ARIMA(1,1,1) model. Models are evaluated with MAE, MSE, and RMSE on two held-out test months: June 2025 and December 2025. Linear regression achieved the best average performance with MAE 14,415.1 and RMSE 19,947.3.

---

## Data

[Citi Bike System Data](https://citibikenyc.com/system-data) - 2025 NYC trips only.

Files prefixed `JC*` (Jersey City) are excluded. The analysis filters to January 1 through December 31, 2025:

- 365 daily records
- 8,759 hourly records
- 45,770,895 total rides
- 37,782,863 member rides
- 7,988,032 casual rides

---

## Repo Layout

```text
Applied-DS-Apex/
|-- ADS_code.ipynb                  main analysis notebook
|-- ADS Proposal.docx               submitted proposal
|-- aggregate_full_year_citibike.py full-year data aggregation helper
|-- data/                           aggregated CSV files
|   |-- daily_usage.csv
|   `-- hourly_usage.csv
`-- README.md
```

---

## Results

Two monthly holdout tests are used:

- June 2025 test set: train on January 8 to May 31, 2025
- December 2025 test set: train on January 8 to November 30, 2025

Average performance across the June and December test months:

| Model | MAE | RMSE |
|:--|--:|--:|
| **Linear Regression** | **14,415.1** | **19,947.3** |
| Rolling ARIMA(1,1,1) | 16,351.1 | 22,755.3 |
| Previous Day | 18,018.8 | 25,568.6 |
| Moving Average | 23,927.5 | 28,774.7 |
| Previous Week Same Day | 24,101.6 | 31,526.9 |

Monthly test performance:

| Test Month | Best Model | MAE | RMSE |
|:--|:--|--:|--:|
| June 2025 | Linear Regression | 15,229.8 | 20,781.9 |
| December 2025 | Linear Regression | 13,600.5 | 19,112.7 |

---

## Key Dates

| Milestone | Date |
|:--|:--|
| Proposal submitted | 2026-03-30 |
| Final presentation | 2026-04-30 |
| Poster due | 2026-05-08 |
