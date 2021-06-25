/* Write your T-SQL query statement below */


select fo.follower as follower, count(distinct f.follower) as num from follow fo join follow f on 
fo.follower=f.followee group by fo.follower order by fo.follower