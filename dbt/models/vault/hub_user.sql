{{ config(materialized='table') }}

SELECT DISTINCT
  user_id,
  {{ dbt_utils.generate_surrogate_key(['event_id']) }} AS hub_user_id,
  CURRENT_TIMESTAMP() AS load_ts
FROM {{ source('bq_user_events', 'raw_events') }}
WHERE user_id IS NOT NULL

