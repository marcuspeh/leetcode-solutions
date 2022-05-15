# Write your MySQL query statement below
SELECT name
FROM salesperson
WHERE name NOT IN (
    SELECT salesperson.name
    FROM salesperson JOIN orders on salesperson.sales_id = orders.sales_id
        JOIN company ON orders.com_id = company.com_id
    WHERE company.name = 'RED'
    );