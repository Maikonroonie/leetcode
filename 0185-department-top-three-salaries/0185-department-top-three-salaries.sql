/* Write your T-SQL query statement below */

--pracownik jest w top 3 jesli w jego dziale jest mniej niz 3
-- osoby zarabiajace wiecej od niego
select d1.name as Department,  e1.name as Employee, e1.salary as Salary
from Employee e1 join Department d1
    on e1.departmentId = d1.id
where 3 > (
    select count(distinct e2.salary)
    from Employee e2
    where e1.DepartmentId = e2.DepartmentId
    and e2.salary > e1.salary
)