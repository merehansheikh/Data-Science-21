def main():
    fR = open('result_data.txt','r')
    print('Total Students are 9')
    skipLines(3,fR)
    subject,result = average(fR)
    print(f'Average Result of {subject} is {result:.3f}.')
    fR.close()
    
def skipLines(n,file):
    for i in range(n):
        file.readline()  

def average(fR):
    sum = 0
    count = 0
    for i in range(9):
        fR.read(42)
        subject = fR.read(2)
        fR.read(5)
        md = fR.read(2)
        fR.read(1)
        ss = fR.read(2)
        fR.read(1)
        fn = fR.read(2)
        fR.read(1)
        sum = sum + int(md) + int(ss) + int(fn) 
        skipLines(2,fR)
    avrg = sum / 27
    return subject,avrg    
        
            
main()    