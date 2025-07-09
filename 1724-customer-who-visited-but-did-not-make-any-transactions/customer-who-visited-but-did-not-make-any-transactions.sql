/* Write your PL/SQL query statement below */
select v.customer_id as customer_id, count(*) as count_no_trans
from Visits v 
left join Transactions t on v.visit_id = t.visit_id
where transaction_id is NULL
group by v.customer_id
-- order by customer_id