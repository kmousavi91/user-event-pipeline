select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select event_id
from `user-event-pipeline`.`bq_user_events`.`stg_raw_events`
where event_id is null



      
    ) dbt_internal_test