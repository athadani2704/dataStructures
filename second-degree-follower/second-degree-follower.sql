# Write your MySQL query statement below


select a.follower as follower, count(distinct b.follower) as num from 
follow a join follow b on 
a.follower=b.followee group by a.follower order by a.follower