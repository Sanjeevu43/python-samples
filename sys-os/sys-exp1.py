#The python sys module provides functions and variables which are used to manipulate different parts of the 
#Python Runtime Environment. It lets us access system-specific parameters and functions.

import sys

for path in sys.path:
    None
    #print(path)

#value = sys.argv[0]  # or sys.argv # default argument is current file name
value = sys.argv[1] # we need to pass argument value from command line
print('You Entered :',value)
print(type(value))
print('Python version :', sys.version)
#print(sys.path)
print('This will not execute')
data = sys.stdin.readline()
print('You have entered −> ', data)

