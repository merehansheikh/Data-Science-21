use employee;
select deptno , min(HIREDATE) as 'Most Senior Employee'
from employee
group by deptno
