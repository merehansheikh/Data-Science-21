select p.SAL
from employee e, pay p
where e.TITLE = p.TITLE
and p.sal > 1000;