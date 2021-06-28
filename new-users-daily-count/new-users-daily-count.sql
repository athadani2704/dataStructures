/* Write your T-SQL query statement below */


with ranks as (
    select user_id, min(activity_date) as login_date from Traffic 
    where activity='login' 
    group by user_id
)
    select login_date, count(user_id) as user_count from ranks 
    where datediff(day, login_date, cast('2019-06-30' as date))<=90 
    group by login_date