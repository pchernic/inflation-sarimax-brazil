import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf

def adf_test(series, name="Series"):
    """
    Performs Augmented Dickey-Fuller test and prints results.
    """
    result = adfuller(series.dropna())
    print(f"{name} ADF Statistic: {result[0]:.4f}")
    print(f"{name} p-value: {result[1]:.4f}")

def plot_residuals(residuals):
    fig, ax = plt.subplots(2, 1, figsize=(10, 6))

    ax[0].plot(residuals)
    ax[0].set_title("Residuals")

    plot_acf(residuals, ax=ax[1])
    ax[1].set_title("Residuals ACF")

    plt.tight_layout()
    plt.show()
