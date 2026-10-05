# 🇮🇳 India Tourism Analytics & Econometric Pipeline (2022–2026)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458.svg)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-blueviolet.svg)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An end-to-end data engineering, statistical profiling, and econometric modeling repository analyzing official Indian tourism dynamics across **474 districts**, **1,650 hospitality establishments**, **1,200 centrally protected monuments**, **2,500 exit survey respondents**, and **40 civil aviation gateways** spanning **2022 through 2026**.

---

## 📌 Project Overview

This repository demonstrates rigorous data science workflows on multi-tiered, real-world public sector tourism data from official government departments (Ministry of Tourism, NIDHI, Archaeological Survey of India, Bureau of Immigration, and DGCA/AAI).

### Key Architectural Highlights
- **Immutable Raw Data Architecture**: Original public data preserved in `data/raw/` with zero destructive modifications.
- **Domain-Aware Imputation**: Statistically robust missing-value treatment (hierarchical modal pincodes, category-bounded medians, structural zero logic for non-ticketed heritage monuments and domestic-only airfields).
- **Relational Data Harmonization**: Unified cross-domain master dataset (`unified_district_master_2026.csv`) linking district footfalls with hotel room capacities and UNESCO monument clusters.
- **Modular Notebook Architecture**: Full analytical journey split into dedicated, self-contained Jupyter notebooks in `python/`, accompanied by automated CLI pipeline scripts in `src/`.
- **Publication-Ready Artifacts**: Visualizations exported at 300 DPI (`results/plots/`) and summary econometric tables (`results/tables/`).

---

## 🗂️ Professional Repository Structure

```
india-tourism-analysis/
├── README.md                                    # Root project documentation & portfolio showcase
├── requirements.txt                             # Production & analysis dependencies
├── .gitignore                                   # Standard Python, Jupyter, and OS gitignore
│
├── data/                                        # Data architecture root
│   ├── README.md                                # Comprehensive data dictionary & methodology
│   ├── raw/                                     # Original untouched datasets ("Data Before")
│   │   ├── 01_district_wise_tourist_footfall_2022_2024.csv
│   │   ├── 02_nidhi_hospital6_annual_macro_overview_2022_2024.csv
│   │   ├── 03_asi_protected_monuments_inventory.csv
│   │   ├── 04_inbound_tourist_survey_microdata_2023_2024.csv
│   │   ├── 05_airport_passenger_traffic_monthly_2022_2024.csv
│   │   ├── 06_annual_macro_overview_2022_2024.csv
│   │   ├── 07_country_wise_fta_summary_2022_2024.csv
│   │   └── 08_state_ut_consolidated_summary_2022_2023.csv
│   │
│   └── cleaned/                                 # Cleaned, optimized & engineered datasets ("Data After")
│       ├── 01_district_wise_tourist_footfall_cleaned.csv
│       ├── 02_nidhi_hospitality_establishments_cleaned.csv
│       ├── 03_asi_protected_monuments_cleaned.csv
│       ├── 04_inbound_tourist_survey_cleaned.csv
│       ├── 05_airport_passenger_traffic_cleaned.csv
│       ├── 06_annual_macro_overview_cleaned.csv
│       ├── 07_country_wise_fta_cleaned.csv
│       ├── 08_state_ut_consolidated_cleaned.csv
│       └── unified_district_master_2026.csv     # 2026 Unified District Master Profile
│
├── python/                                      # Modular Jupyter Notebooks
│   ├── 00_master_pipeline.ipynb                 # Complete end-to-end reproducible pipeline
│   ├── 01_data_ingestion_and_inspection.ipynb   # Ingestion, schema audit, and initial profiling
│   ├── 02_datatype_optimization.ipynb           # Nullable integers, ordered categories, timestamps
│   ├── 03_missing_value_imputation.ipynb        # Domain-aware median, mode, and structural fallbacks
│   ├── 04_feature_engineering.ipynb             # Spend velocity, NPS sentiment, airport flight loads
│   ├── 05_relational_merge.ipynb                # Master district profile multi-table join
│   ├── 06_exploratory_and_econometric_analysis.ipynb # Policy queries, rankings, and segmentations
│   └── 07_visualizations_and_dashboards.ipynb   # Standalone publication-grade charts
│
├── results/                                     # Output artifacts
│   ├── summary_findings.md                      # Detailed executive findings & econometric insights
│   ├── plots/                                   # High-resolution (300 DPI) publication figures
│   │   ├── 01_monthly_airport_passenger_movements.png
│   │   ├── 02_inbound_spend_vs_experience.png
│   │   ├── 03_top_10_states_footfall_2026.png
│   │   ├── 04_district_infrastructure_correlation_matrix.png
│   │   └── 05_room_tariff_distribution_by_accommodation.png
│   │
│   └── tables/                                  # Derived analytical summary tables (CSV)
│       ├── 01_top_10_inbound_destinations_2026.csv
│       ├── 02_tourism_category_performance_2026.csv
│       ├── 03_inbound_spending_velocity_nps_summary.csv
│       ├── 04_top_10_gateway_airports_2026.csv
│       └── 05_hospitality_market_segmentation.csv
│
└── src/                                         # Reusable automated Python scripts
    ├── clean_data.py                            # CLI data cleaning module
    ├── fetch_data.py                            # Open API / portal fetch pipeline
    └── convert_niti.py                          # NITI Aayog Excel-to-CSV processor
```

