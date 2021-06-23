/* Write your T-SQL query statement below */
with coursetab as(
    select distinct student, class from courses
)
select class from coursetab group by class having count(*)>=5