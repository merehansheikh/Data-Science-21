from ArrayQueue import *

def add_in_queue(dic):
    queue = ArrayQueue()
    tuple = dic.items()
    # for key,value in dic:
        # queue.insert((key,value))
    for i in tuple:
        print(i[1],i[0])
        queue.insert((i))
    # print(queue.peek())
    print()
    return queue

def file():
    # print("sdgfs")
    # with open("readylist.txt") as f:
    with open("/home/faizan/Documents/university/university/Third semester/Data Structures and Algorithms/FINALS/lab 9/ready.txt") as f:
        # print("sdgfs")
        dic = {}
        try:
            s = ""
            while True:
                string = ""
                # print("sdgfs")
                line = f.readline()
                # print("sdgfs")
                # print(line[0])
                # print("sdgfs")
                if line[0] == " ":
                    break
                for i in range(len(line)):
                    # print(line[i])
                    s += line[i]
                    if line[i] == " ":
                        a = line[i+1]
                        a += line[i+2]
                        dic[int(a)] = string
                    string += line[i]
                        # s += line[i]
                        # print(line[i])
                        # print("sdgfs")
                    """else:
                        s += line[i]
                        s += line[i+1]
                        s += line[i+2]
                        s += "\n"
                        break"""
        except:
            # print("cghser")
            pass
        # print(s)
        # print(dic)
        mykeys = list(dic.keys())
        mykeys.sort()
        mykeys.reverse()
        new_dic = {i:dic[i] for i in mykeys}
        # print(new_dic)
        return new_dic

class Simulator:
    time = 0
    def __init__(self,queue) -> None:
        self.queue = queue
        self.arrival_time = 0
        self.execution_time = 0
        self.execution_end_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0 
        self.execution()
        
    def execution(self):
        lenth = self.queue.size()
        # print(lenth)
        for i in range(lenth):
            if Simulator.time == 36:
                values = input()
                with open("/home/faizan/Documents/university/university/Third semester/Data Structures and Algorithms/FINALS/lab 9/ready.txt","w") as f:
                    f.write(values)
                    dic = file()
                    add_in_queue(dic)
            item = self.queue.remove()  
            # print(item)
            self.execution_end_time += item[0]
            self.waiting_time = self.execution_time -self.arrival_time
            self.turnaround_time = self.execution_end_time -self.arrival_time
            print(f"{item[1]} {item[0]} {self.waiting_time} {self.turnaround_time}")
            Simulator.time += item[0]
            self.execution_time += item[0]
if __name__ == "__main__":
    dic = file()
    queue = add_in_queue(dic)
    Simulator(queue)