from access_modifier1 import access_m1

def m2():
    #pass
    obj2 = access_m1(30)
    obj2.m11()

    #print('Age :', obj2.__age ) # __age and __name are private variables 
    #print('Name :',obj2.__name)

m2()