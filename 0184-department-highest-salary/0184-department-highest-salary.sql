SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e JOIN Department d
ON e.departmentId = d.id
WHERE e.salary = (
    SELECT MAX(salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId -- Korelacja: porównujemy z działem z głównego --zapytania
);
/*
--drugi sposob
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e JOIN Department d
ON e.departmentId = d.id
JOIN (
    -- To podzapytanie zwraca tabelę z maksymalnymi zarobkami dla działu
    SELECT departmentId, MAX(salary) as max_salary
    FROM Employee
    GROUP BY departmentId
) m 
ON e.departmentId = m.departmentId 
AND e.salary = m.max_salary; -- Kluczowe: łączymy tylko tych, którzy mają MAX pensję
*/

