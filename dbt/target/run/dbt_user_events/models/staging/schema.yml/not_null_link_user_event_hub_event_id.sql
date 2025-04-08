select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select hub_event_id
from `user-event-pipeline`.`bq_user_events`.`link_user_event`
where hub_event_id is null



      
    ) dbt_internal_test