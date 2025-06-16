from typing import *

names: list = ['San','Dan','John']
print(type(names))

names1: List = "('San','Dan','John')"
print(type(names1))

def m1(name: str, age: int, roles: Tuple[str,str,str]) -> list:
    print('Type : ',type(roles))
    print(roles)

roles = ['Lead Engg','People Manager','Mentor']
m1('San',40,roles)

x = tuple[1,2,3]
print('Type : ',type(x))


# operator overload
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b      
   
   def __pow__(self,other):
      print('POW operator overloaded')     
      return Vector(self.a ** other.a, self.b ** other.b)
   
   def __add__(self,other):
      print('Add operator overloaded')     
      return Vector(self.a+other.a, self.b+other.b)
   
   def __str__(self):
      print('Str operator overloaded')     
      #return 'Vector (%d, %d)' % (self.a, self.b)
      return f'Vector ({self.a}, {self.b})'
      #return 'Vector ({0}, {1})'.format(self.a, self.b)

v1 = Vector(2,10)
print(v1)
v2 = Vector(3,2)

print(v1**v2)
print(v1+v2)


