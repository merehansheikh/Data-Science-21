def main():
    l1 = [1,2,3,4,5,6,7,8]
    l2 = [2,4,6]
    l3 = [1,3,5,7]

    count1 = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                count1 += 1
    
    count2 = 0
    for i in range(len(l1)):
        for j in range(len(l3)):
            if l1[i] == l3[j]:
                count2 += 1
    
    print(max(count1, count2))
    
main()