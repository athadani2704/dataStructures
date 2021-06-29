/* Write your T-SQL query statement below */

select distinct b.id, (select name from Accounts where id=b.id) as name from 
Logins b join Logins c on 
b.id=c.id where datediff(day, b.login_date, c.login_date) between 1 and 4 
group by b.id, b.login_date 
having count(distinct c.login_date)=4 order by b.id


-- SELECT
-- DISTINCT l1.id,
-- (SELECT name FROM Accounts WHERE id = l1.id) AS name
-- FROM Logins l1
-- JOIN Logins l2 ON l1.id = l2.id
-- AND DATEDIFF(day, l2.login_date, l1.login_date) BETWEEN 1 AND 4
-- GROUP BY l1.id, l1.login_date
-- HAVING COUNT(DISTINCT l2.login_date) = 4