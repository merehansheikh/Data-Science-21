import random as r

def init_list_random(x):
    for i in range(20):
        x.append(r.randint(10, 99))
def main():

    # x=[]
    # init_list_random(x)
    # print(x)

    x= [4,3,2,5]
    count = 0
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            count += 1
    print (count)
main()