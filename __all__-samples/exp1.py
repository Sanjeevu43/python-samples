# A list of strings that define what variables have to be imported to another file is known as __all__ in Python. 
# The variables which are declared in that list can only be used in another file after importing this file, 
# the rest variables if called will throw an NameError.

__all__ = ["f1","f2","name","__Person"]

name: str = "Sanjeev"
age: int = 30

def f1() -> None:
    print(f'exp1.f1() called')

def f2() -> None:
    print(f'exp1.f2() called')

def f3() -> None:
    print(f'exp1.f3() called')

# this function can't access from other py files
def __f4() -> None:
    print(f'exp1.__f4() called')

__f4()

# if we define class or function or variable with __ (double underscore) and included in __all__ list then we can access from other py files
# other wise can't access
class __Person():
    pass

p = __Person()