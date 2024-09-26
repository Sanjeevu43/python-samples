
class A:
    __name = None # this variable can be accessed with in class
    print('A class variable ',__name)
    def __f1(self): # this function can be accessed with in class
        print('A function!')


class B(A):
    'This is B class function !'
    def f2(self):
        obj_a = A()
        # if not obj_a.__name:
        #     print('Name : ', obj_a.__name)
        #obj_a.__f1() # not accesseble
        print('B function!')
    
    def __str__(self) -> str:
        print("str function !")
        return "Done"

obj_b = B()
print('Doc string : ',obj_b.__doc__)
print(obj_b)
obj_b.f2()

