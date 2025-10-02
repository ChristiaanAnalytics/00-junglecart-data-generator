"""
Central configuration for the JungleCart dataset generator.
Edit SCALE or date range if you want a smaller/faster build.
"""

from pathlib import Path

# --- Paths ---
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR     = PROJECT_ROOT / "data"
OUTPUT_DIR   = DATA_DIR / "output"
RAW_DIR      = DATA_DIR / "raw"

# --- Brand & period ---
BRAND      = "JungleCart"
SEED       = 42
DATE_START = "2018-01-01"
DATE_END   = "2025-09-30"

# --- Scale knobs (lower for smoke tests; raise for larger data) ---
SCALE = {
    "n_customers": 50_000,
    "n_products":  1_200,
    "base_orders_per_day": 180,
}

# --- Channels & logistics network ---
CHANNELS = ["meta", "google", "email", "seo", "affiliate"]

WAREHOUSES = [
    {"id": 1, "name": "JHB-1", "city": "Johannesburg", "country": "ZA"},
    {"id": 2, "name": "AMS-1", "city": "Amsterdam",    "country": "NL"},
    {"id": 3, "name": "LAX-1", "city": "Los Angeles",  "country": "US"},
]

# ~8% of orders international, split by these weights (relative within intl)
INTL_DESTINATIONS = {
    "CA": 0.13, "MX": 0.08, "GB": 0.15, "DE": 0.12, "AU": 0.10,
    "JP": 0.08, "KR": 0.07, "BR": 0.10, "ZA": 0.10, "AE": 0.07
}

# --- Messy-data knobs to create realistic cleaning challenges ---
NOISE = {
    "missing_pct_phone": 0.015,     # missing phone on customer rows
    "dup_web_sessions_pct": 0.002,  # duplicated sessions (click spam)
    "tax_error_pct": 0.003,         # negative or over-high tax amounts
    "time_glitch_pct": 0.005,       # delivered_at < shipped_at
    "promo_mismatch_pct": 0.02,     # missing promotion links
    "extreme_order_pct": 0.001,     # unusually large baskets
    "neg_ship_cost_pct": 0.001,     # negative shipping costs
    "country_code_typos_pct": 0.003 # lowercase or misspelled country codes
}
