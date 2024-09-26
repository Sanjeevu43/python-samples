from typing import final

#@final
class A:
    def m1(self):
        print('A class m1 function')

class B(A):
    def m1(self):
        print('B class m1 function')

b = A()
b.m1()

b1 = B()
b1.m1()