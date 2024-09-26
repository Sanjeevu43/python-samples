import pandas as pd

#6: Creating Dataframe from list of dicts
# Pandas DataFrame can be created by passing lists of dictionaries as a input data. By default dictionary keys will be taken as columns.

# Initialize data to lists.
data = [{'a': 1, 'b': 2, 'c': 3},
        {'a': 10, 'b': 20, 'c': 30}]
  
# Creates DataFrame.
df = pd.DataFrame(data)
print(df)
print(df.shape)

# 7 Another example to create pandas DataFrame by passing lists of dictionaries and row indexes.
# Initialize data of lists
data = [{'b': 2, 'c': 3}, {'a': 10, 'b': 20, 'c': 30}]
  
# Creates pandas DataFrame by passing
# Lists of dictionaries and row index.
df = pd.DataFrame(data, index=['first', 'second'])
print(df)

# 8 Another example to create pandas DataFrame from lists of dictionaries with both row index as well as column index.
# Initialize lists data.
data = [{'a': 1, 'b': 2},
        {'a': 5, 'b': 10, 'c': 20}]
  
# With two column indices, values same
# as dictionary keys
df1 = pd.DataFrame(data, index=['first',
                                'second'],
                   columns=['a', 'b'])
  
# With two column indices with
# one index with other name
df2 = pd.DataFrame(data, index=['first',
                                'second'],
                   columns=['a', 'b1'])
  
# print for first data frame
print(df1, "\n")
  
# Print for second DataFrame.
print(df2)