def main():
    file = open('Practice 12.txt', 'r')
    # new_file = 
    r = file.read()
    count = 0
    for letter in r:
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
