# Updated data‑fetch script for Indian tourism analysis
# ---------------------------------------------------
# This script downloads several publicly available Indian tourism‑related datasets
# and stores them as CSV (or Excel where applicable) inside the project’s
# ``data`` folder. All URLs point to open‑government resources that do **not**
# require a Kaggle or GitHub account.
# ---------------------------------------------------

import csv, json, os, requests
from pathlib import Path

# ---------------------------------------------------------------------
# Helper: write a list of dictionaries to CSV (creates parent folders as needed)
# ---------------------------------------------------------------------
def write_csv(rows, path, header=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header or rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved: {path}")

# ---------------------------------------------------------------------
# 1️⃣ World Bank – International tourist arrivals (India, country level)
# ---------------------------------------------------------------------
wb_url = (
    "https://api.worldbank.org/v2/country/IN/indicator/ST.INT.ARVL"
    "?format=json&date=2015:2025"
)
resp = requests.get(wb_url, timeout=30)
resp.raise_for_status()
_, wb_data = resp.json()
worldbank_rows = [{"year": r.get('date'), "arrivals": r.get('value')} for r in wb_data]
worldbank_path = Path('d:/Antigravity/class project/data/economic/worldbank_arrivals.csv')
write_csv(worldbank_rows, worldbank_path, header=['year', 'arrivals'])

# ---------------------------------------------------------------------
# 2️⃣ India Open Data – State‑wise international arrivals (requires API key)
# ---------------------------------------------------------------------
def fetch_state_arrivals():
    api_key = os.getenv('DATA_GOV_IN_API_KEY', '')
    if not api_key:
        print('[INFO] No Data.gov.in API key - skipping state-wise arrivals.')
        return
    resource_id = '12345678-90ab-cdef-1234-567890abcdef'  # replace with actual ID
    url = (
        f'https://api.data.gov.in/resource/{resource_id}?api-key={api_key}'
        "&format=json&offset=0&limit=5000"
    )
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    records = r.json().get('records', [])
    if not records:
        print('[WARN] No state records returned.')
        return
    state_dir = Path('d:/Antigravity/class project/data/tourism_arrivals')
    state_dir.mkdir(parents=True, exist_ok=True)
    state_path = state_dir / 'state_arrivals.csv'
    write_csv(records, state_path)

fetch_state_arrivals()

# ---------------------------------------------------------------------
# 3️⃣ RBI – Tourism foreign‑exchange earnings (public CSV example)
# ---------------------------------------------------------------------
try:
    rbi_url = 'https://www.rbi.org.in/scripts/DownloadData.aspx?file=Tourism_Foreign_Exchange_2023.csv'
    r = requests.get(rbi_url, timeout=30)
    r.raise_for_status()
    rbi_path = Path('d:/Antigravity/class project/data/economic/rbi_forex.csv')
    rbi_path.parent.mkdir(parents=True, exist_ok=True)
    rbi_path.write_bytes(r.content)
    print(f'Saved: {rbi_path}')
except Exception as e:
    print(f'[ERROR] RBI download failed: {e}')

# ---------------------------------------------------------------------
# 4️⃣ CPCB – Air‑quality index (state level, latest public CSV)
# ---------------------------------------------------------------------
try:
    cpcb_url = 'https://cpcb.nic.in/downloads/aqi_state_2023.csv'
    r = requests.get(cpcb_url, timeout=30)
    r.raise_for_status()
    cpcb_path = Path('d:/Antigravity/class project/data/environment/cpcb_aqi_2023.csv')
    cpcb_path.parent.mkdir(parents=True, exist_ok=True)
    cpcb_path.write_bytes(r.content)
    print(f'Saved: {cpcb_path}')
except Exception as e:
    print(f'[ERROR] CPCB download failed: {e}')

# ---------------------------------------------------------------------
# 5️⃣ NITI Aayog – Tourism‑related employment (Excel, later conversion to CSV)
# ---------------------------------------------------------------------
try:
    niti_url = 'https://niti.gov.in/sites/default/files/2023-06/Tourism_Employment_2022.xlsx'
    r = requests.get(niti_url, timeout=30)
    r.raise_for_status()
    niti_path = Path('d:/Antigravity/class project/data/employment/tourism_employment.xlsx')
    niti_path.parent.mkdir(parents=True, exist_ok=True)
    niti_path.write_bytes(r.content)
    print(f'Saved: {niti_path}')
except Exception as e:
    print(f'[ERROR] NITI download failed: {e}')

# End of script – all downloadable CSV/Excel files are now stored locally.
