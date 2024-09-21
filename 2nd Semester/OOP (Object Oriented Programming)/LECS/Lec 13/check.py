import struct

def main():
    binary_file = open('newfile.bin', 'wb+')
    file = open('newfile.txt', 'w+')

    l = [1, 2, 3, 4]

    binary = [struct.pack('i', elements) for elements in l]
    for elements in binary:
        binary_file.write(elements)

    for elements in l:
        file.write(str(elements))
        file.write(' ')
    
    
    file.close()
    binary_file.close()
# opening the file and reading it
    file_b = open('newfile.bin', 'rb')

    br = file_b.read()
    from_binary = [struct.unpack('i', br[i:i+4])[0] for i in range(0, len(br), 4)]
    print(from_binary)

    file = open('newfile.txt', 'rb')
    rl = file.read()
    words = rl.split()
    sum = 0
    for num in words:
        sum += int(num)
    print(sum)
    print(words)
main()