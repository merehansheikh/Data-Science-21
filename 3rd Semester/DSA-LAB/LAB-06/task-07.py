from random import *
from QUEUE import *

def ticks(t):
    p = t//5
    if t-(p*5)==0:
        return p
    else:
        return p+1

if __name__=="__main__":

    q =Queue()
    task =1
    tic =0
    job =0

    for i in range(100):
        n =randint(10,100)
        if n%5 == 0 or n%13 == 0 or n%67 == 0:
            pages =n % 61
            q.enqueue(pages)
            job +=1
            print(f"Tick:{i+1} Task {job} of Pages {pages} recieved for printing")
            
            if tic==0 and q.is_empty()==False:
                tic =ticks(q.peek())
                tic -=1
                print(f"Tick: {i+1} Task{task} starts beginning")
                
                if tic==0:
                    print(f"Tick:{i+1} Task{task} completed]")
                    q.dequeue()
                    task +=1
                    
            elif tic!=0:
                tic-=1
                if tic==0:
                    print(f"Tick:{i+1} Task{task} completedl")
                    task +=1
                    q.dequeue()

        else:
            if tic==0 and q.is_empty()==False:
                tic =ticks(q.peek())
                tic -=1
                print(f"Tick: {i+1} Task{task} starts beginning")
                if tic==0:
                    print(f"Tick:{i+1} Task{task} completed]")
                    q.dequeue()
                    task +=1

            elif tic!=0:
                tic-=1
                if tic==0:

                    print(f"Tick:{i+1} Task{task} completedl")
                    task +=1
                    q.dequeue()