# Write your MySQL query statement below
select c.name as Customers
    from Customers c
    left join Orders o on c.id = o.customerId
        where o.customerId is Null;

# opcja 2 podzapytnie
/*
select name as Customers
from Customers
where id not in (
    select customerId
    from Orders
)
*/