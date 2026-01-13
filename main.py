import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from src.load_data import load_macro_data
from src.diagnostics import adf_test, plot_residuals
from src.sarimax_model import train_sarimax, forecast_sarimax

# =========================
# 1. Load data
# =========================
df = load_macro_data()

# >>> ESTE TRECHO É AQUI <<<
df["usd_brl_log"] = np.log(df["usd_brl"])

# =========================
# 2. Stationarity tests
# =========================
adf_test(df["ipca"], "IPCA")
adf_test(df["interest_rate"], "INTEREST RATE")
adf_test(df["usd_brl_log"], "USD/BRL (log)")

# =========================
# 3. Train split
# =========================
train = df.loc[: "2022-12-01"]

y_train = train["ipca"]
X_train = train[["interest_rate", "usd_brl_log"]]

# =========================
# 4. Train SARIMAX
# =========================
results = train_sarimax(y_train, X_train)
print(results.summary())

# =========================
# 5. Diagnostics
# =========================
plot_residuals(results.resid)

# =========================
# 6. Forecast
# =========================
X_future = X_train.iloc[-1:].repeat(12)
X_future.index = pd.date_range(
    start=y_train.index[-1] + pd.offsets.MonthBegin(),
    periods=12,
    freq="MS"
)

forecast = forecast_sarimax(results, 12, X_future)
ci = forecast.conf_int()

# =========================
# 7. Plot
# =========================
plt.figure(figsize=(10, 5))
plt.plot(y_train, label="Observed")
plt.plot(forecast.predicted_mean, label="Forecast")

plt.fill_between(
    ci.index,
    ci.iloc[:, 0],
    ci.iloc[:, 1],
    alpha=0.3,
    label="Confidence Interval"
)

plt.title("IPCA Forecast with SARIMAX + Macroeconomic Drivers")
plt.legend()
plt.show()