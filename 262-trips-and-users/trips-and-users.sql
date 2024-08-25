#divisor
#select t.request_at, count(t.id) from Trips t join Users u on t.client_id=u.users_id where t.status!="completed" and u.banned='No' group by t.request_at;
#denominator
# select t.request_at, count(t.id) from Trips t join Users u on t.client_id=u.users_id where u.banned='No' group by t.request_at;

select 
t.request_at as Day, 
ROUND((
(select count(t1.id) from Trips t1 join Users u1 on t1.client_id=u1.users_id join Users u1_driver ON t1.driver_id = u1_driver.users_id where t1.status!="completed" and u1.banned='No' and u1_driver.banned='No' and t1.request_at=t.request_at)/
(select count(t2.id) from Trips t2 join Users u2 on t2.client_id=u2.users_id join Users u2_driver ON t2.driver_id = u2_driver.users_id where u2.banned='No' and u2_driver.banned='No' and t2.request_at=t.request_at)),2) as "Cancellation Rate"
from Trips t
where t.request_at between "2013-10-01" AND "2013-10-03"
group by t.request_at
having (select count(t2.id) from Trips t2 join Users u2 on t2.client_id=u2.users_id join Users u2_driver ON t2.driver_id = u2_driver.users_id where u2.banned='No' and u2_driver.banned='No' and t2.request_at=t.request_at)>0;