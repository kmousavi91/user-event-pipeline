{{ config(materialized='table') }}

SELECT
  {{ dbt_utils.generate_surrogate_key(['event_id']) }} AS hub_event_id,
  event_type,
  page,
  device_type,
  TIMESTAMP(timestamp) AS event_timestamp,
  CURRENT_TIMESTAMP() AS load_ts
FROM {{ source('bq_user_events', 'raw_events') }}

