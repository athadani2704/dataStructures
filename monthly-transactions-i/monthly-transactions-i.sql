/* Write your T-SQL query statement below */

select substring(cast(a.trans_date as varchar), 1, 7) as month, a.country, count(a.amount) as trans_count, 
count(iif(state='approved', 1, NULL)) as approved_count, sum(a.amount) as trans_total_amount, 
sum(iif(state='approved', a.amount, 0)) as approved_total_amount
from Transactions a group by substring(cast(a.trans_date as varchar), 1, 7), a.country