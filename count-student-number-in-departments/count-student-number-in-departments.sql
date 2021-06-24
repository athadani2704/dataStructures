/* Write your T-SQL query statement below */

select dep.dept_name, count(stu.student_id) as student_number from department dep left join student stu 
on dep.dept_id=stu.dept_id 
group by dep.dept_name 
order by 2 desc, 1