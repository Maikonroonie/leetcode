/* Write your T-SQL query statement below */
select s.name
from SalesPerson s
except
select s.name
from SalesPerson s join Orders o
on o.sales_id = s.sales_id join Company c
on o.com_id = c.com_id
where c.name = 'RED'