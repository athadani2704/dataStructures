/* Write your T-SQL query statement below */
with uniqF as (
    select distinct sender_id, send_to_id from FriendRequest
), uniqR as (
    select distinct requester_id, accepter_id from RequestAccepted
)
select round(cast((select count(*) from uniqR) as float)/(select case when (select count(*) from uniqF)=0 then 1 else (select count(*) from uniqF) end), 2) as accept_rate