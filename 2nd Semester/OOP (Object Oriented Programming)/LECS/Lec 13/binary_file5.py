import time
import struct
import random as r

COUNT = 100

def write_binary():
	fb=open("numbers.bin","wb+")
	num=[r.randint(-2147483648,2147483647) for i in range(COUNT)]	
	print(f'Element at index 60: {num[60]}')
	x = [struct.pack('i', element) for element in num]
	for element in x:
		fb.write(element)
	fb.close()

def read_binary():
	fb=open("numbers.bin","rb")
    #skip first 240 bytes from start of the file
	fb.seek(60*4,0)
    #read one element after 60 elements
	xb=fb.read(4)
	y = struct.unpack('i', xb)
	print(f'Element read from 60th byte in the file: {y[0]}')
	fb.close()
	
def main():
	write_binary()
	read_binary()
	
main()
