/* Write your T-SQL query statement below */


with cte as (
    select *, row_number() over(partition by Company order by Salary) as r from Employee
)
    select distinct Id, Company, Salary from cte where (r=1+(select count(*) from Employee e where e.Company=cte.Company)/2) or (r=(select count(*) from Employee e where e.Company=cte.Company)/2 and (select count(*) from Employee e where e.Company=cte.Company)%2=0)