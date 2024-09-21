import struct

def write():
	f=open("binfile.bin","wb+")
	num=[204800, -2147483648, 15, 20, 25]	
	x = [struct.pack('i', element) for element in num]
	for element in x:
		f.write(element)    #writing in file
	f.close()

def read():
	f=open("binfile.bin","rb")
	x=f.read()              #reading from file
	y = [struct.unpack('i', x[i:i+4])[0] for i in range(0, len(x), 4)]	
	print(y)	
	f.close()

def main():
	write()
	read()

main()
