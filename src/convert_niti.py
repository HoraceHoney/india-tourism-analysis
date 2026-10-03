# convert_niti.py
# Convert the NITI Aayog tourism employment Excel file to CSV
import pandas as pd
from pathlib import Path

excel_path = Path('d:/Antigravity/class project/data/employment/tourism_employment.xlsx')
csv_path = Path('d:/Antigravity/class project/data/employment/tourism_employment.csv')

if not excel_path.exists():
    print(f'Excel file not found: {excel_path}')
else:
    try:
        df = pd.read_excel(excel_path)
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(csv_path, index=False)
        print(f'Converted to CSV: {csv_path}')
    except Exception as e:
        print(f'Error converting Excel to CSV: {e}')
