import os
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv

load_dotenv()

FRED_API_KEY = os.getenv("FRED_API_KEY")
fred = Fred(api_key=FRED_API_KEY)

FRED_SERIES = {
    "ipca": "CPALTT01BRM657N",        # CPI Brazil (monthly)
    "interest_rate": "IRSTCI01BRM156N",
    "usd_brl": "DEXBZUS"
}


def fetch_macro_data() -> pd.DataFrame:
    data = {}

    for name, series_id in FRED_SERIES.items():
        s = fred.get_series(series_id)
        s.index = pd.to_datetime(s.index)
        data[name] = s

    df = pd.concat(data.values(), axis=1)
    df.columns = data.keys()

    df = df.asfreq("MS").dropna()
    return df
