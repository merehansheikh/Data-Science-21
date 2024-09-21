class CollegeCourse:
    def __init__(self, dep, course_no, ch_hrs, tuition):
        self.dep = dep
        self.course_no = course_no
        self.ch_hrs = ch_hrs
        self.tuition = tuition
    
    def __str__(self):
        return f'The department is {self.dep}, course number is {self.course_no}. It has {self.ch_hrs}Hrs and with the tuition fee of {self.tuition}'

class LabCourse(CollegeCourse):
    def __init__(self, dep, course_no, ch_hrs, tuition, tuition_fee):
        super().__init__(dep, course_no, ch_hrs, tuition)
        self.tuition_fee = tuition_fee
    def __str__(self):
        return f'{super().__str__()} with tuition fee of {self.tuition_fee}Pkr.'
def main():
    o1 = LabCourse('DS', 'DS#69', 3, 'HEHE', 69000)
    print(o1)
main()
