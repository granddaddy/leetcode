# Write your MySQL query statement below

select t.Request_at as Day, round(
    1 - coalesce(
        completed/(completed+not_completed)
        , 0.0
    )
    , 2
) as "Cancellation Rate"
from
(
select t.Request_at,
MAX(CASE WHEN t.Status = 'completed' then t.c else 0 end) as completed,
MAX(CASE WHEN t.Status != 'completed' then t.c else 0 end) as not_completed
from
(
select count(t.Status) as c, t.Status as Status, t.Request_at as Request_at
from
(
select *
from
(
select *
from Trips
where Request_at >= '2013-10-01' and
Request_at <= '2013-10-03'
) t
inner join
(select *
 from Users
 where Banned = 'No'
 and Role != 'partner'
 ) u
on t.Client_Id = u.Users_Id
) t
inner join
(select *
 from Users
 where Banned = 'No'
 and Role != 'partner'
 ) u
on t.Driver_id = u.Users_Id
group by t.Status, t.Request_at
) t
group by t.Request_at
) t
