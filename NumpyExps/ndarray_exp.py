import numpy as np

array = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print(array.ndim)
print(array.shape)
print(type(array))

if isinstance(array, np.ndarray):
    print('Correct')