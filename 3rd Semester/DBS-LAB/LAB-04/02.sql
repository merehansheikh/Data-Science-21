use employee;
select job as 'Distinct Jobs', count(ename)
from employee
group by job
order by job asc