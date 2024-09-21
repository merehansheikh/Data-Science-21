use employee;
select e1.ename as Employee, e2.ENAME as Manager
from employee as e1, employee as e2
where e1.mgr = e2.empno
order by e1.ENAME