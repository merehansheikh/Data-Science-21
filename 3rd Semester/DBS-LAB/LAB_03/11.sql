select e.ename as 'Name',  round((p.sal + ((p.sal * 0.0333) * 12))) as "Annual Salary After increment"
from employee e, pay p
where e.TITLE = p.TITLE;