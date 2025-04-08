

SELECT
  to_hex(md5(cast(coalesce(cast(event_id as string), '_dbt_utils_surrogate_key_null_') as string))) AS hub_event_id,
  event_type,
  page,
  device_type,
  TIMESTAMP(timestamp) AS event_timestamp,
  CURRENT_TIMESTAMP() AS load_ts
FROM `user-event-pipeline`.`bq_user_events`.`raw_events`