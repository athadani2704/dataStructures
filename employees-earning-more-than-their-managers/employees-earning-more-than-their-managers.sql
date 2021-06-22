/* Write your T-SQL query statement below */
select emp.name as Employee from Employee emp join Employee manager on
emp.managerid=manager.id where emp.salary>manager.salary;