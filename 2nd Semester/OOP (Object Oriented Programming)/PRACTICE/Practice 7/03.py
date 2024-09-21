def main():
    l1 = [2, 3, 4]
    l2 = [5, 6]
    for i in range(len(l1)):
        for j in range(len(l2)):
            print(f'({l1[i]}, {l2[j]})')
main()