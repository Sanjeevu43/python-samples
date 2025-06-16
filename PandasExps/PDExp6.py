
import pandas as pd
import numpy as np

list = [[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],
        [1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],
        [10,20,30],[40,50,60],[70,80,90],[100,200,300],[400,500,600],[700,800,900]]
print('List Size : ',len(list[0]))

#pd_data = pd.DataFrame(data=list,columns=['I','J','K'],index=['A','B','C'])
pd_data = pd.DataFrame(data=list)
print(pd_data.shape)
#print(pd_data)
#print('Desc : ', pd_data.describe())
print(pd_data.head())
print(pd_data.tail())
