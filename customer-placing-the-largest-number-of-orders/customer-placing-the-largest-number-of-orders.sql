/* Write your T-SQL query statement below */
with groupBy as(
    select customer_number, count(*) as count_order from orders group by customer_number
)
select customer_number from groupBy where count_order = (select max(count_order) from groupBy)