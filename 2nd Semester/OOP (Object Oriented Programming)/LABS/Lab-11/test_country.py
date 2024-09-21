from province import *
from country import *
from city import *
def main():
    file = open("cities.csv","rb")
    pakistan = Country('Pakistan')
    f = file.read()
    lines=f.decode("utf-8").split('\n')
    for line in lines:
        if line=='':    break
        s = line.split(',')
        pakistan.add_city(s[1], City(s[0], int(s[2]), int(s[3]), int(s[4]), int(s[5])))
    file.close()
    print (pakistan)
    pakistan.print_city_count_province_wise()
    print(pakistan.get_cities_with_2017_population('Punjab'))

main()
