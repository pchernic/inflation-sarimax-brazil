# 📈 Inflation Forecasting with SARIMAX & Macroeconomic Drivers (Brazil)

## Overview

This project implements an **econometric time-series forecasting model (SARIMAX)** to analyze and predict **Brazilian inflation (IPCA)** using key **macroeconomic exogenous variables**.

The goal is to explore **how monetary policy and exchange rate dynamics influence short-term inflation**, combining statistical rigor with real-world data pipelines.

---

## Business Question

**How do interest rates and exchange rates affect short-term inflation forecasts in Brazil?**

This project focuses on:
- Understanding inflation drivers through interpretable coefficients
- Producing statistically valid forecasts
- Demonstrating applied econometrics in a reproducible workflow

---

## Data Sources

All data is **automatically retrieved via public APIs** (no manual inputs):

- **Inflation (CPI / IPCA proxy)**  
  International Monetary Fund (IMF – IFS database)

- **Interest Rate (short-term)**  
  Federal Reserve Economic Data (FRED)

- **Exchange Rate (USD/BRL)**  
  Federal Reserve Economic Data (FRED)

This approach ensures:
- Reproducibility
- Transparency
- Real-world data engineering practices

---

## Methodology

### 1. Statistical Diagnostics
- Augmented Dickey-Fuller (ADF) tests for stationarity
- Log transformation applied to USD/BRL
- Seasonal structure evaluated (monthly frequency)

### 2. Model
- **SARIMAX (Seasonal ARIMA with Exogenous Variables)**
- Monthly seasonality (12 periods)

**Model specification:**
SARIMAX(1, 1, 1) x (1, 1, 1, 12)
Exogenous variables: Interest Rate, log(USD/BRL)




