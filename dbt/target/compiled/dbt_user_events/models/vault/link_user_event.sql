

SELECT DISTINCT
  to_hex(md5(cast(coalesce(cast(user_id as string), '_dbt_utils_surrogate_key_null_') as string))) AS hub_user_id,
  to_hex(md5(cast(coalesce(cast(event_id as string), '_dbt_utils_surrogate_key_null_') as string))) AS hub_event_id,
  CURRENT_TIMESTAMP() AS load_ts
FROM `user-event-pipeline`.`bq_user_events`.`raw_events`
WHERE user_id IS NOT NULL AND event_id IS NOT NULL