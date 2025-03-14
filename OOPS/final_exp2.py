class FinalClass:
    def __init_subclass__(cls):
        super.__init_subclass__
        print('Called this constructor')
        raise TypeError("Cannot subclass FinalClass")
  
    # def __init__(self):
    #     print('Called this constructor')
    # def m1(self):
    #     print('Final class m1() method called')

# obj = FinalClass()
# obj.m1()    
class MySubClass(FinalClass):
    pass