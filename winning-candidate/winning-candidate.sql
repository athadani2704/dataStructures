/* Write your T-SQL query statement below */

with counts as(
    select Candidate.Name as Name, count(*) as CountOfVote from Candidate join Vote
    on Candidate.id=Vote.CandidateId group by Candidate.Name
    )
    select Name from counts where CountOfVote=(select max(CountOfVote) from counts)
