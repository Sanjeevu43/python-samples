class myclass(object):
    def __init__(self) -> None:
        self.name = "San"
        self.age = 40
    
    def __str__(self) -> str:
        print("Hello")
        return "Name : {} Age: {}".format(self.name,self.age)
    
obj1 = myclass()
print(obj1)