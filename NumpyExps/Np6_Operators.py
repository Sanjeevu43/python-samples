import numpy as np

arr = np.arange(0,50,2, float).reshape(5,5)
print(arr)
print('SUM : ',arr.sum())
print('AVG : ',arr.mean())
print('MIN : ',arr.min())
print('MAX : ',arr.max())
print('SUM COLUMN WISE:', arr.sum(axis=0)) #column
print('SUM ROW WISE:', arr.sum(axis=1)) #row

print('MIN ROW WISE:', arr.min(axis=1)) #row
print('MIN COL WISE:', arr.min(axis=0)) #column
