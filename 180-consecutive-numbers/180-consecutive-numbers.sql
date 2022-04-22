# Write your MySQL query statement below
select distinct l1.num ConsecutiveNums 
from logs l1 JOIN logs l2 on l1.id = l2.id - 1 AND l1.num = l2.num
    JOIN logs l3 on l2.id = l3.id - 1 AND l2.num = l3.num