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

We forecast daily NYC Citi Bike ride volume from **Jan–Jun 2025** trip data, comparing an **ARIMA(p, d, q)** model and a **linear regression** with calendar and lag features against naive baselines, evaluated by **MAE**, **MSE**, and **RMSE**. Full methodology, hypotheses, and results are documented in [`ADS_code.ipynb`](ADS_code.ipynb).

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
├── data/               ← processed Citi Bike parquet files
└── README.md
```

---

## Key Dates

| Milestone | Date |
|:--|:--|
| Proposal submitted | 2026-03-30 |
| Final presentation | **2026-04-30** |
| Poster due | **2026-05-08** |
