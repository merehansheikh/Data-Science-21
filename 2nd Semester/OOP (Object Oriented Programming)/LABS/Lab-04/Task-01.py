import random

def main():
    list = []
    for i in range(20):
        list.append(random.randint(1,9))
    count_list = [0]* 9
    for num in list:
        count_list[num-1] += 1
    
    for i in range(9):
        if count_list[i] != 0:
            print(f'{i+1} exists {count_list[i]} times in the list')
main()