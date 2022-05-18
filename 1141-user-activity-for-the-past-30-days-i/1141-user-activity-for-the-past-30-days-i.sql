# Write your MySQL query statement below
SELECT activity_date as day, COUNT(DISTINCT user_id) AS active_users
FROM activity
where datediff('2019-07-27', activity_date) < 30 and 
    '2019-07-27' > activity_date
GROUP BY activity_date 