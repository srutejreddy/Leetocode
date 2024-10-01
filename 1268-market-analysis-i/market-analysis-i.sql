# Write your MySQL query statement below
select  
    user_id as buyer_id,
    join_date,
    ifnull(orders_count,0) as orders_in_2019
from Users u
left join 
    (select 
        user_id, 
        count(*) as orders_count
    from Users u
    join Orders o 
    on u.user_id = o.buyer_id
    where substr(o.order_date,1,4) = '2019'
    group by user_id) temp 
using(user_id)