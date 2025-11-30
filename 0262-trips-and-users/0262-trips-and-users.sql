/* Write your T-SQL query statement below */

select t.request_at as Day,
round(
cast(
sum(case when t.status != 'completed' then 1 else 0 end) as float)/
count(*), 2) as [Cancellation Rate]
from Trips t
where t.request_at between '2013-10-01' and '2013-10-03'
    and t.client_id not in (select users_id from Users where banned = 'Yes')
    and t.driver_id not in (select users_id from Users where banned = 'Yes')
group by t.request_at;