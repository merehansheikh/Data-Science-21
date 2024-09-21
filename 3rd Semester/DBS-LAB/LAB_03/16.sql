use employee;

select e1.ename as Names, e2.ename as Manager
from employee e1, employee e2
where e1.mgr = e2.EMPNO;