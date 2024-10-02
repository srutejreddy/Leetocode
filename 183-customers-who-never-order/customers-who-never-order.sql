# Write your MySQL query statement below
select 
    name as Customers
from Customers c1
where id not in
    (select customerId
    from Orders )