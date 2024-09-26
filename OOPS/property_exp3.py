
class Person:
    """
    This is property function
    """
    def __init__(self,name) -> str:
        self._name = name
    
    @property
    def name(self):
        print('Getting Name')
        return self._name
    
    @name.setter  # here @name should match function name of @property i.e line no 10 
    def name(self,name):
        print('Setting Name to : ',name)
        self._name = name

    @name.deleter
    def name(self):
        print('Deleting Name')
        del self._name
   
    #n = property(gName,sName,dName)
    #print('n type ', type(n))

y = Person('Sanjeevu')
print(y.name)
y.name = 'Sany'
print(y.name)
del y.name
#print(y.name)
    
