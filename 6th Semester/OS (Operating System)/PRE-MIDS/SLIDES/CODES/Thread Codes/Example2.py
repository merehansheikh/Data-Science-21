import threading
import time
from sys import *

def f1():
    for i in range(1000):
        print('X', end =' ')     

def f2():
    for i in range(1000):
        print('O', end =' ')     

tid1 = threading.Thread(target=f1)
tid2 = threading.Thread(target=f2)
    
# Start threads
tid1.start()
tid2.start()

# Wait for threads to complete
tid1.join()
tid2.join()
print('End of main thread')
