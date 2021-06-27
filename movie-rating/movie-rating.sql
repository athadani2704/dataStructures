/* Write your T-SQL query statement below */


with user_data as (
    select u.name as results, m.counts from Users u join (select user_id, count(*) as counts from Movie_Rating group by user_id) m on u.user_id=m.user_id
), user_data1 as (
    select results, counts, rank() over(order by counts desc, results) as r from user_data
), movie_data as (
    select m.title as results, mr.avg_rating from Movies m join (select movie_id, avg(rating*1.0) as avg_rating from Movie_Rating where MONTH(created_at)=2 and YEAR(created_at)=2020 group by movie_id) mr on m.movie_id=mr.movie_id 
), movie_data1 as (
    select results, avg_rating, rank() over(order by avg_rating desc, results) as r from movie_data
)
    select top 1 results from user_data1 where r=1
    union 
    select top 1 results from movie_data1 where r=1
