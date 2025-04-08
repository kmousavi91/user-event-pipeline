

SELECT DISTINCT
  event_id,
  to_hex(md5(cast(coalesce(cast(event_id as string), '_dbt_utils_surrogate_key_null_') as string))) AS hub_event_id,
  CURRENT_TIMESTAMP() AS load_ts
FROM `user-event-pipeline`.`bq_user_events`.`raw_events`
WHERE event_id IS NOT NULL