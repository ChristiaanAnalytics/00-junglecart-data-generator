"""
Quick QA checks to validate dataset integrity after generation.
"""

import pandas as pd
from .utils_io import load_csv

def fk_order_items() -> dict:
    """
    Validate that order_items foreign keys exist in orders and products.
    Returns a dict with counts of missing keys (0 = all good).
    """
    oi     = load_csv("core/order_items.csv")
    orders = load_csv("core/orders.csv", parse_dates=["order_date"])
    prods  = load_csv("core/products.csv")

    miss_orders = set(oi["order_id"].unique()) - set(orders["order_id"].unique())
    miss_prods  = set(oi["product_id"].unique()) - set(prods["product_id"].unique())

    return {
        "order_items→orders_missing": len(miss_orders),
        "order_items→products_missing": len(miss_prods),
    }

def basic_stats() -> dict:
    """
    Simple descriptive stats: orders per year and average items per order.
    """
    orders = load_csv("core/orders.csv", parse_dates=["order_date"])
    oi     = load_csv("core/order_items.csv")

    per_year = orders["order_date"].dt.year.value_counts().sort_index().to_dict()
    avg_items_per_order = round(len(oi) / max(1, orders["order_id"].nunique()), 2)

    return {
        "orders_per_year": per_year,
        "avg_items_per_order": avg_items_per_order
    }

def print_report():
    """Pretty-print a minimal QA report at the end of your notebook."""
    fk = fk_order_items()
    stats = basic_stats()

    print("==== JungleCart QA Report ====")
    print("Foreign Keys:")
    for k, v in fk.items():
        print(f"  {k}: {'OK' if v==0 else v}")
    print("\nStats:")
    print("  Orders per year:")
    for y, n in sorted(stats["orders_per_year"].items()):
        print(f"    {y}: {n:,}")
    print(f"  Avg items per order: {stats['avg_items_per_order']:.2f}")
