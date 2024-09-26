'''
Pandas DataFrame is a 2-dimensional labeled data structure like any table with rows and columns. 
The size and values of the dataframe are mutable,i.e., can be modified. It is the most commonly used pandas object. 
Pandas DataFrame can be created in multiple ways. Let’s discuss different ways to create a DataFrame one by one.

DataFrame() function is used to create a dataframe in Pandas. The syntax of creating dataframe is:
pandas.DataFrame(data, index, columns)
where,
data: It is a dataset from which dataframe is to be created. It can be list, dictionary, scalar value, series, ndarrays, etc.
index: It is optional, by default the index of the dataframe starts from 0 and ends at the last data value(n-1). It defines the row label explicitly.
columns: This parameter is used to provide column names in the dataframe. If the column name is not defined by default, it will take a value from 0 to n-1.

'''

import pandas as pd
import numpy as np

list = [[1,2,3],[4,5,6],[7,8,9]]
print('List Size : ',len(list[0]))

pd_data = pd.DataFrame(data=list,columns=['I','J','K'],index=['A','B','C'])
print(pd_data.shape)
print(pd_data)
print('Desc : ', pd_data.describe())

I = np.array(pd_data['I'])
print(I)
print(np.mean(I))
print(np.std(I))
print((1-4.0)/np.std(I))

# 1. Creating Empty DataFrame and Storing it in variable df
df1 = pd.DataFrame()
print(df1)

# 2. Creating  Dataframe from Lists
data = [1,2,3,4]
df2 = pd.DataFrame(data)
print(df2)

# 3 . Creating Pandas DataFrame from lists of lists.
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]  
# Create the pandas DataFrame
df3 = pd.DataFrame(data, columns=['Name', 'Age'])
print(df3)

# 4
'''
Method #3: Creating DataFrame from dict of narray/lists
To create DataFrame from dict of narray/list, all the narray must be of same length. 
If index is passed then the length index should be equal to the length of arrays. 
If no index is passed, then by default, index will be range(n) where n is the array length.
'''
# initialize data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}
  
# Create DataFrame
df4 = pd.DataFrame(data)
print(df4)

# 5: Creating a DataFrame by proving index label explicitly.
# initialize data of lists.
data = {'Name': ['Tom', 'Jack', 'nick', 'juli'],
        'marks': [99, 98, 95, 90]}
  
# Creates pandas DataFrame.
df5 = pd.DataFrame(data, index=['rank1',
                               'rank2',
                               'rank3',
                               'rank4'])
print(df5)  

print('======================= ********* ================')
print('df5 Shape : ', df5.shape)

x,y = df5.shape

print('x :',x)
print('y :',y)
count = len(df5.index)
print('Size:', count)
