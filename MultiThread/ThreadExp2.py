import threading

#2) Creating thread By extending Thread class
class MyThread(threading.Thread):
    def run(self) -> None:
        for i in range(5):
            print("Child Thread : ", threading.current_thread().getName()) 
        
t1 = MyThread()
t1.start()
t1.join()

print("Control return to ", threading.current_thread().getName())