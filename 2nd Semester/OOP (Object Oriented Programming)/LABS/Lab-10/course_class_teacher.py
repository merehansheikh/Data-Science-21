import student_subject_record as st
from course import *
from teacher import *

class Course_Class_Teacher:
    def __init__(self, code, title, fname, sname, students_count):
        self.__course = Course(code, title)
        self.__teacher = Teacher(fname, sname)
        self.__students = [st.Student_Subject_Record() for i in range(students_count)]

    def __str__(self):
        s = f'{self.__course}\n{self.__teacher}\nR_No\t\tMid\t\tFinal\t\tSess\t\tTotal\n'
        for student in self.__students:
            s += str(student) + '\n'
        return s

    def get_pass_students(self):
        s = f'R_No\t\tMid\t\tFinal\t\tSess\t\tTotal\n'
        for student in self.__students:
            if student.get_mid()+student.get_final()+student.get_sessional() >= 50:
                s += str(student) + '\n'
        return s

    def sort_students_descending(self):
        for i in range(len(self.__students)):
            for j in range(len(self.__students)-1):
                if self.__students[j].get_mid()+self.__students[j].get_final()+self.__students[j].get_sessional() < self.__students[j+1].get_mid()+self.__students[j+1].get_final()+self.__students[j+1].get_sessional():
                    self.__students[j], self.__students[j+1] = self.__students[j+1], self.__students[j]


def main():
    my_class = Course_Class_Teacher('CC-211','Operating Systems','Ahsan','Butt',10)
    print(my_class)
    print('-------------------------')
    print(my_class.get_pass_students())
    print('-------------------------')
    my_class.sort_students_descending()
    print(my_class)

main()
