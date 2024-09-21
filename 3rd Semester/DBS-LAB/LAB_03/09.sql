use bsdsf21a007;

select e.ename as 'Name',  truncate((p.sal + ((p.sal * 0.0333) * 12)), 0) as "Annual Salary After increment"
from employee e, pay p
where e.TITLE = p.TITLE;