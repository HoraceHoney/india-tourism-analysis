# Data Architecture & Dictionary

This directory contains the datasets for the Indian Tourism Econometric and Data Science Pipeline (covering 2022 through 2026).

---

## 📁 Directory Layout

```
data/
├── raw/                         # Untouched, original government-aligned datasets (Data Before)
│   ├── 01_district_wise_tourist_footfall_2022_2024.csv
│   ├── 02_nidhi_hospitality_establishments_registry.csv
│   ├── 03_asi_protected_monuments_inventory.csv
│   ├── 04_inbound_tourist_survey_microdata_2023_2024.csv
│   ├── 05_airport_passenger_traffic_monthly_2022_2024.csv
│   ├── 06_annual_macro_overview_2022_2024.csv
│   ├── 07_country_wise_fta_summary_2022_2024.csv
│   ├── 08_state_ut_consolidated_summary_2022_2023.csv
│   └── README.md
│
└── cleaned/                     # Fully cleaned, typed, and feature-engineered datasets (Data After)
    ├── 01_district_wise_tourist_footfall_cleaned.csv
    ├── 02_nidhi_hospitality_establishments_cleaned.csv
    ├── 03_asi_protected_monuments_cleaned.csv
    ├── 04_inbound_tourist_survey_cleaned.csv
    ├── 05_airport_passenger_traffic_cleaned.csv
    ├── 06_annual_macro_overview_cleaned.csv
    ├── 07_country_wise_fta_cleaned.csv
    ├── 08_state_ut_consolidated_cleaned.csv
    └── unified_district_master_2026.csv   # Unified master profile merging Footfall + Hospitality + Monuments
```

---

## 🔍 Dataset Catalog

| # | Raw File Name | Cleaned File Name | Scope / Granularity | Records | Key Source Equivalent |
|---|---|---|---|:---:|---|
| 1 | `01_district_wise_tourist_footfall_2022_2024.csv` | `01_district_wise_tourist_footfall_cleaned.csv` | 474 Districts × 5 Years (2022–2026) | 2,380 | MoT / State Tourism Boards |
| 2 | `02_nidhi_hospitality_establishments_registry.csv` | `02_nidhi_hospitality_establishments_cleaned.csv` | Classified Units & Star Hotels (through 2026) | 1,650 | MoT NIDHI / HRACC Portal |
| 3 | `03_asi_protected_monuments_inventory.csv` | `03_asi_protected_monuments_cleaned.csv` | Centrally Protected National Monuments | 1,200 | Archaeological Survey of India (ASI) |
| 4 | `04_inbound_tourist_survey_microdata_2023_2024.csv` | `04_inbound_tourist_survey_cleaned.csv` | International Airport Exit Survey Microdata | 2,500 | MoT International Exit Survey / BOI |
| 5 | `05_airport_passenger_traffic_monthly_2022_2024.csv` | `05_airport_passenger_traffic_cleaned.csv` | 40 Airports × 60 Months (2022–2026) | 2,400 | AAI / DGCA Monthly Reports |
| 6 | `06_annual_macro_overview_2022_2024.csv` | `06_annual_macro_overview_cleaned.csv` | National Economic Overview (2022–2026) | 5 | MoT PIB Annual Bulletins |
| 7 | `07_country_wise_fta_summary_2022_2024.csv` | `07_country_wise_fta_cleaned.csv` | Top 31 Source Nationalities (2022–2026) | 31 | Bureau of Immigration (BOI) |
| 8 | `08_state_ut_consolidated_summary_2022_2023.csv` | `08_state_ut_consolidated_cleaned.csv` | 36 States & Union Territories (2022–2026) | 36 | India Tourism Statistics (ITS) |
| M | — | `unified_district_master_2026.csv` | 2026 Cross-Domain District Master Profile | 474 | Relational Merge (1 + 2 + 3) |

---

## 🛠️ Data Cleaning & Imputation Pipeline

1. **Nullable Numeric Casting**: Cast numeric count columns with missing values to Pandas nullable `Int64` (`Foreign_Visitors`, `Registered_Hotels_Count`, `Reported_Tourist_Complaints`) to avoid float distortion.
2. **Hierarchical Categorical Imputation**:
   - `Pincode`: Imputed by the modal pincode of the corresponding `District_City` group; unresolvable entries tagged as `'Unknown'`.
   - `Star_Classification`: Added `'Unclassified'` category to preserve category integrity without inventing unearned star tiers.
   - `Audit_Quality_Score`: Imputed by conditional accommodation median, with an explicit `Audit_Score_Was_Missing` indicator flag.
3. **Structural Zero Handling**:
   - Non-ticketed ASI monuments imputed with ₹0 entry fees (rather than arbitrary medians).
   - Purely domestic and regional airfields assigned 0 for international passenger movements.
   - Remote districts without international checkpoints assigned 0 foreign visitors.
