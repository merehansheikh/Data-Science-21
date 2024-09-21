use employee;
select  job, min(sal)
from employee
group by job
order by job;