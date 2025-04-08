

  create or replace view `user-event-pipeline`.`bq_user_events`.`my_second_dbt_model`
  OPTIONS()
  as -- Use the `ref` function to select from other models

select *
from `user-event-pipeline`.`bq_user_events`.`my_first_dbt_model`
where id = 1;

