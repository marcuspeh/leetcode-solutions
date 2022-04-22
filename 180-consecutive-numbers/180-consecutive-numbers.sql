# Write your MySQL query statement below
select distinct l1.num ConsecutiveNums 
from logs l1, logs l2, logs l3
where l1.id + 1 = l2.id  AND
    l2.id + 1 = l3.id AND
    l1.num = l2.num AND 
    l2.num = l3.num