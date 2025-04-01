import pandas as pd
import numpy as np

ser = pd.Series()
print('Data Type : ',type(ser))

l = [1,2,3,4]

ser = pd.Series(l)
print(ser)

cus_index = [2,3,4,5,6]

ser_new = pd.Series(ser, index=cus_index)
print(ser_new)
print(ser_new[ser_new > 3])
ser_new[ser_new.isnull()] = 0
print(ser_new)
print(None == None)
print(np.nan == np.nan)
print(str == str)
