use bsdsf21a007; 
select e.ename, p.pname, a.dur
from employee  e, proj p, asg  a
where e.eno = a.eno
and a.pno = p.pno
order by ename