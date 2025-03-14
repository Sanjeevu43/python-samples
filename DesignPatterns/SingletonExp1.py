
class SingleTon:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def m1():
        print('m1() called') 


obj1 = SingleTon()
print(id(obj1))
obj2 = SingleTon()
print(id(obj2))