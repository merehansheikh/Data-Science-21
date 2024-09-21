def main():
    x = [23,43,21,23,43,22,12,23,21]
    for i in range(len(x)):
        if x[i] != -1:
            count = 0
            value_check = x[i]
            for j in range(len(x)):
                if x[i] == x[j] :
                    count += 1
                    x[j] = -1
            print(f'{value_check} is repeated {count} time in the list')

main()