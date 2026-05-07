# Week 3 – Tableau Prep Scripts with TabPy

This project is part of a weekly Tableau Prep assignment. It demonstrates how to use **TabPy** (Tableau Python Server) inside Tableau Prep to run Python scripts as transformation steps within a data flow.

---

## Assignment Overview

**Tool:** Tableau Prep Builder + TabPy  
**Dataset:** `employee_tableau_prep_python_sample.csv`  
**Goal:** Filter employees, compute global metrics, and enrich the output with new columns — all via a Python script step.

---

## Repository Structure

```
├── employee_tableau_prep_python_sample.csv   # Source dataset (15 employees)
├── script.py                                  # Python script used in Tableau Prep (TabPy)
├── Flow.tfl                                   # Tableau Prep flow file
├── Output.csv                                 # Final output after running the flow
└── README.md
```

---

## Dataset

The CSV contains 15 employee records with the following columns:

| Column | Description |
|---|---|
| `Employee_ID` | Unique identifier (e.g. E001) |
| `Employee_Name` | Full name |
| `Department` | IT, Finance, HR, Sales, Marketing, Operations |
| `Age` | Employee age |
| `Salary` | Annual salary |
| `Hire_Date` | Date of hire |
| `City` | City of work location |

---

## Python Script (`script.py`)

The script runs inside Tableau Prep via a **Script Step** connected to a local TabPy server.

### What it does

1. **Computes the average salary** of all 15 employees (before filtering)
2. **Finds the oldest employee** across the entire dataset
3. **Filters** the data to only IT department employees
4. **Adds three new columns** to the filtered output:
   - `Average_Salary_All_Employees`
   - `Oldest_Employee_Name`
   - `Oldest_Employee_Department`

### Key design decision

The global metrics (average salary, oldest employee) are calculated **before** the IT filter. This ensures the values reflect the full company — not just the IT department.

---

## Output

The final output (`Output.csv`) contains **5 rows** — one per IT employee — with the three new enrichment columns appended:

| Employee_ID | Employee_Name | Department | Age | Salary | Average_Salary_All_Employees | Oldest_Employee_Name | Oldest_Employee_Department |
|---|---|---|---|---|---|---|---|
| E001 | Anna Weber | IT | 29 | 52,000 | 57,100 | Helga Braun | HR |
| E003 | Sara Hoffmann | IT | 35 | 58,000 | 57,100 | Helga Braun | HR |
| E006 | Omar Yilmaz | IT | 52 | 72,000 | 57,100 | Helga Braun | HR |
| E009 | Maya Becker | IT | 44 | 69,000 | 57,100 | Helga Braun | HR |
| E012 | Tim Schneider | IT | 25 | 48,000 | 57,100 | Helga Braun | HR |

---

## How to Run

### Prerequisites

- [Tableau Prep Builder](https://www.tableau.com/products/prep) installed
- [TabPy](https://github.com/tableau/TabPy) installed and running

### Steps

1. **Start the TabPy server:**
   ```bash
   tabpy
   ```
   TabPy runs on `localhost:9004` by default.

2. **Open Tableau Prep** and load `Flow.tfl`

3. In the **Script step**, ensure the connection points to:
   - Server: `localhost`
   - Port: `9004`
   - File: `script.py`
   - Function: `process_employees`

4. **Run the flow** — the output will match `Output.csv`

---

## Tools & Technologies

- Tableau Prep Builder
- TabPy (Tableau Python Server)
- Python 3.x
- pandas
