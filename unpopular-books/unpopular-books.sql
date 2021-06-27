/* Write your T-SQL query statement below */


with last_year as (
    select book_id, sum(iif(dispatch_date>dateadd(year, -1, cast('2019-06-23' as date)), quantity, 0)) as total_quantity from Orders group by book_id
)
    select b.book_id, b.name from Books b left join last_year l on 
    b.book_id=l.book_id where (l.total_quantity is null or l.total_quantity<10) and b.available_from<dateadd(month, -1, cast(('2019-06-23') as date))