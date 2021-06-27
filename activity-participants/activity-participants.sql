/* Write your T-SQL query statement below */

with groups as (
    select activity, count(*) as counts from Friends group by activity
), ranks as (
    select activity, rank() over(order by counts) as ranking from groups
)
    select activity from ranks where ranking>1 and ranking<(select max(ranking) from ranks)