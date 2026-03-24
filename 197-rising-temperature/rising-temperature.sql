-- Write your PostgreSQL query statement below
select today.id from
weather today cross join weather yesterday
where today.recordDate = yesterday.recordDate + interval  '1 day'
and today.temperature > yesterday.temperature