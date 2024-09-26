from abc import ABC, abstractmethod

class AbstractClass(ABC):

    @abstractmethod
    def abstarct(self) -> None:
        print("This abstract method")

   
    def non_abstarct(self) -> None:
        print("This is non abstract method")



obj = AbstractClass()
obj.non_abstarct()