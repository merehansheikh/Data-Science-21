import random as r


def main():
    # l = [[9, 9, 5, 9, 4],[4,7,3,7,5],[10,4,4,2,4],[5,2,10,1,9],[8,6,10,5,6]]
    l = [[r.randint(1,19) for x in range(5)]for x in range(5)]
    print(l)
    three_by_three = [[0]*3]*3
    tbt = [[] for i in range(3)]
    for i in range(len(l)-2):
        for j in range(len(l)-2):
            sum = l[i][j] + l[i][j+1] + l[i][j+2]
            sum += l[i+1][j] + l[i+1][j+1] + l[i+1][j+2]
            sum += l[i+2][j] + l[i+2][j+1] + l[i+2][j+2]
            tbt[i].append(sum//9)    
    print(tbt)
main()
