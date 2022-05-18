# Write your MySQL query statement below
SELECT customer_number
FROM Orders
GROUP BY customer_number
HAVING count(order_number) = (
    SELECT count(order_number)
    FROM orders
    GROUP BY customer_number
    ORDER BY count(order_number) desc
    LIMIT 1
)