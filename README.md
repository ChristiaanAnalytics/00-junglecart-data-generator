# 🏕️ JungleCart Synthetic E-Commerce Dataset

A **realistic, end-to-end synthetic data generator** that models **JungleCart**,  
a premium global retailer of outdoor & adventure equipment (think **REI.com**).  
The dataset spans **January 2018 → September 2025** and is designed for a full portfolio of **10 analytics projects**—from classical RFM segmentation to modern digital-marketing attribution.

---

## ✨ Key Features

| Area | Highlights |
|------|-----------|
| **Rich Business Universe** | Customers, orders, products, inventory, marketing campaigns, web sessions, paid-social & SEO metrics, email engagement, Facebook & Instagram analytics. |
| **7-Year Timeline** | Covers pre-COVID growth, 2020 pandemic slump, stimulus spikes, post-pandemic e-commerce boom and supply-chain disruptions through 2025. |
| **Real-World Messiness** | Outliers, missing values, typos, inconsistent country codes, occasional tax errors and time-glitches to practise data-cleaning. |
| **Global Scope** | Orders ship worldwide (Canada, UK, Germany, Australia, Japan, South Korea, Brazil, South Africa, UAE) with local VAT and customs quirks. |
| **Portfolio-Ready** | Data supports 10 different analytics projects: RFM & churn, forecasting, market-basket analysis, lifetime-value modelling, SEO & paid-social dashboards, multi-touch attribution, and more. |
| **Fully Reproducible** | One-click generation in JupyterLab using a single Conda environment. |

---

## 📂 Repository Structure

junglecart-dataset/
├─ README.md
├─ environment.yml
├─ Makefile
├─ notebooks/
│   └─ 01_build_junglecart_dataset.ipynb
├─ src/
│   ├─ init.py
│   ├─ config.py
│   ├─ utils_io.py
│   ├─ utils_dates.py
│   └─ qa_checks.py
├─ data/
│   ├─ raw/
│   └─ output/
│       ├─ core/
│       ├─ inventory/
│       ├─ marketing/
│       ├─ pricing_promos/
│       ├─ social/
│       └─ meta/
└─ docs/
├─ dataset_overview.md
└─ lineage.png

---

## 🛠️ Quickstart

### 1️⃣ Install & activate the environment
```bash
conda env create -f environment.yml
conda activate junglecart

2️⃣ Launch JupyterLab
	•	Recommended: open Anaconda Navigator → Environments → junglecart → Launch JupyterLab,
or from the command line:

make lab



3️⃣ Generate the dataset

Open notebooks/01_build_junglecart_dataset.ipynb and Run All.
All CSV/Parquet files will be written to data/output/.

4️⃣ (Optional) Run QA checks

make qa

This runs the integrity checks in src/qa_checks.py (foreign-key consistency, basic stats).

⸻

📊 Analytics Projects Enabled

The generated data is purposely designed to power ten portfolio projects:
	1.	Customer RFM & Churn Analysis – segment customers and predict churn.
	2.	Revenue Trend Forecasting – SARIMAX & Prophet sales forecasts with pandemic shocks.
	3.	Sales & Inventory Planning – demand forecasting with stock-out risk.
	4.	Market-Basket Analysis – association rules & product bundling.
	5.	Customer Lifetime Value Modelling – probabilistic LTV estimation.
	6.	Cohort & Retention Analysis – revenue cohorts & retention curves.
	7.	Paid-Social Performance Dashboard – Meta Ads ROI & reach with ATT privacy impact.
	8.	Google Analytics & SEO Impact – web traffic, keyword & content performance.
	9.	Marketing Attribution & ROI Modelling – multi-touch attribution across channels.
	10.	Social Sentiment & Engagement Analysis – Facebook & Instagram profile/post analytics.

Each project can live in its own GitHub repo or inside a projects/ folder that symlinks to data/output/.

⸻

🌍 Macro Events Modelled

The time-series data reflects major e-commerce shocks:
	•	Jun 2018 – Wayfair decision: gradual US state-level sales-tax changes & tax-calc errors.
	•	Mar–May 2020 – COVID shock: sharp order drop & shipping delays.
	•	2020–21 – Stimulus spikes: US stimulus cheques boosting orders/AOV.
	•	Q4 2020–Q2 2021 – Post-pandemic boom.
	•	Mar 2021 – Suez Canal blockage: 7–21 day inbound delays.
	•	Apr 2021 – iOS 14.5 ATT: paid-social tracking drop; more unattributed traffic.
	•	Jul 2021 – EU VAT IOSS regime.
	•	2021–22 – US West Coast port congestion.
	•	Feb 2022 – Russia–Ukraine war: fuel surcharges; RU/UA shipping suspended.
	•	2021–23 – Global inflation & strong USD: COGS ↑, MSRP hikes, promo intensity ↑.
	•	Mid-2023–Early 2024 – Panama Canal drought: +5–10 days transit.
	•	Nov 2023–2025 – Red Sea disruptions: +10–20 days ocean transit.
	•	Annual: Lunar New Year inventory pull, Black-Friday/Cyber-Monday surge.

⸻

🗃️ Data Overview

Core Tables

File	Description	Primary Keys / Foreign Keys
core/customers.csv	Customer profiles (age, gender, country)	PK: customer_id
core/orders.csv	Orders with timestamps, shipping & tax details	PK: order_id; FK: customer_id
core/order_items.csv	Line items per order	PK: order_item_id; FK: order_id, product_id
core/products.csv	Full product catalogue with rich outdoor/adventure taxonomy	PK: product_id; FK: category_id
inventory/warehouses.csv	Warehouse locations	PK: warehouse_id
inventory/stock_movements.csv	Inventory in/out movements	PK: movement_id; FK: product_id, warehouse_id
…	…	…

(See docs/dataset_overview.md for the full data dictionary.)

⸻

🧩 Extending or Customising
	•	Scale up: edit SCALE in src/config.py (e.g. increase n_customers).
	•	Add noise: tweak NOISE percentages for more or fewer data-cleaning challenges.
	•	Refactor: move code from the notebook into modules in src/ for production pipelines.

⸻

🧪 Quality Assurance
	•	Foreign-key checks: make qa or from src.qa_checks import print_report.
	•	Descriptive stats: order volumes by year, average items per order, etc.
	•	Cross-table consistency: built-in tests under tests/ (if you add them).

⸻

📝 License

MIT License – feel free to use or adapt for your own projects.

⸻

🙋‍♀️ Credits

Built by [Your Name] to showcase advanced data-engineering and analytics skills.


