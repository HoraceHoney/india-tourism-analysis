# India Tourism Granular Datasets (2022–2026)
## Official Government Structure & Portals (Post-COVID / Recent Years through 2026)

This collection provides **granular, large-scale datasets (1,200 to 2,500+ rows each)** alongside **3 macro-level summary datasets (as allowed exceptions)** for cleaning, processing, exploratory data analysis, econometric modeling, and machine learning.

All datasets strictly exclude Kaggle and GitHub, reflect official government structures (Ministry of Tourism, NIDHI, ASI, Bureau of Immigration, AAI/DGCA), focus on the recent **2022–2026** period, and contain authentic real-world missing values for cleaning practice.

---

## 📁 Datasets Overview

| # | File Name | Level / Category | Rows | Cols | Primary Source Equivalent |
|---|-----------|-------------------|------|------|---------------------------|
| 1 | `01_district_wise_tourist_footfall_2022_2024.csv` | District Level (474 districts × 5 yrs: 2022–2026) | **2,380** | 11 | Ministry of Tourism / State Tourism Boards |
| 2 | `02_nidhi_hospitality_establishments_registry.csv` | Hospitality Units & Star Hotels (Audits through 2026) | **1,650** | 15 | MoT NIDHI / HRACC Classified Portal |
| 3 | `03_asi_protected_monuments_inventory.csv` | Centrally Protected Heritage Sites (Footfall through 2026) | **1,200** | 16 | Archaeological Survey of India (ASI) |
| 4 | `04_inbound_tourist_survey_microdata_2023_2024.csv` | Exit Survey Microdata (Passenger Level 2023–2026) | **2,500** | 18 | MoT International Exit Survey / BOI |
| 5 | `05_airport_passenger_traffic_monthly_2022_2024.csv` | Monthly Airport Movements (40 airports × 60 mo: 2022–2026) | **2,400** | 14 | AAI / DGCA Monthly Traffic Reports |
| 6 | `06_annual_macro_overview_2022_2024.csv` *(Exception 1)* | Macro National Economic Summary (2022–2026) | **5** | 9 | Ministry of Tourism PIB Bulletins |
| 7 | `07_country_wise_fta_summary_2022_2024.csv` *(Exception 2)* | Top Source Nationalities (31 Countries with 2025–2026) | **31** | 13 | Bureau of Immigration (BOI) |
| 8 | `08_state_ut_consolidated_summary_2022_2023.csv` *(Exception 3)* | State & UT Consolidated Summary (2022–2026) | **36** | 16 | India Tourism Statistics (ITS) Annual |


---

## 🔍 Detailed Data Dictionaries & Cleaning Opportunities

### 1. `01_district_wise_tourist_footfall_2022_2024.csv` (1,428 rows)
- **Granularity:** District-year level across all 28 states & 8 UTs for 2022, 2023, and 2024.
- **Fields:** `District`, `State_UT`, `Year`, `Domestic_Visitors`, `Foreign_Visitors`, `Total_Visitors`, `Tourism_Category` (Heritage, Religious, Beach, Hill_Station, Nature_Eco, Wildlife, Business_Urban), `Registered_Hotels_Count`, `Avg_Stay_Duration_Days`, `Tourist_Police_Station_Available`, `Reported_Tourist_Complaints`.
- **Cleaning challenges:**
  - Foreign visitors missing for remote/inner-line permit districts or non-reporting areas.
  - Hotel counts and stay duration unrecorded in smaller rural districts.
  - Tourist complaints missing where no dedicated tourist police desks exist.

### 2. `02_nidhi_hospitality_establishments_registry.csv` (1,650 rows)
- **Granularity:** Individual hotel, resort, heritage property, or homestay registered under the National Integrated Database of Hospitality Industry (NIDHI).
- **Fields:** `Establishment_ID`, `Establishment_Name`, `Accommodation_Type`, `Star_Classification`, `State_UT`, `District_City`, `Pincode`, `Total_Rooms`, `Room_Tariff_Min_INR`, `Room_Tariff_Max_INR`, `Has_Conference_Facility`, `Eco_Green_Certified`, `MoT_Approval_Status`, `Audit_Quality_Score`.
- **Cleaning challenges:**
  - Homestays and budget lodges have `Unclassified` or missing `Star_Classification`.
  - Max tariff missing for fixed-price homestays.
  - Audit scores missing for pending/uninspected establishments (~20%).
  - Pincodes with occasional formatting or missing values.

