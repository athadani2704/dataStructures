/* Write your T-SQL query statement below */


with cred_deb as (
    select user_id, sum(amount) as amount from (
        select paid_by as user_id, -1*sum(amount) as amount from Transactions group by paid_by 
        union all
        select paid_to as user_id, sum(amount) as amount from Transactions group by paid_to
    ) t group by user_id
)
    select u.user_id, u.user_name, u.credit+isnull(c.amount, 0) as credit, 
    iif(u.credit+isnull(c.amount, 0)<0, 'Yes', 'No') as credit_limit_breached from 
    Users u left join cred_deb c on u.user_id=c.user_id