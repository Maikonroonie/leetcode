# Write your MySQL query statement below

select email as Email
from Person
group by email
having count(email) > 1;

/* window function
SELECT DISTINCT email
FROM (
    SELECT 
        email, 
        COUNT(*) OVER (PARTITION BY email) as cnt
    FROM Person
) as t
WHERE cnt > 1;
*/

/* self join
SELECT DISTINCT p1.email
FROM Person p1
JOIN Person p2 
    ON p1.email = p2.email     
    AND p1.id != p2.id;
*/

/* podzapytanie
SELECT DISTINCT p1.email
FROM Person p1
WHERE (
    SELECT COUNT(*) 
    FROM Person p2 
    WHERE p1.email = p2.email
) > 1;
*/

/* cross apply
SELECT DISTINCT p1.email
FROM Person p1
CROSS APPLY (
    SELECT COUNT(*) as cnt
    FROM Person p2
    WHERE p1.email = p2.email
) as c
WHERE c.cnt > 1;
*/