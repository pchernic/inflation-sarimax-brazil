import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_sarimax(
    y: pd.Series,
    X: pd.DataFrame,
    order=(1, 1, 1),
    seasonal_order=(1, 1, 1, 12)
):
    """
    Trains a SARIMAX model with exogenous variables.
    """
    model = SARIMAX(
        y,
        exog=X,
        order=order,
        seasonal_order=seasonal_order,
        enforce_stationarity=False,
        enforce_invertibility=False
    )

    results = model.fit(disp=False)
    return results

def forecast_sarimax(
    results,
    steps: int,
    X_future: pd.DataFrame
):
    """
    Generates forecasts and confidence intervals.
    """
    forecast = results.get_forecast(
        steps=steps,
        exog=X_future
    )
    return forecast
