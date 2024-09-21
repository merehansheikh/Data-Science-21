class Employee:
    def __init__(self):
        self.employee_name = ''
        self.employee_number = 0


class ProductionWorker(Employee):
    def __init__(self,):
        super().__init__()
        self.shift_number = 0
        self.hourly_pay_rate = 0
    def set_shift(self, shift):
        self.shift_number = shift
    def set_pay_rate(self, rate):
        self.hourly_pay_rate = rate
    def display(self):
        print(f"The name of the Employee is {self.employee_name} and his number is {self.employee_number}, has a shift {self.shift_number} with ${self.hourly_pay_rate} per hour")
def main():
    w1 = ProductionWorker()
    w1.employee_name = input('Enter the worker name: ')
    w1.employee_number = int(input('Enter the employe number: '))
    w1.set_shift(int(input("Enter the shift\n1: Day\n2: Night\n")))
    w1.set_pay_rate(int(input("Enter the rate: ")))
    w1.display()
main()