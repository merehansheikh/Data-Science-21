import random as r
import struct

count = 10
#Handling double values
def write_binary(elements):
    x = [struct.pack('d', element) for element in elements]
    file = open("floats.bin","wb+")
    for element in x:
        file.write(element)
    file.close()
#Handling double values
def read_binary():
    file = open("floats.bin","rb+")
    x = file.read()
    y = [struct.unpack('d', x[i:i+8])[0] for i in range(0, len(x), 8)] #using 8 for double value
    print(y)
    file.close()

def main():
    x = [r.random() for i in range(count)]
    print (x)
    write_binary(x)
    read_binary()

main()
