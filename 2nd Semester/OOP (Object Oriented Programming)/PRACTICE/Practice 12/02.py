def main():
    file = open('Practice 12.txt', 'r')
    # new_file = 
    r = file.read()
    count = 0
    check_count = 0
    for letter in r:

        if count == 0:
            if letter != '\n':
                print(letter,end='')
                check_count += 1
            if letter == '\n':
                while check_count <= 15:
                    print(' ',end='')
                    check_count += 1
                check_count = 0
                print('\t', end='')
                count += 1
        elif count == 1:
            if letter != '\n':
                print(letter,end='')
                check_count += 1
            if letter == '\n':
                while check_count <= 15:
                    print(' ',end='')
                    check_count += 1
                check_count = 0
                print('\t', end='')
                count += 1
        else:
            if letter != '\n':
                print(letter,end='')
            if letter == '\n':
                print('\t', end='')
                count += 1

        if count == 13:
            print('\n')
            count = 0

    file.close()
    
main()