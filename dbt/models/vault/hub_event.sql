{{ config(materialized='table') }}

SELECT DISTINCT
  event_id,
  {{ dbt_utils.generate_surrogate_key(['event_id']) }} AS hub_event_id,
  CURRENT_TIMESTAMP() AS load_ts
FROM {{ source('bq_user_events', 'raw_events') }}
WHERE event_id IS NOT NULL

