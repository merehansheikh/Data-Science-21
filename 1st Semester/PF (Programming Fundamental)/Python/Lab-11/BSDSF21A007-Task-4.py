from random import randint
def total_hos(arr):
    sum = 0
    year = 0
    while year < 4:
        coun = 0
        while coun < 6:
            cities = 0
            while cities < 4: 
                sum += arr[year][coun][cities]
                cities += 1
            coun += 1
        year += 1
    return sum

def hos_chn(arr, country):
    sum = 0
    year = 0
    while year < 4:
        cities = 0
        while cities < 4: 
            sum += arr[year][country][cities]
            cities += 1
        year += 1
    return sum

def max_hosp(arr):
    max_hosp = 0
    year = 0
    while year < 4:
        sum = 0
        coun = 0
        while coun < 6:
            cities = 0
            while cities < 4: 
                sum += arr[year][coun][cities]
                max = sum
                cities += 1
            coun += 1
        if max > max_hosp:
            max_hosp = max
            yr = year
        year += 1
    return yr
def year_hos(arr, year):
    sum = 0
    coun = 0
    while coun < 6:
        cities = 0
        while cities < 4: 
            sum += arr[year][coun][cities]
            cities += 1
        coun += 1
    return sum
def year_nam(y):
    year = ["2019", "2020", "2021", "2022"]
    return year[y]
def main():
    year = ["2019", "2020", "2021", "2022"]
    countires = ["USA", "UK", "UAE", "PAK", "IND", "China"]
    cities = [0, 1, 2, 3]
    no_hospital = [[[randint(1,15) for k in range(4)] for j in range(6)] for i in range(4)]

    # total no.  of hospitals build in all the countries in all 4 years
    print("The total no. of hopitals build in all the countries in 4 years are", total_hos(no_hospital))
    
    #no. of hospital build in china
    print("The total no. of hopitals build in China are", hos_chn(no_hospital, 5))
    
    #the year with the maximum no. of hospitals build 
    print("The year with the maximum no. of hospitals build is",year_nam((max_hosp(no_hospital))))
    
    #no. of hospitals build in 2020
    print("The no. of hospitals build in 2020 are", (year_hos(no_hospital, 1)))
    
main()