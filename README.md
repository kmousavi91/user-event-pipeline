## 📊 User Event Analytics Pipeline – GCP + DBT + Python

End-to-end data engineering pipeline using **Google Cloud Platform**, **DBT**, and **Python** to process, transform, and validate user interaction logs from a web/mobile application.

---

### 🚀 Project Overview

This project simulates a modern data stack used in real-world analytics engineering:

- **Ingestion Layer**: Raw JSON event logs stored in **Google Cloud Storage (GCS)**
- **Processing Layer**: Data loaded into **BigQuery** using Python
- **Transformation Layer**: Data modeled with **DBT** (staging, marts, and Data Vault)
- **Validation Layer**: Python script detects anomalies using rolling averages

---

### 🧱 Architecture

```
GCS (raw logs)
   ↓
Python ingestion (google-cloud-storage + bigquery)
   ↓
BigQuery (raw_events table)
   ↓
DBT transformations
   ├── staging (stg_raw_events)
   ├── marts (daily_events)
   └── vault (hub_user, hub_event, link_user_event, sat_event_metadata)
   ↓
Python validation script (detect spikes in activity)
```

---

### 📁 Project Structure

```bash
user-event-pipeline/
├── data/                      # Sample JSON files or schema
├── scripts/
│   ├── ingest_gcs_to_bq.py    # Loads raw JSON into BigQuery
│   └── validate_event_spikes.py  # Anomaly detection
├── dbt_user_events/           # DBT project (models, tests, config)
│   ├── models/
│   │   ├── staging/
│   │   ├── marts/
│   │   └── vault/
├── event_schema.json          # Schema for BigQuery raw table
├── requirements.txt
└── README.md
```

---

### 🛠️ Tools Used

- **Google Cloud Storage** – raw data landing zone  
- **BigQuery** – scalable data warehouse  
- **Python** – ingestion & validation scripts  
- **DBT** – transformations, testing, and modeling  
- **Data Vault 2.0** – enterprise data modeling architecture  

---

### 📊 Data Model Summary

- `raw_events` — base table in BigQuery  
- `stg_raw_events` — staging view that cleans raw data  
- `daily_events` — final table with user/day/device aggregations  
- `hub_user`, `hub_event`, `link_user_event`, `sat_event_metadata` — Data Vault models  
- Schema tests ensure data quality and traceability

---

### ✅ How to Run the Project

1. Clone the repo
2. Set up a GCP project and BigQuery dataset
3. Upload sample JSON files to GCS
4. Run:
   ```bash
   python scripts/ingest_gcs_to_bq.py
   dbt run
   dbt test
   python scripts/validate_event_spikes.py
   ```

---

### 📈 Anomaly Detection

A Python script fetches `daily_events` and detects **spikes in user activity** using a 7-day rolling average, printing warnings if anomalies are found.

---

### 📚 Learning Outcomes

- Build scalable, cloud-native data pipelines
- Apply software engineering principles with DBT
- Work with structured and semi-structured data in BigQuery
- Design flexible, auditable models with Data Vault
- Perform basic anomaly detection with Python

---

### 🧑‍💻 Author

**Kourosh Mousavi**  
Data Engineer | Physics → AI/Cloud/Data  
Warsaw, Poland  
https://www.linkedin.com/in/kourosh-mohammad-mousavi-895763113/

