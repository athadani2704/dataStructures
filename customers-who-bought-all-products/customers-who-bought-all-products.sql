/* Write your T-SQL query statement below */

-- select customer_id from Customer c where exists(select product_key from Product where Product.product_key=c.product_key)


select distinct c.customer_id from Customer c join (select customer_id, count(distinct product_key) as counts from Customer group by customer_id) t 
on c.customer_id=t.customer_id and t.counts=(select count(*) from Product)