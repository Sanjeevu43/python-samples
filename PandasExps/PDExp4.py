from turtle import pd
import pandas as pd

#6: Creating DataFrame using zip() function.
# Two lists can be merged by using list(zip()) function. Now, create the pandas DataFrame by calling pd.DataFrame() function.

# List1
Name = ['tom', 'krish', 'nick', 'juli']  
# List2
Age = [25, 30, 26, 22]  
# get the list of tuples from two lists. # and merge them by using zip().
list_of_tuples = list(zip(Name, Age)) 
  
# Converting lists of tuples into # pandas Dataframe.
df = pd.DataFrame(list_of_tuples,
                  columns=['Name', 'Age'])
print(df)

#7:  Creating dataframe from series
# To create a dataframe from series, we must pass series as argument to DataFrame() function.

# Initialize data to series.
d =  pd.Series([10, 20, 30, 40])
# creates Dataframe.
df = pd.DataFrame(d)
print(df)

#8: Creating DataFrame from Dictionary of series.
# To create DataFrame from Dict of series, dictionary can be passed to form a DataFrame. The resultant index is the union of all
#  the series of passed indexed.

# Initialize data to Dicts of series.
d = {'one': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd']),
     'two': pd.Series([50, 60, 70, 80],
                      index=['e', 'f', 'g', 'h'])}
  
# creates Dataframe.
df = pd.DataFrame(d)
print(df)