# Write your MySQL query statement below
SELECT name, COALESCE(sum(distance), 0) as travelled_distance
FROM users LEFT JOIN rides ON rides.user_id = users.id
GROUP BY name
ORDER BY sum(distance) desc, name asc
