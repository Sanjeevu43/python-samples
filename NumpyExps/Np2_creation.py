# Python program to demonstrate
# array creation techniques
import numpy as np
 
# Creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)
 
# Creating array from tuple
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)
print ("\nArray created using passed tuple:\n", b.ndim)
print ("\nArray created using passed tuple:\n", b.shape)
 
# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)
 
# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s."
            "Array type is complex:\n", d)
 
# Create an array with random values
e = np.random.random((2, 2))
print ("\nA random array:\n", e)
 
# Create a sequence of integers
# from 0 to 30 with steps of 5
f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)

# Create a sequence of 10 values in range 0 to 5
g = np.linspace(0, 5, 10)
print ("\nA sequential array with 10 values between"
                                        "0 and 5:\n", g)
 
# Reshaping 3X4 array to 2X2X3 array
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])
 
newarr = arr.reshape(2, 2, 3)
 
print ("\nOriginal array:\n", arr)
print ("\nOriginal array dimension:\n", arr.ndim)
print ("Reshaped array:\n", newarr)
print ("Reshaped array dimnesion:\n", newarr.ndim)
 
# Flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()
 
print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)

rand_arr = np.random.randint(1,15,2)
print('random number from 1 to 15 \n ',rand_arr)

arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
print('Count : ',np.bincount(arr))

arr_ones = np.ones([3,3])
print('arr_ones :', arr_ones)

arr_nd = np.arange(16).reshape(4,4)
print('arr_nd :', arr_nd)
#make above array ones
arr_nd_ones = np.ones_like(arr_nd)
print('arr_nd_ones :', arr_nd_ones)
print('arr_nd :', arr_nd)

arr_nd1 = np.arange(36).reshape(3,4,3)
print('arr_nd1 :', arr_nd1)
print('&&&&&&&&&&&&&&&&&&&&*************************&&&&&&&&&&&&&&&&&&&&&')

np.set_printoptions(threshold=None)
large_array = np.arange(12100).reshape(110,110)
print(large_array)