class Person:
    pName = 'Sanjeevu'; 

    def __init__(self,name):
        self.pName = name;
        print('Welcome ', self.pName)  

    def m1():
        print('Welcome ',Person.pName)   
    
    def m2(self,name):
        #self.pName=name;
        print('Welcome ',name)
Person.m1();

p1 = Person('Sany');
p1.m2('San')

    




    