# Write your MySQL query statement below
SELECT user_id as buyer_id, join_date, count(order_id) as orders_in_2019
FROM users LEFT JOIN orders ON orders.buyer_id = users.user_id AND YEAR(order_date) = 2019
GROUP BY user_id, join_date
