import random

def main():
    list = []
    count = 0
    for i in range(20):
        list.append(random.randint(1,9))
    for i in range(len(list)):
        if list[i] != 0:
            count = 1
            for j in range(i+1, len(list)):
                if list[i] == list[j]:
                    count += 1
                    list[j] = 0
            print(f'{list[i]} exists {count} times in the list')

main()