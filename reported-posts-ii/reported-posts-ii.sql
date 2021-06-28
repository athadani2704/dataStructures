/* Write your T-SQL query statement below */

with reported as (
    select a.action_date, count(distinct r.post_id)*1.0/count(distinct a.post_id)*100 as average_daily_percent 
    from Actions a left join Removals r on a.post_id=r.post_id 
    where a.action='report' and a.extra='spam'
    group by a.action_date
)
    select round(avg(average_daily_percent), 2) as average_daily_percent from reported