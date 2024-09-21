import threading
import time

def f1():
    for i in range(5):
        print('FCIT')
        time.sleep(0.1)

def f2():
    for i in range(5):
        print('ARIF')
        time.sleep(0.1)

f1()
f2()
