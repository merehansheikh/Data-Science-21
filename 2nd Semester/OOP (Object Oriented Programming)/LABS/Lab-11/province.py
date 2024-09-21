import city

class Province:
    def __init__(self, province_name):
        self.__province_name = province_name
        self.__city_count = 0
        self.__cities = []

    def add_city(self, city):
        self.__city_count += 1
        self.__cities.append(city)

    def __str__(self):
        s = f'***** {self.__province_name} {self.__city_count} cities **********\n----------------------------------------------------------\n'
        for city in self.__cities:
            s += str(city) + '\n'
        return s

    def get_count(self):
        return self.__city_count

    def get_cities_with_2017_population(self):
        s = f'* {self.__province_name} {self.__city_count} cities *\n----------------------------------------\n'
        for city in self.__cities:
            s += city.get_city_name() + '\t' + str(city.get_population_2017()) + '\n'
        return s