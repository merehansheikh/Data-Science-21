def main():
    f = open('result_data.txt','r+')
    skipLines(2,f)
    roll = input('Enter Roll Number: ')
    name = input('Enter Name: ')
    
    pointer = findData(f,roll) 
    name = fillName(name) #To overwrite name completely
    updateName(name,f,pointer)  
    f.close() 
          
        
def skipLines(n,file):
    for i in range(n):
        file.readline()

def fillName(name):    
    if len(name) < 32:
        for i in range(len(name),32):
            name = name + ' '
    return name

def findData(f,roll):
    for i in range(9):
        pointer = f.tell()
        data = f.read(10)
        if data == roll:
            f.seek(pointer)
            return f.tell()
        skipLines(3,f)        
             
def updateName(name,f,pointer):
    
    for i in range(0,3):
        f.seek(pointer + (i * 59))
        f.read(10)
        f.seek(f.tell())
        f.write(name)
main()