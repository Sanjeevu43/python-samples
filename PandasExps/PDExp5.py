import pandas as pd
import numpy as np
# Column names for the dataframe
columns = ["Brand", "Product"]
  
# Row data for the dataframe
data = [
    ("HP", "Laptop"),
    ("Lenovo", "Mouse"),
    ("Dell", "Keyboard"),
    ("Samsung", "Monitor"),
    ("MSI", "Graphics Card"),
    ("Asus", "Motherboard"),
    ("Gigabyte", "Motherboard"),
    ("Zebronics", "Cabinet"),
    ("Adata", "RAM"),
    ("Transcend", "SSD"),
    ("Kingston", "HDD"),
    ("Toshiba", "DVD Writer")
]
pd_data = pd.DataFrame(data,columns = ["Brand", "Product"])
#print(pd_data.shape)
#print(pd_data)

n_splits = 4
#print(pd_data.count())
#print(len(pd_data))
each_len = pd_data.count() // n_splits
#print(each_len)
copy_df = pd_data

no_of_threads = 5
chunks = []
records_per_chunk = len(pd_data) // no_of_threads
print("Records : ", records_per_chunk)

dataframes = []
start = 0
end = records_per_chunk
i = 2
for split in range(no_of_threads):
    print(start,end) 

    if(split+1 == no_of_threads and len(pd_data) > end):
        print("split=", split)
        print("OK")
        print("Len:",len(pd_data))
        print("Start:",end)
        temporary_df = pd_data.iloc[start:, :]
        dataframes.append(temporary_df)
    else:
        temporary_df = pd_data.iloc[start:end, :]
        dataframes.append(temporary_df)  
    
    start = end
    end = records_per_chunk*i    
    i+=1

dataframes1 =  np.array_split(pd_data, no_of_threads)
print("One : ",dataframes)
print("Two : ",dataframes1)


    