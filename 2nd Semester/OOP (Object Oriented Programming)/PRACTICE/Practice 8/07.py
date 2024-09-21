def main():
    file_r = open('practice8.txt', 'r')
    f_w = open('replaced.txt', 'w')
    r = file_r.read()
    w = ''
    for letters in r:
        if ord(letters) >= ord('0') and ord(letters) <=ord('9'):
            w += '-' 
        else:
            w += letters
    f_w.write(w)
    file_r.close()
    f_w.close()
main()