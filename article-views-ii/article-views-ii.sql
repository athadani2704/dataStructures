/* Write your T-SQL query statement below */


with distinct_view as (
    select distinct * from Views
)
    select distinct a.viewer_id as id from distinct_view a join distinct_view b on 
    a.viewer_id=b.viewer_id and a.article_id<>b.article_id and a.view_date=b.view_date 
    order by a.viewer_id