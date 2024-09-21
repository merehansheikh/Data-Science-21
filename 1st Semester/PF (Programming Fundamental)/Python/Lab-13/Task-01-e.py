    #Problems in implementing sub task-c is:
    #In this task we have to compare user's data with the name presenented in result_data.txt.
    #Hence, we do not know the exact length of name.
from re import L


def main():
    fR = open('comma_seperated.txt','r')
    fW = open('result_report.txt','w')
    fR.readline()
    total_data = 27
    col = 6
    header = ['Subject','Sessional','Midterm','Final','Total','Grade']
    arr = [['Data' for i in range(col)]for i in range(total_data)] 
    arr = fillArr_and_splitting(arr,total_data,fR)
    arr = remove_quotation(arr,total_data)
    print(arr)
    presentable_form(arr,fW,header)
    
    
def fillArr_and_splitting(arr,td,file):
    for i in range(td):
        s = file.readline()
        c = 0 
        arr = split(s,arr,i,c)
    return arr    

def split(s,arr,r,arr_index):
    newStr = ""  
    for ch in range(len(s)):

        if s[ch] != ',' and s[ch] != '\n' and (ch != len(s)-1 and r != 28):
            newStr = newStr + s[ch]
            if ch == len(s)-2:
                newStr += s[ch + 1]
        else:
            arr_index = fillArray(arr,r,arr_index,newStr)
            newStr = ""
    return arr
    
def fillArray(arr,r,c,s):
    arr[r][c] = s
    c += 1
    return c

def remove_quotation(arr,n):
    for i in range(n):  
       arr[i][1] = arr[i][1][1:-1]
    return arr            
                
def presentable_form(arr,fW,header):
    count = 1
    temp = 1
    for i in range(len(arr)):
        arr_data = arr[i]
        for q in range(len(arr_data)):
            sum = int(arr[i][3]) + int(arr[i][4]) + int(arr[i][5])
            result = grades(sum)
        fW.write('{0}.{1:>11}{2:>20}\n'.format(str(count),arr[i][0],arr[i][1]))#Name and Roll Number
        fW.write('{0}{1:>11}{2:>9}{3:>8}{4:>7}{5:>7}\n'.format(header[0],header[1],header[2],header[3],header[4],header[5]))#Header 
        temp += 1
        count += 1
        temp += 1    
        fW.write('{0}{1:>15}{2:>9}{3:>8}{4:>7}  {5}\n'.format(arr[i][2],arr[i][3],arr[i][4],arr[i][5],sum,result))
        if temp == 4:
            temp = 1
        
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