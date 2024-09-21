import random

def counting(num):
    if num == 0:
        return ('Zero')
    elif num == 1:
        return ('One')
    elif num == 2:
        return ('Two')
    elif num == 3:
        return ('Three')
    elif num == 4:
        return ('Four')
    elif num == 5:
        return ('Five')
    elif num == 6:
        return ('Six')
    elif num == 7:
        return ('Seven')
    elif num == 8:
        return ('Eight')
    elif num == 9:
        return ('Nine')
    elif num == 10:
        return ('Ten')

def teens(num):
    if num == 11:
        return ("Eleven")
    elif num == 12:
        return ("Twelve")
    elif num == 13:
        return ("Thirteen")
    elif num == 14:
        return ("Fourteen")
    elif num == 15:
        return ("Fifteen")
    else:
        return ("teen")

def tens(num):
    if num == 2:
        return ("Twenty")
    elif num == 3:
        return ('Thirty')
    elif num == 4:
        return ('Forty')
    elif num == 5:
        return ('Fifty')
    elif num == 6:
        return ('Sixty')
    elif num == 7:
        return ('Seventy')
    elif num == 8:
        return ('Eighty')
    elif num == 9:
        return ('Ninety')

def main():
    num = random.randint(0,99)
    print(num, end='\t')
    if num >= 0 and num <= 10:
        print(counting(num))
    elif num > 10 and num < 16:
        print(teens(num))
    elif num >16 and num <= 19:
        print(f'{counting(num%10)} {teens(num//10)}')
    elif num > 19:
        if num % 10 == 0:
            print(f'{tens(num//10)}')
        else:
            print(f'{tens(num//10)} {counting(num%10)}')

main()