"""
Date utilities: global daily date range and simple seasonality factors.
"""

import numpy as np
import pandas as pd
from .config import DATE_START, DATE_END

# Full date index for the dataset period
DATES = pd.date_range(DATE_START, DATE_END, freq="D")

def seasonality_factor(dts: pd.DatetimeIndex) -> np.ndarray:
    """
    Multiplicative weekly (+/-10%) and yearly (+/-15%) seasonality.
    Returns an array aligned to dts.
    """
    weekly = 1.0 + 0.10 * np.sin(2 * np.pi * dts.dayofweek / 7)
    annual = 1.0 + 0.15 * np.sin(2 * np.pi * dts.dayofyear / 365)
    return weekly * annual

# Pre-compute seasonality for the full dataset range
SEASON = seasonality_factor(DATES)
