
class Person:
    """
    This is property function
    """
    def __init__(self,name) -> str:
        self._name = name
    
    def gName(self):
        print('Getting Name')
        return self._name
    
    def sName(self,name):
        print('Setting Name to : ',name)
        self._name = name

    def dName(self):
        print('Deleting Name')
        del self._name
   
    n = property(gName,sName,dName)

    print('n type ', type(n))
    


y = Person('Sanjeevu')
print(y.__doc__)
print(y.n)
y.n = 'Sany'
print(y.n)
del y.n
#print(y.name)
    
