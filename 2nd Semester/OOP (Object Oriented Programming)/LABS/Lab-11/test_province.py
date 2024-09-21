from province import *
from city import *
def main():
    file = open("cities.csv","rb")
    punjab = Province('Punjab')
    f = file.read()
    lines=f.decode("utf-8").split('\n')
    for line in lines:
        if line=='':    break
        s = line.split(',')
        if s[1] == 'Punjab':
            punjab.add_city(City(s[0], int(s[2]), int(s[3]), int(s[4]), int(s[5])))
    file.close()
    print (punjab)
    print(punjab.get_cities_with_2017_population())

main()
