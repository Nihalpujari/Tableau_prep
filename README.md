
**University:** SRH University Heidelberg  
**Course:** Data Management 
**Tool:** Tableau Prep Builder · Python (TabPy) · Gephi

This repository contains all weekly exercises and projects completed as part of the Data Management course. Each folder represents a separate exercise with its own dataset, flow, output, and report.

---

## 📁 Repository Structure

```
tableau_prep/
│
├── Data-Quality/                        # Week 2 — Data Quality Check (FAIR Dataset)
│   ├── raw.csv                          # Raw dataset (106,260 rows × 29 columns)
│   ├── clean.csv                        # Cleaned dataset (106,260 rows × 25 columns)
│   ├── nutrition_obesity_cleaned.hyper  # Tableau Hyper extract
│   ├── nutrition_cleaning_flow.tfl      # Tableau Prep flow (5 steps)
│   ├── Data_Quality_Report.pdf          # Full data quality & FAIR compliance report
│   └── README.md                        # Exercise documentation
│
├── Data-Profiling/                      # Week 3 — Data Profiling & Cleaning
│   ├── raw.csv                          # Raw dataset (100 rows × 18 columns)
│   ├── Output.xlsx                      # Cleaned dataset
│   ├── Output.hyper                     # Tableau Hyper extract
│   ├── flow.tfl                         # Tableau Prep flow
│   ├── Report.pdf                       # Full profiling & cleaning report
│   └── README.md                        # Exercise documentation
│
├── TabPy-Scripts/                       # Week 3 — Tableau Prep + Python (TabPy)
│   ├── employee_tableau_prep_python_sample.csv   # Raw employee dataset
│   ├── flow.tfl                         # Tableau Prep flow with Script step
│   ├── script.py                        # Python script run via TabPy
│   ├── output.csv                       # Filtered IT department output
│   └── README.md                        # Exercise documentation
│
└── Graph-Analysis/                      # Week 4 — Amazon Network Graph (Gephi)
    ├── amazon_sampled_graph.csv         # Edge list (2,178 edges, Source → Target)
    ├── Report.pdf                       # Graph analysis report
    └── README.md                        # Exercise documentation
```

---

## 🗂️ Exercises

| Week | Folder | Topic | Dataset | Status |
|------|--------|-------|---------|--------|
| Week 2 | [Data-Quality](https://github.com/Nihalpujari/Tableau_prep/tree/main/Data%20Quality%20Check%20with%20a%20FAIR%20Dataset) | Data Quality Check with a FAIR Dataset | CDC Nutrition & Obesity — 106,260 rows | ✅ Complete |
| Week 3 | [Data-Profiling](./Data-Profiling) | Data Profiling & Cleaning | Sales transactions — 100 rows | ✅ Complete |
| Week 3 | [TabPy-Scripts](./TabPy-Scripts) | Tableau Prep + Python (TabPy) | Employee dataset | ✅ Complete |
| Week 4 | [Graph-Analysis](./Graph-Analysis) | Amazon Network Graph Analysis (Gephi) | Amazon co-purchasing — 2,178 edges | ✅ Complete |

---

## 🛠️ Tools Used

- **Tableau Prep Builder** — data profiling, cleaning, and transformation
- **Python / TabPy** — scripting inside Tableau Prep workflows
- **Gephi** — graph visualisation and network analysis
- **Tableau Desktop** — data visualisation and analysis

---

## 👤 Author

**Nihal Pujari**  
SRH University Heidelberg  
Data Management Course
