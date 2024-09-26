import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])
            
print('Shape : ',arr.shape)
print('Dimension: ',arr.ndim)
print('Shape of arr: ',arr.shape[0])


newarr = arr.reshape(2,2,3)
print("Reshape : \n",newarr)
print('Shape : ',newarr.shape)
print('Dimension: ',newarr.ndim)

again_reshape_arr = np.reshape(newarr,(-1,newarr.shape[-1]))
print("Again_Reshape : \n",again_reshape_arr)
print('Again_Reshape : ',again_reshape_arr.shape)
print( 'Again_Reshape Dimension: ',again_reshape_arr.ndim)

newarr1 = arr.flatten()
print("Flatten : \n",newarr1)
print('Shape : ',newarr1.shape)
print('Dimension: ',newarr1.ndim)

_arr  = np.array([ [[10,20,30],
                    [40,50,60]],
                      
                    [[70,80,90],
                     [100,110,120]] ])

print("_arr :",_arr.ndim)
print('_arr shape : ',_arr.shape)
print('_arr shape f -1 : ',_arr.shape[-1])

