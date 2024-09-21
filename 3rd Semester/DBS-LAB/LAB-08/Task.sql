-- Insert a new employee with EMPNO 8000, ENAME 'JOHN', JOB 'ANALYST', MGR 7566, 
-- HIREDATE '2019-01-01', SAL 4000, COMM NULL, DEPTNO 20, and ensure that the ENAME is 
-- capitalized properly

use employee;
INSERT INTO employee (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO)
VALUES (8000, UPPER('John'), 'ANALYST', 7566, '2019-01-01', 4000, NULL, 20);



-- Update the salary (SAL) of all employees in the 'SALESMAN' job to be increased by 15%, 
-- rounded to the nearest integer

UPDATE employee
SET SAL = ROUND(SAL * 1.15)
WHERE JOB = 'SALESMAN';



-- Delete all employees whose HIREDATE is before '2010-01-01' and who have a NULL value in 
-- the COMM column

DELETE FROM employee
WHERE HIREDATE < '2010-01-01' AND COMM IS NULL;


-- Select the DEPTNO and the total salary (SAL + COMM) of employees in each department 
-- from the EMPLOYEE table, and order the result by the total salary in descending order


SELECT DEPTNO, SUM(SAL + IFNULL(COMM, 0)) AS TOTAL_SALARY
FROM EMPLOYEE
GROUP BY DEPTNO
ORDER BY TOTAL_SALARY DESC;



-- Select the ENAME, JOB, and the length of service (in years) for employees whose JOB is 
-- 'MANAGER', and calculate the length of service as the difference between the current date 
-- and the HIREDATE, rounded to the nearest integer


SELECT ENAME, JOB, ROUND(DATEDIFF(now(), HIREDATE)/365) AS LENGTH_OF_SERVICE
-- OR  SELECT ENAME, JOB, '2023' - YEAR(HIREDATE) AS LENGTH_OF_SERVICE
FROM EMPLOYEE
WHERE JOB = 'MANAGER';

-- Select the DEPTNO, the average salary (SAL) of employees in each department, and the 
-- difference between the highest and lowest salary in each department, and display the result 
-- only for departments where the average salary is greater than 2000


SELECT DEPTNO, AVG(SAL) AS AVG_SAL, (MAX(SAL) - MIN(SAL)) AS SAL_DIFF
FROM EMPLOYEE
GROUP BY DEPTNO
HAVING AVG_SAL > 2000;


-- Select the ENAME and the total SAL for each TITLE from the EMP and PAY tables combined, 
-- where the ENAME in the EMP table starts with the letter 'J', grouped by TITLE, and display 
-- only those with a total SAL greater than 50000.

USE bsdsf21a007;

SELECT E.ENAME, SUM(P.SAL) AS TOTAL_SAL
FROM EMPLOYEE E, PAY P 
WHERE E.TITLE = P.TITLE
AND E.ENAME LIKE 'J%'
GROUP BY E.TITLE, E.ENAME
HAVING SUM(P.SAL) > 50000;

-- Select the ENAME, PNAME, and SAL of employees who are assigned to the same project 
-- (PNO) in the ASG table, and whose SAL is greater than the average SAL of all employees in 
-- the EMP table

SELECT E.ENAME, P.PNAME, PAY.SAL
FROM EMPLOYEE E, PROJ P, PAY, ASG A
WHERE E.ENO = A.ENO AND P.PNO = A.PNO AND E.TITLE = PAY.TITLE 
HAVING PAY.SAL > (SELECT 
AVG(SAL)
FROM PAY);


-- Select the ENAME and PNAME of employees who are assigned to projects with a BUDGET 
-- greater than 200000 in the PROJ table, and whose TITLE in the EMP table is 'Syst.Anal' or 
-- 'Anal.Eng'. 

SELECT E.ENAME, P.PNAME
FROM EMPLOYEE E, PROJ P,ASG A
WHERE E.ENO = A.ENO AND P.PNO = A.PNO
AND P.BUDGET > 200000 
AND E.TITLE in ('Syst.Anal' ,'Anal.Eng');


-- Select the ENAME, TITLE, and the number of assignments (count of rows) from the ASG table 
-- for each employee from the EMP table, ordered by the number of assignments in 
-- descending order


SELECT E.ENAME, E.TITLE, COUNT(E.ENO) AS Number_of_Assignment
FROM EMPLOYEE E, ASG A
WHERE E.ENO = A.ENO
group BY E.ENAME, E.TITLE
order BY COUNT(*);






