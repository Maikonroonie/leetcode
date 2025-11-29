/* Write your T-SQL query statement below */
/*
SELECT (
    SELECT DISTINCT salary    -- DISTINCT, żeby usunąć duplikaty (np. dwa razy 200)
    FROM Employee
    ORDER BY salary DESC
    OFFSET 1 ROWS             -- Pomiń 1 (najwyższy)
    FETCH NEXT 1 ROW ONLY     -- Weź następny
    ) AS SecondHighestSalary;
*/
select max(e1.salary) as SecondHighestSalary
from Employee e1
where e1.salary < (select
    max(e2.salary)
    from employee e2
) 


