import numpy as np

'''
Basic operations: Plethora of built-in arithmetic functions are provided in NumPy.
1 Operations on single array: 
  We can use overloaded arithmetic operators to do element-wise operation on array to create a new array. 
  In case of +=, -=, *= operators, the existing array is modified.
'''
# basic operations on single array

a = np.array([1, 2, 5, 3]) 
# add 1 to every element
print ("Adding 1 to every element:", a+1) 
# subtract 3 from each element
print ("Subtracting 3 from each element:", a-3) 
# multiply each element by 10
print ("Multiplying each element by 10:", a*10) 
# square each element
print ("Squaring each element:", a**2) 
# modify existing array
a *= 2
print ("Doubled each element of original array:", a) 
# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 
print ("\nOriginal array:\n", a)
print ("Transpose of array:\n", a.T)

# 2 Unary operators: Many unary operations are provided as a method of ndarray class. 
# This includes sum, min, max, etc. These functions can also be applied row-wise or column-wise by setting an axis parameter.

arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])
  
# Axes are defined for arrays with more than one dimension.
# 2-dimensional array has two corresponding axes: the first running vertically downwards across rows (axis 0), 
# and the second running horizontally across columns (axis 1).
# axis=0 means columns, axis=1 means rows
# maximum element of array
print ("Largest element is:", arr.max())
print ("Row-wise maximum elements:", arr.max(axis = 1)) 
# minimum element of array
print ("Column-wise minimum elements:", arr.min(axis = 0)) 
# sum of array elements
print ("Sum of all array elements:", arr.sum()) 
# cumulative sum along each row
print ("Cumulative sum along each row:\n", arr.cumsum(axis = 1))

# 3 Binary operators: These operations apply on array elementwise and a new array is created. 
# You can use all basic arithmetic operators like +, -, /, , etc. In case of +=, -=, = operators, the existing array is modified.

a = np.array([[1, 2],
            [3, 4]])
b = np.array([[4, 3],
            [2, 1]])
 
# add arrays
print ("Array sum:\n", a + b) 
# multiply arrays (elementwise multiplication)
print ("Array multiplication:\n", a*b) 
# matrix multiplication
print ("Matrix multiplication:\n", a.dot(b))

# finding Cumulative sum for list
l = [1,2,3,4]
cumlist = []
j=0

for i in range(len(l)):
    j+=l[i]
    cumlist.append(j)

print('Cumlist : ',cumlist)

x = np.arange(0, 9) # [0 1 2 3 4 5 6 7 8]
print(x)
print(type(x))
print(x.shape)
newx = np.array([x])
print(newx)
print(type(newx))
print(newx.shape)
print(newx.ndim)
print(newx.size)
A = np.array([x, np.ones(9)]) # np.ones(9) = [1. 1. 1. 1. 1. 1. 1. 1. 1.]
print(A)