import threading
import time

count = 0
# Define a simple function for the thread to run
def inc():
    for i in range(1000000):
        global count
        count = count + 1
        #time.sleep(0.0000001) 

def dec():
    for i in range(1000000):
        global count
        count = count - 1
        #time.sleep(0.0000001) 
        
        
# Create two threads
thread1 = threading.Thread(target=inc)
thread2 = threading.Thread(target=dec)

# Start the threads
thread1.start()
thread2.start()

# thread1.join()
# thread2.join()

print(count)
