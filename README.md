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


### 3. Validation
- Residual time series inspection
- Autocorrelation function (ACF)
- Ljung-Box test
- Confidence intervals for forecasts

---

## Key Results

- Inflation becomes stationary after differencing
- Exchange rate shows **statistically significant impact** on inflation
- Interest rate is **not significant in the short-term horizon**
- Strong seasonal dynamics are captured by the model
- Residuals show no significant autocorrelation

These results are **economically coherent** and consistent with inflation dynamics observed in emerging markets.

---

## Outputs

- 12-month inflation forecast
- Confidence intervals
- Residual diagnostics plots
- Fully reproducible end-to-end pipeline

---
## Project Structure

    inflation_sarimax_brazil/
    │
    ├── src/
    │   ├── fetch_macro_data.py    # API data collection (IMF + FRED)
    │   ├── load_data.py           # Data loading pipeline
    │   ├── sarimax_model.py       # Model training & forecasting
    │   ├── diagnostics.py         # Statistical tests & residual analysis
    │
    ├── main.py                    # End-to-end execution
    ├── requirements.txt
    ├── .env.example               # API key template
    └── README.md


## How to Run

```bash
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env

# Run the model
python main.py

## Why This Project Matters

This project demonstrates:

- Applied econometrics, not just machine learning
- Real-world time-series forecasting
- Use of exogenous macroeconomic drivers
- Clear statistical interpretation of results
- Clean, modular, and reproducible project structure

---

## Future Improvements

- Lag selection for exogenous variables
- Out-of-sample backtesting
- Scenario-based forecasting
- Model comparison (VAR, Bayesian approaches)

---

## Author

**Paulo Chernicharo**  



