import threading

class Cls():
    def f1(self):
        print('Hello')

obj1 = Cls()
t1=threading.Thread(target=obj1.f1())
t1.start()
t1.join()
