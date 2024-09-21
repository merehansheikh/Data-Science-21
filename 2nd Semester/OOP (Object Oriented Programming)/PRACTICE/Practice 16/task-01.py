class Instructor:
    def __init__(self, f_name, l_name, office_no):
        self.f_name = f_name
        self.l_name = l_name
        self.office_no = office_no
    
    def __str__(self):
        return f'{self.f_name} {self.l_name} has a office number {self.office_no}' 

class Classroom:
    def __init__(self, building_no, room_no):
        self.building_no = building_no
        self.room_no =  room_no

    def __str__(self):
        return f'Building {self.building_no} room {self.room_no}'

class CollegeCourse:
    def __init__(self, f_name, l_name, office_no, classs, credit_hours):
        # composition
        self.inst = Instructor(f_name, l_name, office_no)
        self.classroom = classs
        self.credit_hours = credit_hours

    def __str__(self):
        return f'{self.inst} has a class in {self.classroom} and has {self.credit_hours} credit hours course'
    
def main():
    classs = Classroom(1, 3)
    oop = CollegeCourse('Abdul', 'Mateen', 23, classs, 3)
    print(oop)
main()

