from module1 import *

class D:
    print("D class")
    #C()

def m1():
    print('m1() called')
    D()


if __name__ == '__main__':
    print('Inside main')
    m1()



