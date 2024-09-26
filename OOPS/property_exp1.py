'''
Python's property() is the Pythonic way to avoid formal getter and setter methods in your code. 
This function allows you to turn class attributes into properties or managed attributes. 
Since property() is a built-in function, you can use it without importing anything.

Syntax: property(fget, fset, fdel, doc)

Parameters: 

fget() - used to get the value of attribute
fset() - used to set the value of attribute
fdel() - used to delete the attribute value
doc() -  string that contains the documentation (docstring) for the attribute
Return: Returns a property attribute from the given getter, setter and deleter.

Note: 
If no arguments are given, property() method returns a base property attribute that doesn’t contain any getter, setter or deleter.
If doc isn’t provided, property() method takes the docstring of the getter function.
'''

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature
        #self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32   # here getter metod will called, bcoz you called self.temperature
        #return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)

    ''' property object temperature. Simply put, property attaches some code (get_temperature and set_temperature)
    to the member attribute accesses (temperature).

    Any code that retrieves the value of temperature will automatically call get_temperature()
    instead of a dictionary (__dict__) look-up. Similarly, any code that assigns a value to temperature
    will automatically call set_temperature(). This is one cool feature in Python.  '''

    
    
temp = Celsius(10)  # when you assign a value through constructor then setter metod will call 

#temp.temperature = 30 # when you assign a value directly then also setter metod will call 
#temp.temperature  # when you call variable which used property, then getter metod will call 

print(temp.get_temperature())

print(temp.to_fahrenheit())


