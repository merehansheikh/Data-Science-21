use employee;
select deptno , max(HIREDATE) as 'Most Fresh Employee'
from employee
group by deptno
