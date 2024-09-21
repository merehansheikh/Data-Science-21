def check_bit():
    x = int(input("Enter any number:"))
    bit_no = int(input("Enter bit no to check:"))
    if (x & (2 ** (bit_no -1 )))==0:
        print (f'In {x} bit {bit_no} is off')
    else:
        print (f'In {x} bit {bit_no} is on')
check_bit()