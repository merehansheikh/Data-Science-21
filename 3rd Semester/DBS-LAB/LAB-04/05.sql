use employee;
select job JOB, max(sal) as "Max Salary"
from employee
where job != "President"
group by job
order by max(sal)