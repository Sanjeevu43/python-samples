class access_m1:
    __age = 20
    __name = 'My X'
    id
    def __init__(self,age) -> None:
        self.__age = age
        self.__name = 'Mr Y'
        self.id = 101
    
    def m11(self):
        self.__m1()

    def __m1(self):
        print('Age :', self.__age )
        print('Name :',self.__name)

obj = access_m1(40)
if __name__ == "__main__":
    obj.m11()
    def m1():
        print('m1() called')
        obj1 = access_m1(40)
        print('ID: ',obj1.id)
        #print(obj1.__age)
    m1()

# def m1():
#     print('m1() called')
#     obj1 = access_m1(40)
#     print('ID: ',obj1.id)
#     #print(obj1.__age)
# m1()




