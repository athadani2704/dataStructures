/* Write your T-SQL query statement below */
with cte as(
    select dep.Name as Department, emp.Name as Employee, emp.Salary as Salary,
    dense_rank() over(partition by dep.Name order by emp.Salary desc) as ranks
    from
    Employee emp join Department dep on emp.DepartmentId=dep.Id
)select Department, Employee, Salary from cte where ranks=1