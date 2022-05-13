# Write your MySQL query statement below
SELECT employee_id
FROM (
    SELECT * FROM employees LEFT JOIN salaries USING(employee_id)
    UNION
    SELECT * FROM employees RIGHT JOIN salaries USING(employee_id)
    ) as t
WHERE name is null or salary is null
ORDER BY employee_id;
