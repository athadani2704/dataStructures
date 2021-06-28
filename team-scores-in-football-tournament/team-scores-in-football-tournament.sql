/* Write your T-SQL query statement below */


with create_table as (
    select host_team, guest_team, (select team_name from Teams where team_id=Matches.host_team) as host_name, 
    (select team_name from Teams where team_id=Matches.guest_team) as guest_name, 
    iif(host_goals>guest_goals, 3, iif(host_goals=guest_goals, 1, 0)) as host_nums, 
    iif(host_goals<guest_goals, 3, iif(host_goals=guest_goals, 1, 0)) as guest_nums 
    from Matches
), all_teams as (
    select host_team as team_id, host_name as team_name, host_nums as num_points from create_table
    union all
    select guest_team as team_id, guest_name as team_name, guest_nums as num_points from create_table
    union all
    select team_id, team_name, 0 as num_points from Teams where team_id not in 
        (
         select distinct host_team from Matches
         union
         select distinct guest_team from Matches
        )
)
    select team_id, team_name, sum(num_points) as num_points from all_teams group by team_id, team_name 
    order by sum(num_points) desc, team_id