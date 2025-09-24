# 00-junglecart-data-generator

Generate a unified, realistic e-commerce “data universe” for **JungleCart** (premium outdoor & adventure gear), spanning **Jan 2018 → end-Sep 2025** with embedded macro events (COVID dip, stimulus spikes, logistics disruptions, ATT privacy), rich product taxonomy, and realistic messiness (missing values, outliers, tax errors, typos).

> Output feeds 10 analytics projects:  
> 1) RFM & churn  2) Revenue forecasting (SARIMAX/Prophet)  3) Sales & inventory planning  
> 4) Market basket  5) Customer LTV  6) Cohort retention  
> 7) Paid social dashboard  8) SEO impact  9) Multi-touch attribution  10) Social sentiment & engagement

---

## Quickstart (Anaconda Navigator → JupyterLab)

1. **Create the environment**
   - Open **Anaconda Navigator → Environments → Create**
   - Name: `junglecart`  •  Python 3.10+  
   - With `junglecart` selected → **▶ Open Terminal**:
     ```bash
     conda install -y jupyterlab pandas numpy scipy pyarrow tqdm -c conda-forge
     pip install Faker
     ```

2. **Launch JupyterLab**
   - Navigator **Home → (env dropdown: junglecart) → Launch JupyterLab**.

3. **Open the notebook**
   - In JupyterLab, open `dataset_generator.ipynb` (in this repo).
   - Run cells **1 → 10** top-to-bottom.  
   - Outputs are written under `output/` in domain subfolders.

> If you only see a “Busy” kernel: it’s generating the larger tables. You can test fast by lowering `n_customers`, `n_products`, or `base_orders_per_day` in **Cell 1**.

---

## Output layoutm
