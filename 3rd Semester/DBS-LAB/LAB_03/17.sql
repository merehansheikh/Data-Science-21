use employee; 
select e.ename as 'Employee Name', d.dname as 'Department Name', d.loc as'Department Location'
from employee e, dept d
where e.DEPTNO = d.DEPTNO;