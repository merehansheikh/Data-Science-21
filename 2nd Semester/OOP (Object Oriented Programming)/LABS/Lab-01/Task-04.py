import random
def print_sequence(a,b):

    for i in range(min(a,b), max(a,b)+1):
        print(i, end=" ")

def main():
    a  = random.randint(10,99)
    b = random.randint(10,99)

    print_sequence(a,b)

main()