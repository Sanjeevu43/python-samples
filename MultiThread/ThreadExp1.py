'''
In Python we can create thread in 3 ways
1) without class
2) By extending Thread class
3) Without extending Thread class
'''
#1 Creating a thread without class
from threading import *
import multiprocessing

def d1():
    print(f'Processing d1')
    for i in range(3):
        print("Child Thread : ", current_thread().name)

def d2():
    print(f'Processing d2')
    for i in range(3):
        print("Child Thread : ", current_thread().name)

t1 = Thread(target=d1)
t2 = Thread(target=d2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Done")
print("Main Thread : ", current_thread().name)