def main():
    file_r = open('practice8.txt', 'r')
    f_w = open('newtext.txt', 'w')
    r = file_r.read()
    w = ''
    for i in r:
        w += i
    f_w.write(w)
    file_r.close()
    f_w.close()
main()