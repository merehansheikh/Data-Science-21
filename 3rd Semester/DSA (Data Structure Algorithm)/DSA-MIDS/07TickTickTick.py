from random import randint
from Queue_LinkedNode import *

def time_of_prnter_processing():
    waiting_que = Linked_Queue()
    tick = 1
    printing_time = []
    task = []
    t = 0

    for _ in range(15):
        x = randint(10, 99)
        if x % 5 == 0 or x % 13 == 0 or x % 67 == 0:
            pages = x % 61
            waiting_que.enqueue(pages)
            task.append(len(task) + 1)

            print (f"At tick {tick}, {task[-1]} of {waiting_que.rear.data} pages received for printing.")

            if len(printing_time) == 0:
                printing_time.append(tick + limit(waiting_que.rear.data)) 
            else:
                printing_time.append(printing_time[-1] + limit(waiting_que.rear.data))
            
        if len(printing_time) and tick == printing_time[0]:
            print (f"At tick {tick}, {task[t]} completed.")

            printing_time.pop(0)
            waiting_que.dequeue()

            t += 1
        
        tick += 1

    for _ in range(len(printing_time)):
        print (f"At tick {printing_time[0]}, {task[t]} completed.")

        printing_time.pop(0)
        waiting_que.dequeue()
        t += 1

def limit(pages):
    time = pages // 5
    if pages % 5 != 0:
        time += 1
    return time

if __name__ == "__main__":

    time_of_prnter_processing()
    print ()
    print (f"************THE END************")