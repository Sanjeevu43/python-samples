# slice : arr[:rows,:columns]

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print('*********************************************************')

print(arr[:0]) # no rows and columns 
print(arr[:1]) # return first row
print(arr[:2]) # return two rows

print(arr[:,:1]) # return first column
print(arr[:,:2]) # return two columns
print(arr[:1,:2]) # return from first row and two columns
print(arr[:1,:3]) # return from first row and three columns

l1 = [1,2,3]
l2 = [4,5,6]
print(l1+l2)

l1 = np.array([1,2,3])
l2 = np.array([4,5,6])
print(l1+l2)