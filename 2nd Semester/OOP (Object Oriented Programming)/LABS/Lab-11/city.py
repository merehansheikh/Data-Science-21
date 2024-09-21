class City:
    def __init__(self, city_name, pop_1972, pop_1981, pop_1998, pop_2017):
       self.__city_name = city_name
       self.__pop_1972 = pop_1972
       self.__pop_1981 = pop_1981
       self.__pop_1998 = pop_1998
       self.__pop_2017 = pop_2017

    def __str__(self):
        return f'{self.__city_name}\t{self.__pop_1972}\t{self.__pop_1981}\t{self.__pop_1998}\t{self.__pop_2017}'

    def get_population_2017(self):
       return self.__pop_2017


    def get_population_1998(self):
       return self.__pop_1998


    def get_population_1981(self):
       return self.__pop_1981


    def get_population_1972(self):
       return self.__pop_1972

    def get_city_name(self):
        return self.__city_name