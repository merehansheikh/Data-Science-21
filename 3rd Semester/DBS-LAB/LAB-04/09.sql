use employee; 
select *
from employee as e, dept as d
where e.DEPTNO = d.DEPTNO
order by e.ename asc