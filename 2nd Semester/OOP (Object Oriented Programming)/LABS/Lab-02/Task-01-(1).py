import random


def zero():
    print('zero')


def counting_9(num):
    if num in range(1, 10):
        if num == 1:
            return "one"
        if num == 2:
            return 'two'
        if num == 3:
            return 'three'
        if num == 4:
            return 'four'
        if num == 5:
            return 'five'
        if num == 6:
            return 'six'
        if num == 7:
            return 'seven'
        if num == 8:
            return 'eight'
        if num == 9:
            return 'nine'


def teens(num):
    if num == 1:
        return 'eleven'
    if num == 2:
        return 'twelve'
    if num == 3:
        return 'thirteen'


def tens(num):
    if num == 10:
        return 'ten'
    if num == 20:
        return 'twenty'
    if num == 30:
        return 'thirty'
    if num == 40:
        return 'forty'
    if num == 50:
        return 'fifty'
    if num == 60:
        return 'sixty'
    if num == 70:
        return 'seventy'
    if num == 80:
        return 'eighty'
    if num == 90:
        return 'ninty'


def main():
    x = random.randint(0, 100)
    print(x)
    first_digit = x // 10
    second_digit = x % 10
    print("First Digit:", first_digit)
    print("Second Digit:", second_digit)

    if first_digit == 0:  # for 1-9 range
        if second_digit == 0:
            zero()
        digit = counting_9(second_digit)

    if first_digit == 1:  # for 11-19
        if x in range(11, 14):
            digit = teens(second_digit)
        if x >= 14 and x <= 19:
            digit = counting_9(second_digit)
            digit += 'teen'

    if second_digit == 0:
        digit = tens(x)
        
    if (x in range(21, 30) or x in range(31, 40)  # for 21-99 excluding the tens
        or x in range(41, 50) or x in range(51, 60)
        or x in range(61, 70) or x in range(71, 80)
        or x in range(81, 90) or x in range(91, 100)):
        for_now = second_digit
        num = x - for_now
        digit = tens(num)
        digit += " "
        digit += counting_9(second_digit)

    print(digit)


main()
