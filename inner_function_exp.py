import ast
import numpy as np

l = "{'yes','no','maybe'}"
print(type(l))
print(l)

temp_list = ast.literal_eval(l)
print(type(temp_list))
print(temp_list)
print('no' in temp_list)
print('yes' in temp_list)