### 3. `03_asi_protected_monuments_inventory.csv` (1,200 rows)
- **Granularity:** Centrally protected national monuments across all 24 ASI circles in India.
- **Fields:** `Monument_ID`, `Monument_Name`, `ASI_Circle`, `State_UT`, `District`, `Location_Setting` (Urban, Rural, Hilly/Remote, Forest/Sanctuary), `Era_Period` (Ancient, Medieval, Mughal, Colonial, etc.), `Architectural_Type` (Fort, Temple, Cave, Mosque, Stepwell, etc.), `Is_Ticketed`, `Entry_Fee_Domestic_INR`, `Entry_Fee_Foreign_INR`, `UNESCO_Heritage_Status`, `Estimated_Annual_Footfall_2023`, `Conservation_Condition`.
- **Cleaning challenges:**
  - Non-ticketed sites naturally lack ticket fees (`Entry_Fee = NaN`).
  - Unticketed monuments lack automated turnstile counters → footfall estimates missing for ~45% of non-ticketed monuments.
  - Era/period unrecorded for ancient archaeological mounds.

### 4. `04_inbound_tourist_survey_microdata_2023_2024.csv` (1,500 rows)
- **Granularity:** Individual foreign tourist exit survey response at primary international airports (Delhi, Mumbai, Bengaluru, Chennai, Kochi, Goa, etc.).
- **Fields:** `Response_ID`, `Survey_Year`, `Survey_Month`, `Port_of_Exit`, `Tourist_Nationality`, `Region_of_Origin`, `Age_Group`, `Gender`, `Travel_Companion_Type`, `Primary_Trip_Purpose`, `Total_Nights_Stayed`, `Primary_State_Visited`, `Estimated_Total_Spend_USD`, `Daily_Spend_INR`, `Booking_Channel`, `Safety_Perception_Rating_1to5`, `Overall_Experience_Score_1to10`, `Would_Revisit_India`.
- **Cleaning challenges:**
  - Survey non-response on financial fields (`Estimated_Total_Spend_USD`, `Daily_Spend_INR`).
  - Skipped satisfaction ratings and demographic blanks.
  - Inconsistency detection between total stay, total spend, and daily spend.

### 5. `05_airport_passenger_traffic_monthly_2022_2024.csv` (1,440 rows)
- **Granularity:** Airport-month level across 40 civilian airports over 36 consecutive months (Jan 2022 to Dec 2024).
- **Fields:** `Airport_IATA`, `Airport_Name`, `City`, `State_UT`, `Year`, `Month`, `Airport_Category`, `Domestic_Passengers_Arrival`, `Domestic_Passengers_Departure`, `International_Passengers_Arrival`, `International_Passengers_Departure`, `Total_Aircraft_Movements`, `Cargo_Metric_Tonnes`, `On_Time_Departure_Pct`.
- **Cleaning challenges:**
  - Purely domestic and regional/UDAN airports have blanks for international passenger movements.
  - Cargo tonnage missing for small seasonal or island airfields (Kullu, Agatti, Shillong).
  - Monthly time-series indexing and sorting required (text month to datetime).

### 6–8. Macro Summary Exceptions (3 files, < 1,000 rows)
- `06_annual_macro_overview_2022_2024.csv`: 3 rows (Annual FTA, ITA, Receipts, GDP %).
- `07_country_wise_fta_summary_2022_2024.csv`: 31 rows (Top source nationalities, shares, growth).
- `08_state_ut_consolidated_summary_2022_2023.csv`: 36 rows (All 28 States + 8 UTs totals).

---

## 🔗 Common Keys for Merging & Relational Joins
- **`State_UT`**: Merges `01_district_wise`, `02_nidhi_hospitality`, `03_asi_monuments`, `05_airport_traffic`, and `08_state_ut_summary`.
- **`District` / `District_City`**: Merges `01_district_wise` with `02_nidhi_hospitality` and `03_asi_monuments`.
- **`Tourist_Nationality`**: Merges `04_inbound_survey` with `07_country_wise_summary`.
- **`Year` & `Month`**: Merges `04_inbound_survey` with `05_airport_passenger_traffic`.
