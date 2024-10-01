# Write your MySQL query statement below
select 
    user_id as buyer_id,
    u.join_date, 
    ifnull(count(o.order_date),0) as orders_in_2019
from Users u
left join Orders o 
    on u.user_id = o.buyer_id 
    and o.order_date like '2019%'
group by user_id