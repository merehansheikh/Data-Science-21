from random import randint
def progWiseAvg(q):
    pwsum = [0]*4
    for prog in range(4):
        for sem in range(8):
            for sub in range(6):
                for stud in range(50):
                    pwsum[prog] += q[prog][sem][sub][stud]
    print("Program Wise Average")
    for prog in range(4):
        print("Program", prog, round(pwsum[prog]/8/6/50, 3))

def semWiseAvg(w):
    semWsum = [0] * 8
    for sem in range (8):
        for prog in range(4):
            for sub in range(6):
                for stud in range(50):
                    semWsum[sem] += w[prog][sem][sub][stud]
    print("Semester Wise Average")
    for sem in range(8):
        print("Semester", sem, round(semWsum[sem]/4/6/50, 3))

def SemWiseAvg4Prog(m, prog):
    pro_sem_avg = [0] * 8
    for sem in range (8):
            for sub in range(6):
                for stud in range(50):
                    pro_sem_avg[sem] += m[prog][sem][sub][stud]
    print("Semester Wise Average of Program", prog, "is")
    for sem in range(8):
        print("Semester", sem, round(pro_sem_avg[sem]/6/50, 3))

def result_std(arr, prog, stud):
    semWsum = [0] * 8
    for sem in range (8):
            for sub in range(6):
                    semWsum[sem] += arr[prog][sem][sub][stud]
    print("Semester Wise Average in the", prog, "program of student", stud)
    for sem in range(8):
        print("Semester", sem, round(semWsum[sem]/6, 3))
def main():
    data = [[[[randint(10,99) for l in range(50)] for k in range(6)] for j in range(8)] for i in range(4)]
    progWiseAvg(data)
    print()
    semWiseAvg(data)
    print()
    print("Enter the program you want to check the semester wise average")
    program = int(input())
    SemWiseAvg4Prog(data, program)
    print()
    print("Enter the program and student of a semester to calculate the result of the student")
    prog_st = int(input("Enter the program: "))
    stu = int(input("Enter the student: "))
    result_std(data, prog_st, stu)
main()