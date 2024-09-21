def main():
    a = [1,3,5,7,9]
    b = [2,4,6,8,10]
    sorted_3 = []
    for i in range(len(a)):
        if a[i] < b[i]:
            sorted_3.append(a[i])
            sorted_3.append(b[i])
        elif a[i] > b[i]:
            sorted_3.append(b[i])
            sorted_3.append(a[i])
    print(sorted_3)
    
main()