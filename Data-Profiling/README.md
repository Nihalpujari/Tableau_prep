# 📊 Week 3 — Data Profiling & Cleaning Exercise

**Course:** Data Management | SRH Fernhochschule Riedlingen  
**Tool:** Tableau Prep Builder  
**Dataset:** `tableau_prep_cleaning_exercise.csv`

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `tableau_prep_cleaning_exercise.csv` | Raw dataset (100 rows, 18 columns) |
| `tableau_prep_cleaned.csv` | Cleaned dataset (95 rows, 22 columns) |
| `DataProfiling_Report_v2.docx` | Full profiling & cleaning report |

---

## 🎯 Exercise Overview

This exercise covers a full data profiling and cleaning pipeline using Tableau Prep Builder, from raw data import through to a validated, analysis-ready output.

**Steps covered:**
1. Dataset import into Tableau Prep
2. Profiling — missing values, data types, distributions, duplicates, cardinality
3. Column analysis — identifiers, validity, unique value counts
4. Structure analysis — record identification, calculated field consistency
5. Defining cleaning rules
6. Cleaning and transformation
7. Validation — before vs after comparison
8. Export for Tableau Desktop
9. Pipeline context — ETL vs ELT decision

---

## 🔍 Issues Found During Profiling

| Issue | Detail |
|-------|--------|
| Duplicate rows | 5 fully duplicate Order_IDs |
| Missing values | 76 nulls across 8 columns |
| Case inconsistencies | Customer_Segment, Payment_Method, Product_Category, Country, Customer_Name, City |
| Invalid value | Age = 130+ (biologically impossible) |
| Dirty numeric | Unit_Price contained € symbols and comma decimals (e.g. `9999,99`) |
| Mixed date formats | 5+ formats in Order_Date: `DD.MM.YYYY`, `DD/MM/YYYY`, `YYYY-MM-DD`, `YYYY/MM/DD`, `MM-DD-YYYY` |

---

## 🧹 Cleaning Steps Applied

- **Removed 5 duplicate rows** using PARTITION logic on Order_ID
- **Standardised text** — Group and Replace + Title Case on 6 columns
- **Excluded invalid Age** value (130–140 range)
- **Cleaned Unit_Price** — stripped € symbol, fixed comma decimals, converted to Float
- **Filled missing values** — Age → mean (48), Satisfaction_Score → mode (3), categoricals → "Unknown"
- **Standardised dates** — DATEPARSE with conditional logic for all 5 formats
- **Created 3 new fields** — Age_Group, Sales_Tier, Unit_Price_Scaled (min-max)

---

## ✅ Validation Summary

| Metric | Before | After |
|--------|--------|-------|
| Rows | 100 | 95 |
| Duplicate Order_IDs | 5 | 0 |
| Missing values | 76 | Minimal |
| Customer_Segment variants | 6 | 3 |
| Payment_Method variants | 7 | 5 |
| Product_Category variants | 10 | 5 |
| Country variants | 10 | 5 |
| Customer_Name variants | 18 | 12 |
| Invalid Age values | 1 | 0 |
| Total columns | 18 | 22 |

---

## ⚙️ ETL vs ELT

This exercise uses an **ETL approach** — data is profiled and cleaned in Tableau Prep before being loaded into Tableau Desktop. ETL is the right choice here because:

- Small dataset (100 rows)
- Well-defined, fixable issues
- Destination is Tableau Desktop, not a cloud warehouse

ELT would be preferred for large-scale pipelines using tools like Snowflake, BigQuery, or dbt.

---

## 🛠️ Tools Used

- **Tableau Prep Builder** — profiling, cleaning, transformation, export
- **Tableau Desktop** — downstream analysis target
