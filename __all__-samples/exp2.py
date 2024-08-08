
from exp1 import *
from exp1 import f3 # without this import, line no 10 won't execute

print(name)
#print(age) NameError: name 'age' is not defined, because age variable not added in __all__ list

print(f1())
print(f2())
print(f3()) #NameError: name 'f3' is not defined, because f3 function not added in __all__ list
p = __Person()