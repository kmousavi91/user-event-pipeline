{{ config(materialized='view') }}

SELECT
  event_id,
  user_id,
  event_type,
  page,
  TIMESTAMP(timestamp) AS event_timestamp,
  device_type
FROM {{ source('bq_user_events', 'raw_events') }}
