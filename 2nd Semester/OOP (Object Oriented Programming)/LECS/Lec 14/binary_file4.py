import random as r
import struct

count = 10

def write_binary(elements):
    x = [struct.pack('i', element) for element in elements]
    file = open("numbers.bin","wb+")
    size = struct.pack('i', len(x))
    file.write(size)
    for element in x:
        file.write(element)
    file.close()

def read_binary():
    file = open("numbers.bin","rb+")
    size = struct.unpack('i',file.read(4))[0]
    x = file.read(4*size)
    y = [struct.unpack('i', x[i:i+4])[0] for i in range(0, len(x), 4)]
    print(y)
    file.close()
    return y[r.randint(0,len(y)-1)]

#reading data into list
#finding location of element to be deleted
#open file for writing+reading using r+
#using seek move to location where element exists
#overwrite elements from list into file to overwrite the file
def delete_binary(element):
    file = open("numbers.bin","rb+")
    size = struct.unpack('i',file.read(4))[0]
    x = file.read(4*size)
    y = [struct.unpack('i', x[i:i+4])[0] for i in range(0, len(x), 4)]
    file.close()
    for i in range(len(y)):
        if y[i]==element:
            break
    file = open("numbers.bin","rb+")
    file.write(struct.pack('i', size-1))
    file.seek(i*4, 1)
    x = [struct.pack('i', element) for element in y[i+1:len(y)]]
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
