# 🥗 Week 2 — Data Quality Check with a FAIR Dataset

**Course:** Data Management | SRH University Heidelberg  
**Tool:** Tableau Prep Builder  
**Dataset:** Nutrition, Physical Activity and Obesity – BRFSS (CDC)

---

## 📁 Files in this Folder

| File | Description |
|------|-------------|
| `raw.csv` | Raw dataset — 106,260 rows × 29 columns |
| `clean.csv` | Cleaned dataset — 106,260 rows × 25 columns |
| `nutrition_obesity_cleaned.hyper` | Tableau Hyper extract for Tableau Desktop |
| `nutrition_cleaning_flow.tfl` | Tableau Prep flow — all 5 cleaning steps |
| `Data_Quality_Report.pdf` | Full data quality & FAIR compliance report |
| `README.md` | This file |

---

## 🎯 Exercise Overview

**Goal:** Choose one publicly available FAIR dataset and use Tableau Prep to explore and improve its data quality across key dimensions: completeness, consistency, accuracy, validity, relevance, and interoperability.

**Dataset selected:**
- **Title:** Nutrition, Physical Activity, and Obesity – Behavioral Risk Factor Surveillance System (BRFSS)
- **Source:** Centers for Disease Control and Prevention (CDC) — data.cdc.gov
- **Time period:** 2011–2023 (13 years)
- **Size:** 106,260 rows × 29 columns
- **Format:** CSV | License: Public domain

The dataset tracks obesity, overweight, physical activity, and fruit/vegetable consumption among U.S. adults across all 50 states, broken down by age, sex, income, education, and race/ethnicity.

---

## 🔍 Data Quality Issues Found

| # | Issue | Category | Rows Affected |
|---|-------|----------|---------------|
| 1 | "Unknown" masking missing values in 5 demographic columns | Missing values | 75,900–98,670 per column |
| 2 | GeoLocation stored as unparseable string + 1,932 "Unknown" values | Inconsistent format | 106,260 |
| 3 | Trailing whitespace in column name `High_Confidence_Limit ` | Inconsistent format | All 106,260 |
| 4 | `Sample_Size` stored as float64 instead of integer | Incorrect data type | All 106,260 |
| 5 | 5 redundant/constant columns with no analytical value | Irrelevant fields | All 106,260 |
| 6 | Education value truncated at 30 characters | Invalid value | Affected rows |

---

## 🧹 Cleaning Workflow (5 Steps)

| Step | Action |
|------|--------|
| **Step 1** | Connect raw CSV as input |
| **Step 2** | Fix column name (strip trailing space), change `Sample_Size` to integer, complete truncated Education value |
| **Step 3** | Replace "Unknown" and "Data not reported" with null across 5 demographic columns |
| **Step 4** | Split `GeoLocation` into `Latitude` and `Longitude`, remove original GeoLocation, remove 5 redundant columns |
| **Step 5** | Export cleaned dataset as CSV |

---

## ✅ Improvements Achieved

| Metric | Before | After |
|--------|--------|-------|
| Number of columns | 29 | 25 |
| Detectable null values | 0 (hidden as "Unknown") | Correctly represented as null |
| GeoLocation | Unparseable string | Two numeric fields (Latitude, Longitude) |
| Column name errors | 1 (trailing space) | 0 |
| Sample_Size data type | float64 | Int64 (integer) |
| Truncated category values | 1 (Education) | 0 |

---

## ⚠️ Remaining Limitations

- No persistent identifier (DOI/PID) embedded in the file — FAIR findability gap
- No machine-readable license field in the data
- "Unknown" vs "not applicable" distinction lost — a production pipeline should separate the two
- Statistical outliers not removed — may represent valid extreme values
- No accompanying data dictionary/codebook

---

## 📐 FAIR Compliance

| Principle | Score | Notes |
|-----------|-------|-------|
| Findable | 60% | Named source (BRFSS), no global PID |
| Accessible | 80% | Open CSV, public portal |
| Interoperable | 75% | Column name fixed; GeoLocation split; Education completed |
| Reusable | 70% | Unknown → NaN; redundant columns removed |

---

## 🛠️ Tools Used

- **Tableau Prep Builder** — profiling, cleaning, transformation, export
- **Tableau Desktop** — downstream analysis target
