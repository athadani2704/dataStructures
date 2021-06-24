/* Write your T-SQL query statement below */
select distinct c.Num as ConsecutiveNums from Logs a join Logs b
on a.Num=b.Num 
join Logs c
on b.Num=c.Num where a.Id=b.Id-1 and b.Id=c.Id-1