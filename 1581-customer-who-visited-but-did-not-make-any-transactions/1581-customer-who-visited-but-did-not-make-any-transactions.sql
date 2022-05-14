# Write your MySQL query statement below
SELECT customer_id, count(*) as count_no_trans
FROM Visits LEFT JOIN Transactions ON 
    visits.visit_id = transactions.visit_id 
WHERE amount is null
GROUP BY customer_id;