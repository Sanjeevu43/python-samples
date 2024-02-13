from typing import final

# final method cannot be overriden
class BaseClass:
    @final
    def m1(self) -> None:
        print('Base Class final m1() method, cannot be overriden')
    
    def m2(self) -> None:
        print('Base Class m2() method, can override')

class ChildClass(BaseClass):
    # def m1(self) -> None:
    #     print('Child Class m1() method')

    def m2(self) -> None:
        print('Child Class m2() method')

obj1: BaseClass = BaseClass()
obj1.m1()
obj1.m2()

obj2: BaseClass = ChildClass()
obj2.m2()

@final
class BaseClass2:
    pass

# final class cannot be subclassed
# class ChildClass2(BaseClass2):
#     pass
    
    
