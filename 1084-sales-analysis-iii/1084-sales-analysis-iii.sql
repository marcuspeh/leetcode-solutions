# Write your MySQL query statement below
SELECT DISTINCT product_id, product_name
FROM Product NATURAL JOIN Sales 
WHERE NOT EXISTS (
    SELECT 1 
    FROM Sales
    WHERE (sale_date < '2019-01-01' OR sale_date > '2019-03-31' ) AND
        product_id = Product.product_id
)