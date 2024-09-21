def main():
    l1 = [23, 32, 11]
    l2 = [51, 12, 63, 26]
    count = 0

    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] > l2[j]:
                count += 1
        print(f'{l1[i]} {count}')
        count =0
main()
