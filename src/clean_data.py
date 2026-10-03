# src/clean_data.py
"""Data cleaning utilities for the Indian tourism analysis project.

The script reads the raw CSV files created by `fetch_data.py`, handles
missing values, and writes cleaned versions to ``data/cleaned/``.

Missing‑value strategies used:
* **World Bank arrivals** – forward‑fill (chronological) then replace any
  remaining NaNs with the median of the known years.
* **State‑wise arrivals** – forward‑fill, then fill any leading missing values
  with 0 (assumes no arrivals before the first reported record).
* **RBI foreign‑exchange** – numeric columns are filled with the column
  median.
* **CPCB AQI** – fill missing AQI values with the state‑wise median.
* **Employment (converted CSV)** – numeric columns filled with median.

The cleaned CSV files keep the original column names and are written with a
``_cleaned`` suffix.
"""

import pandas as pd
from pathlib import Path

# ---------------------------------------------------------------------
# Helper to write a cleaned DataFrame
# ---------------------------------------------------------------------
def write_clean(df: pd.DataFrame, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Cleaned data saved to {out_path}")

# ---------------------------------------------------------------------
# 1️⃣ World Bank arrivals (numeric, time series)
# ---------------------------------------------------------------------
wb_path = Path('d:/Antigravity/class project/data/economic/worldbank_arrivals.csv')
if wb_path.exists():
    wb_df = pd.read_csv(wb_path)
    wb_df['arrivals'] = pd.to_numeric(wb_df['arrivals'], errors='coerce')
    # sort by year just in case
    wb_df = wb_df.sort_values('year')
    wb_df['arrivals'] = wb_df['arrivals'].ffill().bfill()
    median_val = wb_df['arrivals'].median()
    wb_df['arrivals'].fillna(median_val, inplace=True)
    write_clean(wb_df, Path('d:/Antigravity/class project/data/cleaned/worldbank_arrivals_cleaned.csv'))
else:
    print('World Bank CSV not found – skipping')

# ---------------------------------------------------------------------
# 2️⃣ State‑wise arrivals (time series per state)
# ---------------------------------------------------------------------
state_path = Path('d:/Antigravity/class project/data/tourism_arrivals/state_arrivals.csv')
if state_path.exists():
    state_df = pd.read_csv(state_path)
    # Expect columns: state, year, arrivals (or similar). Cast arrivals to numeric.
    if 'arrivals' in state_df.columns:
        state_df['arrivals'] = pd.to_numeric(state_df['arrivals'], errors='coerce')
        state_df = state_df.sort_values(['state', 'year'])
        state_df['arrivals'] = state_df.groupby('state')['arrivals'].ffill().fillna(0)
    write_clean(state_df, Path('d:/Antigravity/class project/data/cleaned/state_arrivals_cleaned.csv'))
else:
    print('State arrivals CSV not found – skipping')

# ---------------------------------------------------------------------
# 3️⃣ RBI foreign‑exchange earnings (numeric columns)
# ---------------------------------------------------------------------
rbi_path = Path('d:/Antigravity/class project/data/economic/rbi_forex.csv')
if rbi_path.exists():
    rbi_df = pd.read_csv(rbi_path)
    for col in rbi_df.select_dtypes(include='number').columns:
        rbi_df[col].fillna(rbi_df[col].median(), inplace=True)
    write_clean(rbi_df, Path('d:/Antigravity/class project/data/cleaned/rbi_forex_cleaned.csv'))
else:
    print('RBI CSV not found – skipping')

# ---------------------------------------------------------------------
# 4️⃣ CPCB AQI data (numeric)
# ---------------------------------------------------------------------
cpcb_path = Path('d:/Antigravity/class project/data/environment/cpcb_aqi_2023.csv')
if cpcb_path.exists():
    cpcb_df = pd.read_csv(cpcb_path)
    for col in cpcb_df.select_dtypes(include='number').columns:
        cpcb_df[col].fillna(cpcb_df[col].median(), inplace=True)
    write_clean(cpcb_df, Path('d:/Antigravity/class project/data/cleaned/cpcb_aqi_cleaned.csv'))
else:
    print('CPCB CSV not found – skipping')

# ---------------------------------------------------------------------
# 5️⃣ Employment data (converted from Excel)
# ---------------------------------------------------------------------
employment_path = Path('d:/Antigravity/class project/data/employment/tourism_employment.csv')
if employment_path.exists():
    emp_df = pd.read_csv(employment_path)
    for col in emp_df.select_dtypes(include='number').columns:
        emp_df[col].fillna(emp_df[col].median(), inplace=True)
    write_clean(emp_df, Path('d:/Antigravity/class project/data/cleaned/tourism_employment_cleaned.csv'))
else:
    print('Employment CSV not found – skipping')

# ---------------------------------------------------------------------
# End of cleaning script
# ---------------------------------------------------------------------
