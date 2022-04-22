# Write your MySQL query statement below
SELECT DISTINCT p2.email Email
FROM person p1 JOIN person p2 ON p1.email = p2.email and p1.id <> p2.id;