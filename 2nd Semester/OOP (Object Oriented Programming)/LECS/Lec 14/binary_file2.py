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
    return y[r.randint(0, len(y)-1)]

#modifying element, first we have to search element
#next move to start of the matched element
#Write to replace new element with existing elemetn
def modify_binary(element1, element2):
    file = open("numbers.bin","rb+")
    while True:
        element = struct.unpack('i', file.read(4))[0]
        if element == element1:
            #file.seek(file.tell()-4)   #move to required location from start
            file.seek(-4,1)             #move to required location from current
            file.write(struct.pack('i', element2))
            break
    file.close()

def main():
    x = [r.randint(-2147483648, 2147483647) for i in range(count)]
    write_binary(x)
    element=read_binary()
    modify_binary(element, 4000000)     #modify element at position 4
    read_binary()

main()
