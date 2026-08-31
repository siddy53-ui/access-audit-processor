# 🛡️ Enterprise Access Auditor

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Live-success.svg)](#)

**Live Demo:** [Launch the Interactive Dashboard](https://audit-report-automator.streamlit.app/)

### Dashboard Preview

![Streamlit Dashboard](https://github.com/siddy53-ui/access-audit-processor/raw/main/dashboard.png)

## 📌 Project Overview

This framework automates a repetitive, error-prone manual audit process and can be adapted to automate reporting, data processing, and visualization workflows across any industry that relies on manual spreadsheet-based compliance checks.

## 💡 Business Impact & ROI

This automation was engineered to resolve a critical operational bottleneck. Previously, processing these complex security datasets required **90 minutes of daily manual effort** per team member and involved over **30 repetitive steps** in Excel, making the process highly susceptible to human error.

By replacing this manual workflow with a vectorized Python pipeline, the reporting process was reduced to seconds. This eliminates data manipulation errors, ensures consistent compliance output, and recovers significant engineering time annually.

The **Enterprise Access Auditor** is an automated data processing and visualization pipeline designed to replace manual, error-prone spreadsheet tasks in enterprise compliance. It ingests raw server access logs, applies business exclusion rules using vectorized operations, visualizes the data distribution, and generates a structured, multi-tab audit workbook.

This project demonstrates practical **data automation** and **interactive visualization**, showing how raw operational data can be rapidly transformed into actionable compliance intelligence.

## 🏗️ Architecture & Tech Stack

Built entirely in Python, using industry-standard data and front-end libraries:

- **Pandas** — Core data engine. Uses vectorized string parsing and boolean masking to process thousands of records efficiently without expensive `for` loops.
- **Streamlit** — Drives the interactive web UI, providing instant data visualization (bar charts and metric cards) and dynamic file handling.
- **OpenPyXL** — Handles programmatic generation of multi-sheet Excel reports, segregating data into Business As Usual (BAU), Exclusions, and Duplicates.
- **Faker** — Generates synthetic, anonymized enterprise datasets for safe local testing and demonstration (no real audit data is used or required).

## ✨ Key Features

1. **Vectorized data pipeline** — Parses complex strings (e.g. `DOMAIN\User`) and filters records based on target activities and specific security groups.
2. **Automated data triage** — Intelligently routes records into distinct categories:
   - **Valid records (BAU):** Clean data ready for compliance tracking.
   - **Exclusions:** Automatically flags service accounts (e.g. `svc-*`) and domain administrators.
   - **Duplicates:** Detects and separates redundant log entries.
3. **Interactive visualizations** — Renders metric summaries and bar charts natively in the browser, so analysts can verify data integrity before download.
4. **Synthetic data generator** — Standalone module that spins up realistic, randomized CSV test logs with intentional noise and edge cases.
5. **Zero-data-exfiltration (local execution)** — Designed for strict enterprise security requirements. The Streamlit app and Pandas processing engine run entirely locally; confidential audit logs never need to leave the internal network.

## 🚀 How to Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/siddy53-ui/access-audit-processor.git
cd access-audit-processor
```

**2. Create a virtual environment and install dependencies**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

**3. Generate synthetic test data**

```bash
python generate_test_data.py
```

This generates a synthetic audit log CSV (`synthetic_audit_logs.csv`) in the root directory.

**4. Launch the application**

```bash
streamlit run app.py
```

## 📂 Repository Structure

```
├── app.py                     # Streamlit UI, visual routing, and file handling
├── process_audit.py           # Core Pandas data transformation logic
├── generate_test_data.py      # Faker script to generate synthetic CSV logs
├── synthetic_audit_logs.csv   # Sample generated test data
├── dashboard.png              # Dashboard preview image
├── requirements.txt           # Deployment dependencies
└── README.md                  # Project documentation
```

## 👨‍💻 Author

**Sourav Dutta**
- **LinkedIn:** [Sourav Dutta](https://www.linkedin.com/in/sourav-dutta-15314b430)
- **Focus:** Data Automation | Python Engineering | Data Visualization


