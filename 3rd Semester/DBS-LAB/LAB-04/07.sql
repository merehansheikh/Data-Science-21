use employee;
select ename Name, sal Salary
from employee
where sal < 40000 and ename like ('J%')
order by sal 