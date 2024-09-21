from random import *
class Node:
    def __init__(self, val):
        self.data =val
        self.link =None


class Queue:
    class Node:
        def __init__(self, val):
            self.data =val
            self.link =None
    def __init__(self):
        self.front =None
        self.rear =None

    def push(self, val):
        tmp =Node(val)
        if self.front==None:
            self.front =tmp
            self.rear =tmp
            return
        else:
            self.rear.link =tmp
            self.rear =tmp
            return
    
    def pop(self):
        if self.front==None:
            return
        else:
            tmp =self.front
            self.front =tmp.link
            return tmp.data
    def is_empty(self):
        if self.front==None:
            return True
        return False
    def peek(self):
        if self.front==None:
            return None
        else:
            return self.front.data

    def dis(self):
        cr =self.front
        while cr !=None:
            print(cr.data)
            cr =cr.link

def ticks(pone):
    
    p =pone//5
    if pone-(p*5)==0:
        return p
    else:
        return p+1

def main():

    q =Queue()
    task =1
    tic =0
    job =0


    for i in range(200):
   
        n =randint(10,50)
 
        if n%5==0 or n%13==0 or n%67==0:
     
    
            pages =n%61
            q.push(pages)
        
    

            job +=1
            
            print(f"Tick:{i+1} Task {job} of Pages {pages} recieved for printing")
   
            if tic==0 and q.is_empty()==False:
              
                tic =ticks(q.peek())

                tic -=1
        
                print(f"Tick: {i+1} Task{task} starts beginning")
                if tic==0:
                
                    print(f"Tick:{i+1} Task{task} completed]")
                    q.pop()

                    task +=1

            elif tic!=0:
                tic-=1
                if tic==0:

                    print(f"Tick:{i+1} Task{task} completedl")
                    task +=1
                    q.pop()

 
            
        else:
            if tic==0 and q.is_empty()==False:
                
         
                tic =ticks(q.peek())
    
                tic -=1
            
                print(f"Tick: {i+1} Task{task} starts beginning")
                if tic==0:
                
                    print(f"Tick:{i+1} Task{task} completed]")
                    q.pop()

                    task +=1

            elif tic!=0:
                tic-=1
                if tic==0:

                    print(f"Tick:{i+1} Task{task} completedl")
                    task +=1
                    q.pop()



       


 


main()
            