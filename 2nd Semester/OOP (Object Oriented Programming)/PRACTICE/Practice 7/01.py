def main():
    list = [2,43,21,45,32,34,46,766,87,5,4]
    for i in range(1,len(list)-1,1):
        if list[i] > list[i-1] and list[i] > list[i+1]:
            print(f'{list[i]} is greater than {list[i-1]} and {list[i+1]}')
main()