-- Write your PostgreSQL query statement below
select eu.unique_id, em.name from
employees as em left join EmployeeUNI as eu 
on em.id = eu.id