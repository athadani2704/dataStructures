/* Write your T-SQL query statement below */


select p.project_id, p.employee_id from Project p join Employee e on 
p.employee_id=e.employee_id where e.experience_years=(select max(e1.experience_years) from Employee e1 join Project p1 on e1.employee_id=p1.employee_id where p1.project_id=p.project_id group by p1.project_id)