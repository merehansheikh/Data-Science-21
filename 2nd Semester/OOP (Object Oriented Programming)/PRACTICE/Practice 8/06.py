def main():
    file_r = open('practice8.txt', 'r')
    f_w = open('compare.txt', 'w')
    r = file_r.read()
    w = ''
    for i in r:
        if i!= ' ':
            w += i
    f_w.write(w)
    file_r.close()
    f_w.close()


    file_r = open('practice8.txt', 'r')
    f_w = open('compare.txt', 'r')
    r = file_r.read()
    w = f_w.read()
    if len(r) > len(w):
        print(f'First file was bigger with {len(r)} letter in it')
    else:
        print(f'Second file was bigger with {len(w)} letter in it')

    file_r.close()
    f_w.close()
main()