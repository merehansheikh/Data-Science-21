def main():

	f = open("8peek.py", "r")
	d = f.peek(1)  # not working in python but available in many langauges
	print(f.tell())  # it still return 0
	f.close()
	
	print("[")
	print(d)  # the first character of the file
	print("]")
	return 0

main()