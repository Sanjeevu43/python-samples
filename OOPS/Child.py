#from Parent import ParentC
import Parent
class Child(Parent.ParentC):
    def __init__(self) -> None:
        print('Child class constructor')
    
c = Child()
c._p2()