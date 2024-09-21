def is_leap(year): 
    if (year % 400 == 0) and (year % 100 == 0):
        return True

    elif (year % 4 ==0) and (year % 100 != 0):
        return True

    else:
        return False

def main():


    year = int(input("Enter a year you want to check: "))

    if is_leap(year):
        print('In {0} February has 29 days' .format(year))

    else:
        print('In {0} February has 28 days' .format(year))


main()
