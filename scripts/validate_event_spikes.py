from google.cloud import bigquery
import pandas as pd

# Config
project_id = "user-event-pipeline"
dataset = "bq_user_events"
table = "daily_events"

client = bigquery.Client(project=project_id)

def fetch_event_data():
    query = f"""
        SELECT event_date, user_id, event_count
        FROM `{project_id}.{dataset}.{table}`
        WHERE event_date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) AND CURRENT_DATE()
        ORDER BY event_date
    """
    return client.query(query).to_dataframe()

def detect_spikes(df):
    spikes = []

    for user_id in df["user_id"].unique():
        user_df = df[df["user_id"] == user_id].copy()
        user_df["moving_avg"] = user_df["event_count"].rolling(window=7, min_periods=1).mean()
        user_df["is_spike"] = user_df["event_count"] > 3 * user_df["moving_avg"]

        spikes.extend(user_df[user_df["is_spike"]].to_dict("records"))

    return spikes

if __name__ == "__main__":
    df = fetch_event_data()
    if df.empty:
        print("No data found in daily_events.")
    else:
        spikes = detect_spikes(df)
        if spikes:
            print("🔺 Potential spikes detected:")
            for row in spikes:
                print(f"{row['event_date']} | user: {row['user_id']} | count: {row['event_count']} | 7d avg: {row['moving_avg']:.2f}")
        else:
            print("✅ No anomalies detected.")

