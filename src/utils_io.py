"""
Lightweight I/O helpers for saving and loading dataset CSVs.
"""

from pathlib import Path
import pandas as pd
from .config import OUTPUT_DIR

def ensure_dir(path: Path | str) -> None:
    """Create directory if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)

def save_csv(df: pd.DataFrame, rel_path: str) -> None:
    """
    Save a DataFrame to CSV under data/output/.
    Example: save_csv(df, "core/customers.csv")
    """
    full = Path(OUTPUT_DIR) / rel_path
    ensure_dir(full.parent)
    df.to_csv(full, index=False)
    print(f"✅ wrote {rel_path} — {len(df):,} rows")

def load_csv(rel_path: str, parse_dates=None) -> pd.DataFrame:
    """
    Load a CSV from data/output/ and optionally parse date columns.
    """
    full = Path(OUTPUT_DIR) / rel_path
    if not full.exists():
        raise FileNotFoundError(f"Expected file not found: {full}")
    return pd.read_csv(full, parse_dates=parse_dates)
