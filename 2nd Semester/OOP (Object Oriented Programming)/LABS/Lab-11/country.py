from province import *
from city import *

class Country:
    def __init__(self, country_name):
        self.__country_name = country_name
        self.__cities_count = 0
        self.__provinces = dict()
        self.__provinces['Punjab'] = Province('Punjab')
        self.__provinces['Sindh'] = Province('Sindh')
        self.__provinces['Balochistan'] = Province('Balochistan')
        self.__provinces['KPK'] = Province('KPK')

    def add_city(self, province, city):
        self.__provinces[province].add_city(city)
        self.__cities_count += 1

    def __str__(self):
        s = f'<<<<<<< {self.__country_name} {self.__cities_count} cities >>>>>>>>>>\n---------------------------------------------------\n'
        keys = self.__provinces.keys()
        for key in keys:
            s += str(self.__provinces[key]) + '\n'
        return s

    def print_city_count_province_wise(self):
        keys = self.__provinces.keys()
        for key in keys:
            print (f'Count in {key} is {self.__provinces[key].get_count()}')

    def get_cities_with_2017_population(self, province):
        s = f'<<<<<<< {self.__country_name} >>>>>>>>>>\n-----------------------------------------------\n'
        s += self.__provinces[province].get_cities_with_2017_population() + '\n'
        return s