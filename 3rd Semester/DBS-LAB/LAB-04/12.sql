use bsdsf21a007;
select *
from asg
right outer join proj 
on asg.pno = proj.pno