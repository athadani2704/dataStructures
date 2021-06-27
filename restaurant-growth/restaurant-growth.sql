/* Write your T-SQL query statement below */



with prepare_data as (
    select visited_on, sum(amount) as amount from Customer group by visited_on
), add_ranks as (
    select visited_on, sum(amount) over(order by visited_on rows between 6 preceding and current row) as amount, avg(amount*1.0) over(order by visited_on rows between 6 preceding and current row) as average_amount, row_number() over(order by visited_on) as r from prepare_data
)
    select visited_on, amount, round(average_amount, 2) as average_amount from add_ranks where r>=7