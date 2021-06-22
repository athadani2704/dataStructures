/* Write your T-SQL query statement below */

-- with cte as(
--     select player_id, event_date, games_played, row_number() over(partition by player_id order by event_date) as r from activity
-- )
-- select distinct a.player_id, a.event_date, (case when a.r=b.r+1 then a.games_played+b.games_played when a.r=1 then a.games_played else 0 end) as games_played_so_far from cte a join cte b
-- on a.player_id=b.player_id where a.r=b.r+1 or a.r=1


select a.player_id, a.event_date, sum(b.games_played) as games_played_so_far from activity a join activity b
on a.player_id=b.player_id where a.event_date>=b.event_date group by a.player_id, a.event_date
