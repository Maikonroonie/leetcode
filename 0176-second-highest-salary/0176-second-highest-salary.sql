/* Write your T-SQL query statement below */
/*
select top 1 salary as SecondHighestSalary
from(
    select top 2 salary
    from Employee
    order by salary desc
    ) as topsalaries
order by salary 
*/
select max(e1.salary) as SecondHighestSalary
from Employee e1
where e1.salary < (select
    max(e2.salary)
    from employee e2
) 

