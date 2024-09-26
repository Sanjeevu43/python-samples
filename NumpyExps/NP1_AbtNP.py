import numpy as np


'''
NumPy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools
for working with these arrays. It is the fundamental package for scientific computing with Python. 
It is open-source software. It contains various features including these important ones:
1. A powerful N-dimensional array object
2. Sophisticated (broadcasting) functions
3. Tools for integrating C/C++ and Fortran code
4. Useful linear algebra, Fourier transform, and random number capabilities

Arrays in NumPy: NumPy's  main object is the homogeneous multidimensional array.
It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.
In NumPy dimensions are called axes. The number of axes is rank.
NumPy's array class is called ndarray. It is also known by the alias array.
'''

arr = np.array([
               [[1,2,3,1],
               [4,5,6,1]],

               [[7,8,9,1],
               [10,11,12,1]]
               ])
# Printing type of arr object
print("Array is of type: ", type(arr)) 
# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim) 
# Printing shape of array
print("Shape of array: ", arr.shape) 
# Printing size (total number of elements) of array
print("Size of array: ", arr.size) 
# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)
print(np.zeros)
print(np.ones)
print('Max : ',np.argmax(arr,axis=-1))
print("Shape of first element: ", arr.shape[0]) 

l = [1,2,3,4]
l = np.array(l)
print('*** : ',l[:-1])
print(l.shape)
l1 = l.reshape(2,2)
print(l1.shape)

arr1 = np.array([[0.08769687, 0.9123031 ],
                [0.8103393 , 0.18966071],
                [0.74483985, 0.25516018],
                [0.6372295 , 0.3627704 ],
                [0.945463  , 0.05453704]])

print('Max On Row: ',np.argmax(arr1,axis=-1)) # gives index of max value on row base
print(arr1.shape) # gives index of max value on row base
print(arr1.sum(axis=0))
print(np.mean(arr1,axis=-1))

_arr = np.array([1,2,3,4])
print('_arr shape: ',_arr.shape)
print('_arr dimension: ',_arr.ndim)

print('Cumulative : ',_arr.cumsum())