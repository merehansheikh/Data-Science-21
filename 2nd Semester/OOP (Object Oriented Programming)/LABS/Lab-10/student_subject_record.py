import random as r
class Student_Subject_Record:
    student_count = 0
    def __get_probablistic_percentage(self):
        percentage = int(self.__mid / 35 * 100)
        random_value = r.randint(0,10)
        difference_down = percentage - 0
        difference_up = 100 - percentage
        if random_value >= 2 and random_value <=8:
            return r.randint(percentage - difference_down//2, percentage + difference_up//2)
        else:
            return r.randint(0, 100)
    def __init__(self):
        Student_Subject_Record.student_count += 1
        self.__roll_no = Student_Subject_Record.student_count
        self.__mid = r.randint(0,35)
        self.__final = self.__get_probablistic_percentage()*40//100
        self.__sessional = self.__get_probablistic_percentage()*25//100

    def get_mid(self):
        return self.__mid

    def get_final(self):
        return self.__final

    def get_sessional(self):
        return self.__sessional

    def __str__(self):
        return f'{self.__roll_no}\t\t{self.__mid}\t\t{self.__final}\t\t{self.__sessional}\t\t{self.__mid+self.__final+self.__sessional}'