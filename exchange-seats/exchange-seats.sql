/* Write your T-SQL query statement below */



select case when (a.id%2)=0 then a.id-1 
            when (a.id%2)=1 and (a.id<(select max(id) from seat)) then a.id+1
            --when ((select max(id) from seat)%2)=0 then a.id+1
            else a.id
            end as id, a.student from seat a 
            order by id-- join seat b on a.id=b.id-1