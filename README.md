# 🧠 User Event Pipeline — GCP + BigQuery + DBT

This project demonstrates a complete **event data pipeline** from Google Cloud Storage to BigQuery, using **Python**, **DBT**, and **data quality testing**.

It simulates ingestion and transformation of user event logs (clicks, scrolls, purchases), handling **bad data**, applying **Data Vault modeling**, and testing via **DBT tests**.

---

## 📦 Tech Stack

- **Google Cloud Storage (GCS)** – Raw data storage
- **BigQuery** – Data warehouse for ingestion and analytics
- **Python** – Custom ingestion script with cleaning & validation
- **DBT** – SQL-based transformation and testing
- **Data Vault Modeling** – Scalable, auditable data structure

---

## 📌 Use Case

> Track user behavior events and prepare them for clean analytics.

We ingest a JSON log file that includes valid and invalid user events. Invalid fields (e.g. `null user_id`, bad timestamps) are handled or filtered out during ingestion and transformation.

---

## 📂 Project Structure

```
user_event_pipeline/
│
├── data/                      # JSON event logs (raw input)
│   └── event_log_*.json
│
├── scripts/                   # Ingestion script
│   └── ingest_gcs_to_bq.py
│
├── dbt         # DBT project
│   ├── models/
│   │   ├── staging/           # stg_raw_events.sql — cleans raw data
│   │   ├── marts/             # daily_events.sql — aggregates by user/date
│   │   └── vault/             # Data Vault models: hub_user, hub_event, etc.    
│   └── dbt_project.yml
```

---

## ✅ Pipeline Workflow

### 1. Ingest Raw Events
```bash
python scripts/ingest_gcs_to_bq.py
```
- Reads a JSON file from GCS
- Cleans and validates rows (e.g. bad timestamp, missing user_id)
- Loads cleaned events into BigQuery: `bq_user_events.raw_events`

### 2. Transform with DBT
```bash
cd dbt_user_events/
dbt run
```
- Cleans raw data in `stg_raw_events`
- Aggregates clean data in `daily_events`
- Applies Data Vault logic in `hub_user`, `hub_event`, `link_user_event`

### 3. Validate with DBT Tests
```bash
dbt test
```
- Validates schema (not_null, unique, etc.)
- Detects duplicates or nulls in hubs and staging layers

---

## 🚨 Error Handling Example

When ingesting messy data, errors like below are caught:

```
Skipping row 1: missing or bad user_id
Skipping row 3: invalid timestamp format
✅ Cleaned 19 valid records out of 20
```

---

## 📊 Example Use Cases

- Spike detection in event volume
- Anomaly filtering at ingestion time
- Scalable warehouse modeling with Data Vault

---

## 🧪 Features Demonstrated

- [x] GCS file ingestion using Python
- [x] Schema-based filtering and cleanup
- [x] BigQuery table creation from schema
- [x] Data Vault modeling with DBT
- [x] DBT testing (`not_null`, `unique`, `accepted_values`)
- [x] Clean separation of raw, staging, marts, and vault layers

---


## ✍️ Author

**Kourosh Mousavi**  
https://www.linkedin.com/in/kourosh-mohammad-mousavi-895763113/
Tools: Python | GCP | BigQuery | DBT | Data Vault | Airflow


