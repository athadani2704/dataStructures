/* Write your T-SQL query statement below */


select q.id, q.year, isnull(NPV.npv, 0) as npv from Queries q left join NPV on 
q.id=NPV.id and q.year=NPV.year