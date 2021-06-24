/* Write your T-SQL query statement below */

select * from (
    select distinct id, 'Root' as Type from tree where p_id is null
    union
    select a.id, 'Leaf' as Type from tree a left join tree b 
    on a.id=b.p_id where b.id is null and a.p_id is not null
    union
    select a.id, 'Inner' as Type from tree a join tree b 
    on a.id=b.p_id where b.id is not null and a.p_id is not null
)tab order by id