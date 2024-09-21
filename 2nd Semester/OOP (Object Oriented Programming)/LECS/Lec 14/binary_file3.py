import random as r
import struct

count = 10

def write_binary(elements):
    x = [struct.pack('i', element) for element in elements]
    file = open("numbers.bin","wb+")
    for element in x:
        file.write(element)
    file.close()

def read_binary():
    file = open("numbers.bin","rb+")
    x = file.read()
    y = [struct.unpack('i', x[i:i+4])[0] for i in range(0, len(x), 4)]
    print(y)
    file.close()
    return y[r.randint(0,len(y)-1)]
#reading value into list
#value removed from list, if exists
#write modified list into fresh file
def delete_binary(element):
    file = open("numbers.bin","rb+")
    x = file.read()
    y = [struct.unpack('i', x[i:i+4])[0] for i in range(0, len(x), 4)]
    file.close()
    for i in range(len(y)):
        if y[i]==element:
            break
    y.pop(i)        #remove element from list
    x = [struct.pack('i', element) for element in y]
    file = open("numbers.bin","wb+")
    for element in x:
        file.write(element)
    file.close()

def main():
    x = [r.randint(-2147483648, 2147483647) for i in range(count)]
    write_binary(x)
    element = read_binary()
    print(f'Element selection for deletion: {element}')
    delete_binary(element)     #modify element at position 4
    read_binary()

main()
