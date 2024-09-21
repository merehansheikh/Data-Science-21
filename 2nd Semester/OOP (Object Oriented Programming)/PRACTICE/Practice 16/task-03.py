class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def set(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self, day):
        self.day = day

    def get_month(self, month):
        self.month = month

    def get_year(self, year):
        self.year = year

    def __str__(self) -> str:
        return f'{self.day}/{self.month}/{self.year}'


class Employee:
    def __init__(self, emp_no, name, designation, j_date, salary, p_date=''):
        self.emp_no = emp_no
        self.name = name
        self.designation = designation
        self.j_date = j_date
        self.salary = salary
        self.p_date = p_date
    def __str__(self):
        if self.p_date == '':
            return f'{self.name} is a employee in this company and has a number of {self.emp_no} and is {self.designation} in the company and joined this company in {self.j_date} with the salary of {self.salary}'
        return f'{self.name} is a employee in this company and has a number of {self.emp_no} and is {self.designation} in the company and joined this company in {self.j_date} with the salary of {self.salary} and got promoted in {self.p_date}'
    
def main():

    j_date = Date(20, 9, 2003)
    p_date = Date(21, 10, 2004)
    emp1 = Employee(69, 'ALI', 'CEO', j_date, 29000, p_date)
    print(emp1)
main()
