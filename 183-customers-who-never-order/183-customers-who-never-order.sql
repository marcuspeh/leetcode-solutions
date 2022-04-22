# Write your MySQL query statement below
SELECT name Customers 
FROM Customers
WHERE id not in (SELECT customerId from orders)