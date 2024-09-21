import random as r

def init_list_random(x):
    for i in range(20):
        x.append(r.randint(10, 99))

def average_of_list(list):
    sum = 0
    for num in list:
        sum += num
    average = sum / len(list)
    return average
    
def smaller_than_average(list, average):
    count = 0
    for num in list:
        if num < average:
            count += 1
    return count

def main():
    x =[]
    init_list_random(x)
    print(x)
    avg = average_of_list(x)
    print(avg)
    print(smaller_than_average(x, avg))

main()