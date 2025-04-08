

SELECT
  DATE(event_timestamp) AS event_date,
  user_id,
  device_type,
  COUNT(*) AS event_count
FROM `user-event-pipeline`.`bq_user_events`.`stg_raw_events`
GROUP BY 1, 2, 3