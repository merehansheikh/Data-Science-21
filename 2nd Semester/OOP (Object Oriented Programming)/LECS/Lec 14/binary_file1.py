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

#Modifying element by overwriting some element at given position
def modify_binary(element, position):
    file = open("numbers.bin","rb+")
    file.seek(position * 4)
    file.write(struct.pack('i', element))
    file.close()

def main():
    x = [r.randint(-2147483648, 2147483647) for i in range(count)]
    write_binary(x)
    read_binary()
    modify_binary(100000,4)     #modify element at position 4
    read_binary()

main()
