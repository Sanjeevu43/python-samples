class ParentC:
    _x = ""
    
    def __init__(self) -> None:
        print('Parent constructor')
        if not self._x:
            print('X is None')
        else:
            print('X is not None')

    
    def p1():
        print('Parent p1 method...!')
    
    def _p2(self):
        print('Parent p2 method...!')
    

p = ParentC()
#ParentC.p1() # p1 is called on class
#p._p2()

i = 0
if (i):
    print(f"I is {i}")