---

## 📊 Summary of Core Econometric Insights

### 1. Inbound Concentration vs. Destination Density (2026)
While classical metropolitan gateways (Chennai, Jaipur) lead in aggregate visitor volumes, **Ernakulam (20.08%)** and **Puri (14.99%)** exhibit the highest inbound foreign visitor density, requiring dedicated international amenities and multi-lingual service desks.

### 2. Tourism Segment Performance
- **Nature / Eco-Tourism** records the highest average foreign visitor footfall (**42,150 visitors/district**) and longest dwell time (**3.0 days**), exceeding classical heritage and hill-station circuits.
- **Beach Tourism** generates the largest average domestic volume (**1.30M visitors/district**).

### 3. Spending Velocity & Foreign Exchange Impact
- Visitors from **Oceania** ($257.70/day) and **North America** ($224.50/day) exhibit the highest daily spending velocity.
- **South Asian** (31.9%) and **American** (28.7%) tourists recorded the highest Net Promoter Sentiment, signaling strong organic repeat travel and referral dynamics.

### 4. Aviation Gateway Dependency
- **Delhi (DEL)** (95.7M annual passengers) and **Mumbai (BOM)** (80.3M) drive total volume.
- **Cochin (COK)** (**48.4%**) and **Thiruvananthapuram (TRV)** (**46.0%**) lead India in international traffic exposure, acting as critical international diaspora and inbound tourism hubs.

---

## 📈 Visual Analytics Gallery

All visualization artifacts are programmatically generated and exported to `results/plots/`:

| Chart | Metric Visualized | Key Finding |
|---|---|---|
| **01** | `01_monthly_airport_passenger_movements.png` | Post-COVID monthly passenger recovery trajectories across 40 airports. |
| **02** | `02_inbound_spend_vs_experience.png` | Scatter analysis comparing trip expenditure (USD) against visitor satisfaction (1–10). |
| **03** | `03_top_10_states_footfall_2026.png` | State-level annual footfall distribution identifying top regional tourism engines. |
| **04** | `04_district_infrastructure_correlation_matrix.png` | Pearson correlation matrix evaluating hotel room capacity vs tourist complaints. |
| **05** | `05_room_tariff_distribution_by_accommodation.png` | Boxplot spread of entry room tariffs across Heritage, Star, Resort, and Homestay units. |

---

## 🚀 Getting Started & Reproduction

### Prerequisites
- Python 3.10 or higher
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/HoraceHoney/india-tourism-analysis.git
cd india-tourism-analysis
```

### 2. Set Up Virtual Environment & Dependencies
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 3. Launch the Interactive Notebooks
```bash
jupyter notebook python/
```
You can execute the notebooks in sequential order:
- `01_data_ingestion_and_inspection.ipynb`
- `02_datatype_optimization.ipynb`
- `03_missing_value_imputation.ipynb`
- `04_feature_engineering.ipynb`
- `05_relational_merge.ipynb`
- `06_exploratory_and_econometric_analysis.ipynb`
- `07_visualizations_and_dashboards.ipynb`

Or run the complete pipeline in a single step with `python/00_master_pipeline.ipynb`.

---

## 🏛️ Data Sources & Alignment

- **Ministry of Tourism (MoT), Government of India**: India Tourism Statistics (ITS), Annual Reports, and PIB Bulletins.
- **National Integrated Database of Hospitality Industry (NIDHI)**: HRACC Star Classification & Classified Unit Registry.
- **Archaeological Survey of India (ASI)**: Centrally Protected Heritage Monuments & Footfall Records.
- **Bureau of Immigration (BOI)**: Inbound Foreign Tourist Arrivals (FTA) by Port of Entry & Nationality.
- **Airports Authority of India (AAI) & DGCA**: Monthly Civil Aviation Airport Traffic Reports.

---

## 📜 License & Citation

This project is released under the [MIT License](LICENSE).  
For academic or professional citations:
```bibtex
@misc{india_tourism_analytics_2026,
  author = {Horace Honey},
  title = {India Tourism Analytics & Econometric Pipeline (2022–2026)},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/HoraceHoney/india-tourism-analysis}}
}
```
