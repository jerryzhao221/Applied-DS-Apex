<div align="center">

# NYC Citi Bike Demand Forecasting

*Forecasting Daily Ride Volume with Time-Series Models*

**CUSP-GX 7023 · Applied Data Science · Spring 2026**

</div>

---

## Group · **Apex**
Jerry Zhao · Clement Mo · Keyang Yan

---

## Abstract

We forecast daily NYC Citi Bike ride volume from **Jan–Jun 2025** trip data. Three naive baselines (moving average, previous day, previous week same day) are compared against a **linear regression** with calendar and lag features and an **ARIMA(1,1,1)** model, evaluated by **MAE**, **MSE**, and **RMSE**. Linear regression achieved the best performance (MAE 15,255 · RMSE 20,795). Full methodology, hypotheses, and results are documented in [`ADS_code.ipynb`](ADS_code.ipynb).

---

## Data

[Citi Bike System Data](https://citibikenyc.com/system-data) — 2025 NYC trips only.
Files prefixed `JC*` (Jersey City) are excluded.

---

## Repo Layout

```
Applied-DS-Apex/
├── ADS_code.ipynb      ← main analysis notebook
├── ADS Proposal.docx   ← submitted proposal
├── data/               ← aggregated CSV files (daily_usage.csv, hourly_usage.csv)
└── README.md
```

---

## Results

| Model | MAE | RMSE |
|:--|--:|--:|
| Moving Average | 25,207 | 30,518 |
| Previous Day | 19,929 | 28,648 |
| Previous Week Same Day | 23,669 | 32,190 |
| **Linear Regression** | **15,255** | **20,795** |
| ARIMA(1,1,1) | 26,391 | 31,675 |

Test set: June 2025 (30 days).


---

## Key Dates

| Milestone | Date |
|:--|:--|
| Proposal submitted | 2026-03-30 |
| Final presentation | **2026-04-30** |
| Poster due | **2026-05-08** |
