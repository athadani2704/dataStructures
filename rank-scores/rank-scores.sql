/* Write your T-SQL query statement below */
select score, dense_rank() over (order by score desc) as Rank
from scores-- order by score desc;