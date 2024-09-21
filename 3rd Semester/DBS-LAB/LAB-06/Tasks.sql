#EMPLOYEE (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, HIRE_DATE, JOB_ID, SAL, COMM, MGR, DEPTNO)
#DEPARTMENT (DeptNO, DeptName, LOC)
#SALGRADE (GRADE, LOSAL, HISAL)

#Q1: Display the employee last name, job ID, and start date of employees hired between February 20, 1998, and May 1, 1998. Order the query in ascending order by start date
select e.last_name, e.job_id, e.hiredate
from employee
where e.hiredate between 'February 20, 1998' and 'May 1, 1998'
order by e.hiredate;

#Q2: Display the name and job title of all employees who do not have a manager
SELECT FIRST_NAME, LAST_NAME, JOB_ID 
FROM EMPLOYEE 
WHERE MGR IS NULL;

#Q3: Create a query to display the name and hire date of any employee hired after employee Davies
SELECT FIRST_NAME, LAST_NAME, HIRE_DATE 
FROM EMPLOYEE 
WHERE HIRE_DATE > (SELECT HIRE_DATE FROM EMPLOYEE WHERE LAST_NAME = 'Davies');

#Q4: Give employee number, name, hire date, commission, department id, department name, location, salary grade of all employees those names are Hassan, salary is less than 50000, commission is 2% of the half of their salary
SELECT E.EMPLOYEE_ID, concat(E.FIRST_NAME, ' ', E.LAST_NAME) AS NAME, E.HIRE_DATE, 
  (E.SAL/2)*0.02 AS COMMISSION, E.DEPTNO, D.DeptName, D.LOC, 
  S.GRADE 
FROM EMPLOYEE E ,DEPARTMENT D, SALGRADE S
WHERE E.DEPTNO = D.DeptNO AND
S.SAL = E.SAL AND E.SAL BETWEEN S.LOSAL AND S.HISAL 
AND E.FIRST_NAME = 'Hassan' AND E.SAL < 50000;

#Q5: Write a query to display the number of people with the same job. 
SELECT JOB_ID, COUNT(*) AS NUM_OF_PEOPLE 
FROM EMPLOYEE 
GROUP BY JOB_ID;

#Q6: Write a query to display the total salary for each department, including any commissions
SELECT D.DeptName, SUM(E.SAL + CASE WHEN E.COMM IS NULL THEN 0 ELSE E.COMM END) AS TOTAL_SALARY
FROM EMPLOYEE E, DEPARTMENT D
WHERE E.DEPTNO = D.DeptNO
GROUP BY D.DeptName;

#Q7: Select the top 10 highest paid employees, including their department name and location
SELECT concat(E.FIRST_NAME, ' ', E.LAST_NAME) AS NAME , E.SAL, D.DeptName, D.LOC
FROM EMPLOYEE E, DEPARTMENT D
WHERE E.DEPTNO = D.DeptNO
ORDER BY E.SAL DESC
LIMIT 10;

#Q8: Write a query to display the total number of employees in each department
SELECT D.DeptName, COUNT(*) AS TOTAL_EMPLOYEES
FROM EMPLOYEE E, DEPARTMENT D
WHERE E.DEPTNO = D.DeptNO
GROUP BY D.DeptName;


#Q9: Write a query to display those employees who have worked for 10 years
SELECT CONCAT(FIRST_NAME, ' ',LAST_NAME)  AS NAME, HIRE_DATE
FROM EMPLOYEE
having (CURRENT_DATE - HIRE_DATE) >= 10;

#Q10: Display all departments and their average employee salary
SELECT D.DeptName, AVG(E.SAL) AS AVERAGE_SALARY
FROM EMPLOYEE E, DEPARTMENT D
WHERE E.DEPTNO = D.DeptNO
GROUP BY D.DeptName;

													#-------- Part-II ---------
								#Worker (Worker_ID, First_Name, Last_Name, Salary, Joining_Date, Department) 
								#Bonus (Worker_ID, Bonus_Date, Bonus_Amount) 
								#Title (Worker_ID, Worker_Title, Affected_From)


select substr(first_name, 1, instr(first_name, ' ')-1)
from worker;

#Q2: Write a query to show only even rows from a worker table
SELECT *
FROM Worker
HAVING Worker_ID % 2 = 0;

#Q3: Display the first name, last name and salary of all workers who earn more than $50,000
SELECT First_Name, Last_Name, Salary
FROM Worker
WHERE Salary > 50000;

#Q4: Display the first name, last name and department of all workers who work in the same department as worker with ID 123
SELECT w.First_Name, w.Last_Name, w.Department
FROM Worker w
WHERE w.Department = (SELECT Department FROM Worker WHERE Worker_ID = 123);

#Q5: Display the first name, last name and bonus amount of all workers who received a bonus on or after '2022-01-01' and who work in the department 'Marketing'
SELECT w.First_Name, w.Last_Name, b.Bonus_Amount
FROM Worker w, BONUS b
WHERE w.Worker_ID = b.Worker_ID
AND b.Bonus_Date >= '2022-01-01'
AND w.Department = 'Marketing';

																# ------ PART - III -------
						#Employee (employee-name, street, city) 
						#Works (employee-name, company-name, salary) 
						#Company (company-name, city) 
						#Manages (employee-name, manager-name)



#Q1: Find the names of all employees who earn more than the average salary of all employees of their company
SELECT w.employee-name
FROM Works w
WHERE w.salary > (
  SELECT AVG(w2.salary)
  FROM Works w2
);


#Q2: Write a query to retrieve the names of all employees who have a salary greater than or equal to the salary of their manager
SELECT e.employee-name
FROM Employee e, Manages m, Employee m2
WHERE e.employee-name = m.employee-name
AND m2.employee-name = m.manager-name
AND e.salary >= m2.salary;

#Q3: Write a query to retrieve the names of all employees who work for companies located in "New York".
SELECT employee_name
FROM Works
WHERE company_name IN (
  SELECT company_name
  FROM Company
  WHERE city = 'New York'
);

#Q4: Write a query to retrieve the names of all employees who work for companies located in the same city as their manager
SELECT e.employee_name
FROM Works e, Works m, Company ec, Company mc
WHERE e.company_name = ec.company_name
AND m.company_name = mc.company_name
AND e.salary >= m.salary
AND e.employee_name != m.employee_name
AND e.employee_name != NULL
AND e.employee_name = m.manager_name
AND ec.city = mc.city;


#Q5: Find the names of all employees in the database who live in the same cities and on the same streets as do their managers.
SELECT e1.employee_name 
FROM Employee e1, Employee e2 
WHERE e1.city = e2.city AND e1.street = e2.street 
AND e1.employee_name != e2.employee_name 
AND e1.manager_name = e2.employee_name;








