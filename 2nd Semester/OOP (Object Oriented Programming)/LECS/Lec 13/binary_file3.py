import struct
import random as r

def write():
	fb=open("binfile.bin","wb+")
	fa=open("binfile.txt","w+")
	num=[r.randint(-2147483648,2147483647) for i in range(1000)]	
	x = [struct.pack('i', element) for element in num]
	for element in x:
		fb.write(element)
	for element in num:
		fa.write(str(element))
		fa.write(' ')
	fa.close()
	fb.close()

def read():
	fb=open("binfile.bin","rb")
	fa=open("binfile.txt","rb")
	xb=fb.read()
	y = [struct.unpack('i', xb[i:i+4])[0] for i in range(0, len(xb), 4)]
	sum = 0	
	for element in y:
		sum += element
	print (f'Sum of elements read from binary file: {sum}')
	fb.close()

	sum = 0
	xa=fa.read()
	words = xa.split()
	for word in words:
		sum += int(word)
	print (f'Sum of elements read from ascii file:  {sum}'),     fa.close()

def main():
	write()
	read()

main()
