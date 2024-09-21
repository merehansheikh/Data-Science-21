def main():
    fR = open('result_data.txt','r')
    print('Total Students are 9')
    skipLines(2,fR)
    
    std_no = int(input('Enter Student Number: '))
    pointer = 59 * (std_no - 1)
    fR.seek(fR.tell()*std_no+(pointer))
    print()
    presentable_form(fR,std_no)
    fR.close()

def skipLines(n,file):
    for i in range(n):
        file.readline()  
         
def presentable_form(fR,std_no):
    count = 1
    sum = 0
    for i in range(3):
        roll_num = fR.read(10)
        name = fR.read(32)
        subject = fR.read(7)
        md = fR.read(2)
        fR.read(1)
        ss = fR.read(2)
        fR.read(1)
        fn = fR.read(2)
        total = int(md) + int(ss) + int(fn)
        sum = sum + total
        result = grades(total)
        if std_no == 9 and i == 3:#Last student Number, then avoid \n character
            fR.read()   
        else:    
            fR.read(1)     
        if count == 1:    
            print('{}{:>33s}'.format(roll_num,name)) 
            print('{}{:>7s}{:>7s}'.format('Course','Total','Grade')) 
            count = 2
        print('{}{:>6s}    {}'.format(subject,str(total),result)) 
     
    print('{:=>20s}'.format('='))
    sum = sum / 3
    result = grades(sum)     
    print('{}{:>10.2f}{:>6s}'.format('OPM',sum,result)) 
         
def grades(n):
    if n >= 85:
        return 'A'
    if n >= 80:
        return 'A-'
    if n >= 75:
        return 'B'
    if n >= 70:
        return 'B+'
    if n >= 65:
        return 'B-'
    if n >= 61:
        return 'C+'
    if n >= 58:
        return 'C'
    if n >= 55:
        return 'C-'
    if n >= 50:
        return 'D'
    if n >= 0:
        return 'F'
    
main()            