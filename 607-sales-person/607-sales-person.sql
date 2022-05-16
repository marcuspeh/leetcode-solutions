# Write your MySQL query statement below
SELECT salesperson.name
FROM salesperson LEFT JOIN 
        (orders JOIN company ON orders.com_id = company.com_id and company.name = 'RED')
        on salesperson.sales_id = orders.sales_id
WHERE company.name is null;