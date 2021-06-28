/* Write your T-SQL query statement below */


select e.*, 
case when e.operator='>' then 
    case when (select value from Variables v where v.name=e.left_operand)>(select value from Variables v where v.name=e.right_operand) then 'true' else 'false' end 
when e.operator='<' then
    case when (select value from Variables v where v.name=e.left_operand)<(select value from Variables v where v.name=e.right_operand) then 'true' else 'false' end
else
    case when (select value from Variables v where v.name=e.left_operand)=(select value from Variables v where v.name=e.right_operand) then 'true' else 'false' end
end as value from Expressions e