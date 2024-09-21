
## Task 01
SELECT eno, name, mgr ,CONCAT('-', LPAD(salary, 10, '-')) AS padded_salary,hire_date
FROM employees
WHERE name LIKE 'g%' OR name LIKE 'a%' OR name LIKE 'w%' OR name LIKE 's%';

## Task 02

SELECT SAL, HIREDATE
FROM EMP
WHERE ENAME LIKE '%N' AND MONTH(HIREDATE) = 3;


##task 03

SELECT e.ename
FROM employees e
WHERE (SUBSTRING(e.ename, 2, 1) = 'a' OR SUBSTRING(e.ename, 2, 1) = 's')
AND SUBSTRING(e.ename, 3, 3) = 'manager'
AND e.department_id = 30;

## Task 04
SELECT ename, salary, salary*5 AS DREAM_SALARY
FROM employees;

## Task -05
SELECT ename, salary, LEAST(salary*0.10, 1000) AS BONUS
FROM employees;

## TAsk - 06
SELECT ename, salary, commission*0.15 AS COMMISSION
FROM employees
WHERE commission IS NOT NULL;

## Task 07
SELECT deptno AS DEPT_NO, COUNT(*) AS NUM_EMPLOYEES, AVG(sal) AS AVG_SALARY
FROM emp
GROUP BY deptno
ORDER BY deptno;

## Task 08
SELECT ENAME AS ENAME, SAL AS SALARY, HIREDATE AS HIRE_DATE
FROM EMP
WHERE HIREDATE BETWEEN '2005-01-01' AND '2013-12-31';



## TAsk -09

SELECT DEPT.DEPTNO AS DEPT_NO, DEPT.DNAME AS DEPT_NAME, SUM(EMP.SAL) AS TOTAL_SALARY
FROM DEPT
JOIN EMP ON DEPT.DEPTNO = EMP.DEPTNO
GROUP BY DEPT.DEPTNO, DEPT.DNAME
ORDER BY DEPT.DEPTNO;
 
 
 
## Task -10
SELECT LPAD(ENAME, 15, '*') AS EMPLOYEE_NAME_PADDED, DATE_ADD(HIREDATE, INTERVAL 3 MONTH) AS HIRE_DATE_PLUS_THREE_MONTHS,LPAD(JOB_TITLE, 15, '*') AS JOB_TITLE_PADDED
FROM EMPLOYEES;


## Task 11

INSERT INTO employee (eno, ename, hiredate, job, sal, mgr, deptno) 
VALUES (101, 'John Doe', '2023-04-05', 'Software Engineer', 75000, 100, 30);



## Task 12
SELECT ename, sal
FROM employee
WHERE deptno = (SELECT deptno FROM dept WHERE dname = 'SALES');


## Task 13

CREATE VIEW low_earners AS
SELECT ename, salary
FROM employee
WHERE salary < 1000;
#show the low earners
SELECT * FROM low_earners;


## Task 14

CREATE VIEW hired_between_2008_and_2023 AS
SELECT ename, hiredate
FROM employee
WHERE hiredate BETWEEN '2008-01-01' AND '2023-12-31';


## Task 15

CREATE VIEW unassigned_employees AS
SELECT ename
FROM employee
WHERE deptno IS NULL;































