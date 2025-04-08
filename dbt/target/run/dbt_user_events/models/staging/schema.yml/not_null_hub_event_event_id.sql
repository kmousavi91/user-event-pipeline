select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select event_id
from `user-event-pipeline`.`bq_user_events`.`hub_event`
where event_id is null



      
    ) dbt_internal_test