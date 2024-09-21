from full_time_employee import *
from hourly_employee import *
from payroll import *

payroll = Payroll()

payroll.add(Full_Time_Employee('Azam', 'Ali', 60000))
payroll.add(Full_Time_Employee('Munir', 'Raza', 65000))
payroll.add(Hourly_Employee('Saeed', 'Malik', 100, 500))
payroll.add(Hourly_Employee('Babar', 'Khan', 150, 400))
payroll.add(Hourly_Employee('Kalim', 'Ullah', 100, 550))

payroll.print()
