{{ config(materialized='table') }}

SELECT
  DATE(event_timestamp) AS event_date,
  user_id,
  device_type,
  COUNT(*) AS event_count
FROM {{ ref('stg_raw_events') }}
GROUP BY 1, 2, 3
