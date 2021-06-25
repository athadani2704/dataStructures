/* Write your T-SQL query statement below */


with cte1 as (
    select distinct o.customer_id, (select c.customer_name from Customers c where c.customer_id=o.customer_id) as customer_name, o.product_name from Orders o
), cte2 as (
    select distinct customer_id, product_name from Orders
)
    select distinct cte1.customer_id, cte1.customer_name from cte1 where not exists (select distinct a.product_name from Orders a where a.customer_id=cte1.customer_id and a.product_name='C') and (select count(distinct a.product_name) from Orders a where a.customer_id=cte1.customer_id and (a.product_name<>'C' and (a.product_name in ('A','B'))))=2 order by cte1.customer_id