from QUEUE import *

if __name__ == '__main__':
    
    # checling the queue class
    lq = LinkedQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    
    print(f'Checking if the queue is empty: {lq.is_empty()} \n')
    print(f'Checking the size of the queue: {lq.size()} \n')
    
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print()
    # after dequeueing all the elements, the queue should be empty
    print(f'Checking if the queue is empty: {lq.is_empty()} \n')