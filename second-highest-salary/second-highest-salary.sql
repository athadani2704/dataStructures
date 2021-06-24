/* Write your T-SQL query statement below */
-- with a as (
-- select distinct top 2 salary as SecondHighestSalary from employee order by salary desc)
-- select top 1 case when (select count(*) from a)>1 then SecondHighestSalary else NULL END as SecondHighestSalary from a order by SecondHighestSalary;
--     -- )select case when (exists(select SecondHighestSalary from b)) then SecondHighestSalary else NULL end as from b SecondHighestSalary;

with tab as (
    select Salary, dense_rank() over(order by Salary desc) as d from Employee
)
select max(Salary) as SecondHighestSalary from tab where d=2


-- 100    1       
-- 200    2
-- 200    2
-- 300    3

