import random as r
import struct
import os

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

#deleting element by using temporary file
def delete_binary(element):
    file1 = open("numbers.bin","rb+")
    file2 = open("temp.bin","wb+")
    while True:
        s = file1.read(4)
        if s == b'':
            break                   #this is end of file, so break the loop
        x = struct.unpack('i', s)[0]
        if x != element:
            file2.write(s)
    file1.close()
    file2.close()
    os.remove('numbers.bin')
    os.rename('temp.bin', 'numbers.bin')

def main():
    x = [r.randint(-2147483648, 2147483647) for i in range(count)]
    write_binary(x)
    element = read_binary()
    print(f'Element selection for deletion: {element}')
    delete_binary(element)     #modify element at position 4
    read_binary()

main()
