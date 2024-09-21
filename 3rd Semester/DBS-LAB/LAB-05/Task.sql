use bsdsf21a007;

## task-01
SELECT emp.Title, asg.Resp
FROM Employee as emp, Asg, pay
WHERE emp.Eno = Asg.Eno
AND emp.Title = pay.Title
group by emp.title ,asg.resp
Having min(sal) > avg(sal); 

## task-02
SELECT emp.Title, Avg (asg.Dur), Avg (pay.Sal)
FROM Employee as emp, Pay, Proj, Asg
WHERE Emp.Title = Pay.Title
AND Emp.Eno = Asg.Eno
AND Asg.Pno = Proj.Pno
GROUP BY emp.Title;

## task-03
SELECT *
FROM Employee as emp, Asg, Proj, Pay
Where Emp.Eno = Asg.Eno
AND Asg.Pno = Proj.Pno
AND Emp.Title = Pay.title
AND Asg.Dur in (Select Avg (asg.Dur)
FROM Asg, Employee as emp
WHERE Asg.Eno = Emp.Eno
GROUP BY emp.title);

## task-04
SELECT emp.Ename, emp.Title, asg.Resp, pay.Sal, proj.budget
FROM Employee as emp, Asg, Proj, Pay
Where Emp.Eno = Asg.Eno
AND Asg.Pno = Proj.Pno
AND Emp.Title = Pay.title
and proj.Pname like '_sales%' 
or proj.Pname = 'instrumentation';

## task-05
SELECT asg.Dur, asg.Resp, proj.Pno, emp.Eno, emp.Title
FROM Employee as emp, Asg, Proj, Pay
Where Emp.Eno = Asg.Eno
AND Asg.Pno = Proj.Pno
AND Emp.Title = Pay.title
And proj.Pno IN ('P1', 'P2', 'P3')
AND pay.Sal between 27000 and 40000
AND proj.Pname like '_a%';

## task-06
select e.ename, p.pname
from employee e, asg a, proj p
Where E.Eno = A.Eno
AND A.Pno = P.Pno
and p.pname in ('instrumentation', 'maintenance')
and a.dur between 6 and 48
order by e.ename;

## task-07
select proj.pname, proj.budget, pay.sal
from proj, pay, employee as emp, asg 
Where Emp.Eno = Asg.Eno
AND Asg.Pno = Proj.Pno
AND Emp.Title = Pay.title
and pay.sal > (select avg(pay.sal) from pay, employee as emp
where pay.title = emp.title);

## task-08
select p.sal
from employee emp, asg a, pay p
where emp.eno = a.eno
and emp.title = p.title
and emp.title = 'Elec.Eng'
and a.resp = 'Manager'
and a.dur > 24
and p.sal < 20000;

## task-09
select e.ename
from employee as e, asg as a, proj as p
where e.eno = a.eno
and a.pno = p.pno
and p.budget > (select avg(proj.budget) from proj);

##task-10
select desg.DesignationName , emp_desg.SalaryPaid,
dep.DepartmentName, dep.facultyname
from Employee as e, Designation as desg,
Employee_Designation as emp_desg, Department as dep,
Employee_Department as emp_dept
where emp.empno = emp_desg.empno
and desg.designationid = emp_desg.designation id
and dep.departmentid = emp_dep.departmentid
and emp.empno = emp_dep.empno
and desg.DesignationName in ('Associate Professor','Lecturers');

##task-11
select max(len(e.ename))
from employee e;

## task-12
select e.ename, dept.facultyid, e.eno 
from employee as e, department as dept, 
employee_department as emp_dept
where e.empno = emp_dept.empno
and emp_dept.departmentid = dept.departmentid;

## task-13
select emp.ename
from employee as emp, asg as a, proj p
where emp.eno = a.eno
and a.pno = p.pno
and emp.ename = 'Elec.Eng'
and a.resp = 'Manager'
and p.budget > 250000;

## task-14
select emp.ename, proj.pname, p.sal, round(p.sal*1.1 ,2) as Bonus
from employee as emp, proj, pay p, asg a
where emp.eno = a.eno
and a.pno = proj.pno
and emp.title = p.title
and a.dur > 24;

##task-15
select emp.ename, a.resp
from employee as emp, proj, pay p, asg a
where emp.eno = a.eno
and a.pno = proj.pno
and emp.title = p.title
and p.sal in (40000, 34000, 27000)
and proj.pname not in ('CAD/CAM', "instrumentation")
and proj.pno in ('P1', 'P2', 'P3')
and (p.sal < 48000
or p.sal< 36000);