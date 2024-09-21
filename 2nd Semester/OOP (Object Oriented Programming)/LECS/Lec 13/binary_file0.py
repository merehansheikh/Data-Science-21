import struct

def pack_unpack(num):
    x = struct.pack('i', num)
    print(f'Binary string:{x}')                    #print binary string of 32 bits/ 4 bytes
    print(f'Binary string length is:{len(x)} bytes')      #print length of binary string
    y = struct.unpack('i', x)   #return tuple having single element
    print(f'Result of unpack: {y} tuple')        #print tuple
    print(f'First element of tuple is: {y[0]}')     #print first element of the tuple

def main():
	pack_unpack(-2147483648),     print('----------------------------------------')
	pack_unpack(2147483647),     print('----------------------------------------')
	#We have use the minimum element and maximum element of 32 bit size; whereas if you uncomment
    #the next line, there will be a run-time error that element is greater than size of maximum integer
    #pack_unpack(2147483650),     print('----------------------------------------')

main()
