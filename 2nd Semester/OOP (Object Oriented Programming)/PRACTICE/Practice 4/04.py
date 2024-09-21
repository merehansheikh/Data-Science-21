def main():
    d =[37, 90, 42, 84, 79, 97, 34, 31, 10, 59, 83, 64, 21, 74, 15, 56, 19, 46, 25, 13]
    swap_index = int(input('Enter the index of the element you want to swap'))
    swap_with_index = int(input('Enter the index of the element you want to swap with'))
    loop = 50

    for i in range(loop):
        d[swap_index], d[swap_with_index] = d[swap_with_index], d[swap_index]

    print(d)

main()