import random
def check_sum(a, b, sum):
    if sum == (a+b):
        print("Your answer is correct")
    else:
        print(f'Sorry, correct answer is {a+b}')

def main():
    a = random.randint(10,50)
    b = random.randint(10,50)

    print(f'A: {a}')
    print(f'B: {b}')

    sum = int(input(""))
    
    check_sum(a, b, sum)
main()
