from Array_Queue import *

def read_file(f):
    
    file = open(f, 'r')
    
    t = file.read()
    
    t = t.split('\n')
    t = [i.split(' ') for i in t]
    
    file.close()
    
    # with open('file.txt', 'w') as file:
    #     pass

    return t

def convert_2D_2nd_to_int(arr):
    temp = []
    for i in range(len(arr)):
        strr = arr[i][0]
        intt = int(arr[i][1])
        t = list((strr, intt))
        temp.append(t)
        
    return temp
        
class Simulator:
    time = 0
    total_time = 0
    def __init__(self, q):
        self.q = q
        self.exe_st_time = 0  
        self.exe_end_time = 0  
        self.exe_wt_time = 0
        self.exe_turn_arround_time = 0
        
    def execute(self):
        for i in range(self.q.size):
            temp = self.q.dequeue()
            self.exe_st_time = temp[1]
            self.exe_end_time = temp[1]
            print(temp[0], temp[1])
            Simulator.time += 1
            Simulator.total_time += temp[1]
            
    def waiting_time(self):
        return self.exe_st_time - Simulator.time
    
    def turnaround_time(self):
        return self.exe_end_time - Simulator.time

    # def 

  


class Data:
    
    def __init__(self, file, execution_time, waiting_time, turnaround_time):
        self.file = file
        self.execution_time = execution_time
        self.waiting_time = waiting_time
        self.turnaround_time = turnaround_time
    # sms.exe, <Execution Time>, <Waiting Time>, <Turnaround Time>  
    def __str__(self):
        s = self.file +'<' + str(self.execution_time)+ '>' + '<' + str(self.waiting_time) + '>'+ '<' + str(self.turnaround_time) + '>'
        return s
        

if __name__ == '__main__':
    a = Array_Queue()
    f = 'readylistcopy.txt'
    temp = read_file(f)
    content1 = convert_2D_2nd_to_int(temp)
    
    
    for ele in content1:
        a.enqueue(ele)
        
        
    print(a.reverse_sort_2D_array())
    # for i in a:
    #     print(i)
    