-- Write your PostgreSQL query statement below
select p.product_name, s.year, s.price 
from sales as s join product as p
using (product_id) 
