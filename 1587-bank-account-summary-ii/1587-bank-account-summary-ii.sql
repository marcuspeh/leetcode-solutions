# Write your MySQL query statement below
SELECT name as NAME, SUM(amount) as BALANCE
FROM Users JOIN transactions ON users.account = transactions.account
GROUP BY name
HAVING SUM(amount) > 10000