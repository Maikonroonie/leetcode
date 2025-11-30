/* Write your T-SQL query statement below */
select distinct t1.id,
    Case
        when t1.p_id is Null then 'Root'
        when t2.id is not null then 'Inner'
        else 'Leaf'
        end as type
from Tree t1 left join Tree t2
on t1.id = t2.p_id;

--druga metoda
/* 
SELECT id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;
*/