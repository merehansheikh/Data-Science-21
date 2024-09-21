class Teacher:
    def __init__(self, fname, sname):
        self.__fname = fname
        self.__sname = sname

    def __str__(self):
        return f'Teacher: {self.__fname} {self.__sname}'