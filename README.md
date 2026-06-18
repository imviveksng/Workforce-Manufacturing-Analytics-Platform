# 🏭 Workforce & Manufacturing Analytics Platform

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

> An end-to-end ETL pipeline and BI dashboard platform that automates workforce and manufacturing analytics — from raw Excel data to interactive Power BI insights.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Technology Stack](#-technology-stack)
- [Architecture](#-architecture)
- [Repository Structure](#-repository-structure)
- [Datasets](#-datasets)
- [ETL Workflow](#-etl-workflow)
- [Dashboard Pages](#-dashboard-pages)
- [Key Insights](#-key-insights)
- [Getting Started](#-getting-started)
- [Future Enhancements](#-future-enhancements)

---

## 📖 Project Overview

This project simulates a real-world manufacturing organization and delivers a fully automated analytics platform covering:

- **Workforce attendance** tracking across departments and shifts
- **Overtime analysis** at employee and department level
- **Production performance** monitoring by machine
- **Quality control** tracking defect rates and rejections

The pipeline processes **627,914+ records** sourced from multiple Excel files, transforms them using Python, loads them into PostgreSQL, and visualizes them through interactive Power BI dashboards.

---

## 🎯 Business Problem

Organizations typically receive workforce and operational data from multiple departments in Excel format. This leads to:

- ❌ Data inconsistencies across sources
- ❌ Time-consuming manual report preparation
- ❌ No centralized view of workforce productivity
- ❌ Limited visibility into machine-level performance

This platform solves these problems by automating the entire reporting workflow — from ingestion to visualization.

---

## 🛠️ Technology Stack

| Layer          | Technology    | Purpose                        |
|----------------|---------------|--------------------------------|
| Source Data    | Excel (.xlsx) | Raw input files                |
| ETL Processing | Python 3.10+  | Extract, transform, load logic |
| Data Wrangling | Pandas, NumPy | Cleaning & transformation      |
| Data Storage   | PostgreSQL    | Centralized analytical storage |
| Analytics      | SQL           | Business queries & aggregations|
| Visualization  | Power BI      | Interactive dashboards         |
| Fake Data      | Faker         | Realistic data simulation      |

---

## 🏗️ Architecture

```
┌─────────────────────────────────┐
│         Excel Source Files      │
│  employees │ attendance │ OT    │
│  production │ quality          │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│       Python ETL Pipeline       │
│  extract.py → transform.py      │
│       → load.py → main.py       │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│        PostgreSQL Database      │
│  Employees │ Attendance │ OT    │
│  Production │ Quality          │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│        Power BI Dashboard       │
│  Executive Summary │ Workforce  │
│  Overtime │ Production/Quality  │
└────────────────┬────────────────┘
                 │
                 ▼
         Business Decisions
```

---

## 📁 Repository Structure

```
Workforce-Manufacturing-Analytics-Platform/
│
├── data/
│   ├── employees.xlsx
│   ├── attendance.xlsx
│   ├── overtime.xlsx
│   ├── production.xlsx
│   └── quality.xlsx
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── main.py
│   ├── generate_employees.py
│   ├── generate_attendance.py
│   ├── generate_overtime.py
│   ├── generate_production.py
│   └── generate_quality.py
│
├── sql/
│   ├── company_db.sql
│   └── analytics_queries.sql
│
├── dashboards/
│   ├── Workforce_Manufacturing_Analytics.pbix
│   └── dashboard_screenshots/
│
├── docs/
│   ├── architecture.png
│   └── data_model.png
│
├── requirements.txt
└── README.md
```

---

## 📊 Datasets

| Dataset    | Records   | Description                              |
|------------|----------:|------------------------------------------|
| Employees  |     1,000 | Employee master data across departments  |
| Attendance |   365,000 | Daily attendance records (1 year)        |
| Overtime   |    98,238 | Employee OT hours by date                |
| Production |    87,600 | Machine-level daily production output    |
| Quality    |    76,076 | Defect and rejection records             |
| **Total**  | **627,914+** | **Records processed through pipeline** |

---

## ⚙️ ETL Workflow

### 1. Extract
- Read all five source Excel files using `openpyxl` / `pandas`
- Load raw datasets into Pandas DataFrames for processing

### 2. Transform
- Remove duplicate records
- Validate business rules (e.g., valid department codes, shift values)
- Clean invalid and null records
- Standardize column names and data types
- Derive calculated fields (e.g., attendance %, defect rate)

### 3. Load
- Connect to PostgreSQL via `SQLAlchemy` and `psycopg2`
- Create using `company_db`
- Load all transformed tables into the database
- Confirm row counts and data integrity

---

## 📈 Dashboard Pages

![Dashboard](dashboards/dashboard_screenshots/1.png)
### 🔷 Executive Summary
- Total employee headcount
- Overall attendance percentage
- Total overtime hours logged
- Total production units
- Defect percentage

![Dashboard](dashboards/dashboard_screenshots/2.png)
### 🔷 Workforce Analytics
- Department-wise attendance breakdown
- Shift-level performance comparison
- Employee-level attendance ranking

![Dashboard](dashboards/dashboard_screenshots/3.png)
### 🔷 Overtime Analytics
- Top 10 employees by OT hours
- Department-wise OT distribution
- OT trends over time

![Dashboard](dashboards/dashboard_screenshots/4.png)
### 🔷 Production & Quality Analytics
- Production output by machine
- Defect percentage by date/department
- Production vs. rejection comparison

---

## 💡 Key Insights

- 📌 Workforce attendance maintained at approximately **90%** across all departments
- 📌 Defect rate held near **3%**, within acceptable manufacturing thresholds
- 📌 Identified **top overtime contributors** at employee and department level
- 📌 Monitored **machine-level production performance** to flag underperformers

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL 14+
- Power BI Desktop

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/Workforce-Manufacturing-Analytics-Platform.git
cd Workforce-Manufacturing-Analytics-Platform

# Install dependencies
pip install -r requirements.txt
```

### Configure Database

Update your PostgreSQL credentials in `scripts/load.py`:

```python
DB_URL = "postgresql://username:password@localhost:5432/workforce_db"
```

### Run the Pipeline

```bash
# Run the full ETL pipeline
python scripts/main.py
```

### Open Dashboard

Open `dashboards/Workforce_Manufacturing_Analytics.pbix` in Power BI Desktop and refresh the data source to point to your PostgreSQL instance.

---

## 🔮 Future Enhancements

- [ ] Incremental ETL loading (process only new/changed records)
- [ ] Apache Airflow for pipeline scheduling and orchestration
- [ ] Cloud deployment (AWS RDS / Azure PostgreSQL)
- [ ] Real-time API data integration
- [ ] Star schema data warehouse redesign

---

## 📬 Connect

Feel free to connect or reach out if you have questions about this project!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vivek-kumar-singh-2b41bb229)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/imviveksng)

---

*Built with ❤️ as a portfolio project for Data Analyst & BI Analyst roles.*
