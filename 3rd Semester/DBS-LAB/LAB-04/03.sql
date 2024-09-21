use employee;
select avg(sal)
from employee
group by DEPTNO
order by avg(sal);