-- Write your PostgreSQL query statement below
select today.id
from
weather today cross join weather yesterday
where today.recordDate = yesterday.recordDate + INTERVAL '1 Day'
and today.temperature > yesterday.temperature