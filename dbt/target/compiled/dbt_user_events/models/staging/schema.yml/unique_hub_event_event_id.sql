
    
    

with dbt_test__target as (

  select event_id as unique_field
  from `user-event-pipeline`.`bq_user_events`.`hub_event`
  where event_id is not null

)

select
    unique_field,
    count(*) as n_records

from dbt_test__target
group by unique_field
having count(*) > 1


