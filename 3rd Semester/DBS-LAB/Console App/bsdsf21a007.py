import mysql.connector as sql

db = sql.connect(
host="localhost",
user="root",
password="abdullah69")

turuk = "use employee;"
cursor = db.cursor()
cursor.execute(turuk)

# Task 02
# Write a Python program to retrieve data from the employee table where the salary
# is greater than 1000

query2 = "SELECT * FROM employee\
    where sal > 1000 "
# cursor = db.cursor()
cursor.execute(query2)
result = cursor.fetchall()

for data in result:
    print(data, '\n')
    
# Task 03
# Write a Python program to retrieve data from the employee table where the hire
# date is between 2002 to 2006.

query3 = "SELECT * FROM employee\
    where year(hiredate) between 2002 and 2006 "
cursor = db.cursor()
cursor.execute(query3)
result = cursor.fetchall()

for data in result:
    print(data, '\n')
    
# Task 04
# Write a Python program to retrieve data from the employee table where the
# department number is 10.

query4 = "SELECT * FROM employee\
    where deptno = 10 "
cursor = db.cursor()
cursor.execute(query4)
result = cursor.fetchall()

for data in result:
    print(data, '\n')

# Task 05
# Write a Python program to retrieve data from the employee table where the
# manager ID is not null


query5 = "SELECT * FROM employee\
    where mgr is not null"
cursor = db.cursor()
cursor.execute(query5)
result = cursor.fetchall()

for data in result:
    print(data, '\n')

# Task 06
# Write a Python program to retrieve data from the employee table where the
# commission is null



query6 = "SELECT * FROM employee\
    where comm is not null"
cursor = db.cursor()
cursor.execute(query6)
result = cursor.fetchall()

for data in result:
    print(data, '\n')

# Task 07
# Write a Python program to retrieve data from the employee table where the
# employee name starts with the letter 'S'


query7 = "SELECT * FROM employee\
    where ename like 'S%' "
cursor = db.cursor()
cursor.execute(query7)
result = cursor.fetchall()

for data in result:
    print(data, '\n')
# Task 08
# Write a Python program to retrieve data from the employee table where the
# department number is either 10 or 20

query8 = "SELECT * FROM employee\
    where deptno = '10' or deptno = '20' "
cursor = db.cursor()
cursor.execute(query8)
result = cursor.fetchall()

for data in result:
    print(data, '\n')


# Task 09
# Write a Python program to retrieve data from the employee table where the hire
# date is the latest

query9 = "SELECT * FROM employee\
    where hiredate = (Select max(hiredate) from employee) "
cursor = db.cursor()
cursor.execute(query9)
result = cursor.fetchall()

for data in result:
    print(data, '\n')
# Task 10
# Write a Python program to retrieve data from the employee table where the
# employee’s name and salary are both displayed in descending order


query10 = "SELECT * FROM employee\
    order by ename, sal -- desc"
cursor = db.cursor()
cursor.execute(query10)
result = cursor.fetchall()

for data in result:
    print(data, '\n')
