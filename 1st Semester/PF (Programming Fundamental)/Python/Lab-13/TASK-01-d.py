def main():
    f_RW = open('result_data.txt','r+')
    skipLines(2,f_RW)
    name = input('Enter Name: ')
    name = fillName(name) #To Match User name and Data Names(result_data.txt)
    Last_name = fillName('Usman Jan')#For the Last record
    pointer1 = findData(f_RW,name) 
    pointer2 = findData(f_RW,Last_name)#Pointer of Last Name
    if pointer1 == pointer2:#It is the Last Data then just remove it
        lastData_remove(pointer1,f_RW)
    remove_InsertData(pointer1,pointer2,f_RW)  
    f_RW.close()
          
        
def skipLines(n,file):
    for i in range(n):
        file.readline()

def fillName(name):    
    if len(name) < 32:
        for i in range(len(name),32):
            name = name + ' '
    return name

def findData(f,name):
    for i in range(9):
        pointer = f.tell()
        f.read(10)
        data = f.read(32)
        if data == name:
            f.seek(pointer)
            return f.tell()
        skipLines(3,f)  

def lastData_remove(pointer,f):
    f.truncate()
      
def remove_InsertData(p1,p2,f):
    f.seek(p2)
    data1 = f.read(57)
    f.read(1)
    data2 = f.read(57)
    f.read(1)
    data3 = f.read(57)

    lastData_remove(p2,f)
    
    f.seek(p1)
    f.write(data1+'\n'+data2+'\n'+data3+'\n')
main()