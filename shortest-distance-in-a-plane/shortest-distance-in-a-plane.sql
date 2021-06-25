/* Write your T-SQL query statement below */


select min(round(sqrt((square(a.x-b.x))+(square(a.y-b.y))), 2)) as shortest from point_2d a, point_2d b
where a.x<>b.x or a.y<>b.y