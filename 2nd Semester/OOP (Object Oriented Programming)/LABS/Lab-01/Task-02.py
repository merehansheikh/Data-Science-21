import random


def print_table(num):
    print(f'Table no. {num}')
    for i in range(1,10):
        print(f'{num}\t*\t{i}\t=\t{(num*i)}')

def main():
    table = random.randint(5,9)
    print_table(table)
main()