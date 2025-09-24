# Expose key helpers so notebooks can simply:  from src import ...
from .config import (
    PROJECT_ROOT, DATA_DIR, OUTPUT_DIR, RAW_DIR,
    BRAND, SEED, DATE_START, DATE_END,
    SCALE, CHANNELS, WAREHOUSES, INTL_DESTINATIONS, NOISE
)
from .utils_io import save_csv, load_csv, ensure_dir
from .utils_dates import DATES, SEASON, seasonality_factor
