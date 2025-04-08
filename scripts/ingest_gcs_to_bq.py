from google.cloud import storage, bigquery
import json
import pandas as pd

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

    # Download the file from GCS
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        content = blob.download_as_text()
    except Exception as e:
        print(f"❌ Failed to download file from GCS: {e}")
        return

    try:
        events = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}")
        return

    if isinstance(events, dict):
        events = [events]

    clean_events = []
    for i, event in enumerate(events):
        try:
            # Required fields check
            if not isinstance(event.get("event_id"), str) or not event.get("event_id").strip():
                print(f"❌ Skipping row {i}: missing or bad event_id")
                continue
            if not isinstance(event.get("user_id"), str) or not event.get("user_id").strip():
                print(f"❌ Skipping row {i}: missing or bad user_id")
                continue

            # Timestamp validation and formatting
            try:
                parsed_ts = pd.to_datetime(event["timestamp"])
                event["timestamp"] = parsed_ts.strftime("%Y-%m-%dT%H:%M:%SZ")
            except Exception:
                print(f"❌ Skipping row {i}: invalid timestamp format")
                continue

            # Optionally check for known fields
            expected_keys = {"event_id", "user_id", "event_type", "page", "timestamp", "device_type"}
            if not expected_keys.issubset(event.keys()):
                print(f"⚠️ Row {i} has unexpected/missing keys: {set(event.keys())}")
                # Continue if you're okay with partial keys, otherwise skip

            clean_events.append(event)

        except Exception as e:
            print(f"❌ Skipping row {i}: unexpected error - {e}")
            continue

    print(f"✅ Cleaned {len(clean_events)} valid records out of {len(events)}")

    # Load to BigQuery
    try:
        table_ref = bq_client.dataset(dataset_id).table(table_id)
        errors = bq_client.insert_rows_json(table_ref, clean_events)
        if errors:
            print("❌ Errors occurred while inserting rows:")
            print(errors)
        else:
            print(f"✅ Successfully loaded {len(clean_events)} events into {dataset_id}.{table_id}")
    except Exception as e:
        print(f"❌ BigQuery insert error: {e}")

if __name__ == "__main__":
    load_json_from_gcs_to_bigquery()

