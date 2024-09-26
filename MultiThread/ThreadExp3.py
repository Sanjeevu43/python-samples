import threading

# 3) Creating thred Without extending Thread class

class MyThread:
    def m1(self):
        for i in range(3):
            print("Child Thread :", threading.current_thread().getName())

obj = MyThread()
#t1 = threading.Thread(obj.m1())
t1 = threading.Thread(target=MyThread().m1)
t1.start();
t1.join()
print("Done")
print("Control return to ",threading.current_thread().getName())