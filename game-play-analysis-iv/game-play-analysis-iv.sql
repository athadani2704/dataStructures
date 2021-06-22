/* Write your T-SQL query statement below */

with cte1 as
(
    select player_id, min(event_date) over(partition by player_id order by event_date) as minval, event_date from activity
)
, cte2 as
(
    select count(*) as c from cte1 where event_date=dateadd(day, 1, minval
)
)
select round(cast(c as float)/(select count(distinct player_id) from activity),2) as fraction from cte2