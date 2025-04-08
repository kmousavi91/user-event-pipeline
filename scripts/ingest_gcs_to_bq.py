from google.cloud import storage, bigquery
import json

# CONFIG
bucket_name = "user-event-pipeline-raw-data-mousavi"
blob_name = "event_log_2025-04-01.json"
dataset_id = "bq_user_events"
table_id = "raw_events"
project_id = "user-event-pipeline"

def load_json_from_gcs_to_bigquery():
    # Init clients
    storage_client = storage.Client(project=project_id)
    bq_client = bigquery.Client(project=project_id)

    # Get the GCS file
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    content = blob.download_as_text()
    events = json.loads(content)

    # Ensure it's a list
    if isinstance(events, dict):
        events = [events]

    # Load into BigQuery
    table_ref = bq_client.dataset(dataset_id).table(table_id)
    errors = bq_client.insert_rows_json(table_ref, events)

    if errors:
        print("❌ Errors occurred while inserting rows:")
        print(errors)
    else:
        print(f"✅ Successfully loaded {len(events)} events into BigQuery table {dataset_id}.{table_id}")

if __name__ == "__main__":
    load_json_from_gcs_to_bigquery()

