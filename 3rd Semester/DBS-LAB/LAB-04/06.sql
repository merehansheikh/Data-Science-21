use employee;
select deptno as 'Department', sum(sal) as Sum
from employee
where mgr is not null
group by DEPTNO
order by sum(sal);
