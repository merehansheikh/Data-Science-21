import threading
import time

def f1():
    for i in range(5):
        time.sleep(1)
        print('FCIT')
        

def f2():
    for i in range(5):
        time.sleep(1.5)
        print('ARIF')
        

tid1 = threading.Thread(target=f1)
tid2 = threading.Thread(target=f2)
    
# Start threads
tid1.start()
tid2.start()

# Wait for threads to complete
tid1.join()
tid2.join()

print("Main thread has finished")