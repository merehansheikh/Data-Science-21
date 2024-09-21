import struct
import random

def pack_unpack():
    num=[2147483647, -2147483648, 15, -200, 525]	
    x = [struct.pack('i', element) for element in num]
    #[0] is used to get first element of the tuple, because I want to make list of numbers not tuples
    #as discussed in the previous program that unpack function returns value in tuple
    y = [random.randint(1,10)[0] for i in range(len(x))]
    print(y)

def main():
	pack_unpack()

main()
