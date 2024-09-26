
# Merge dicts
d1 = {'name':'Sany','age':40}
d2 = {'dept':'admin','sal':40000}
d2 = {**d2, **d1} # old technique to merge
print(d1)
print(d2)
print('*******************************************************************8')
d3 = {'name':'Jhony','age':45}
d4 = {'dept':'Payroll','sal':30000}

#d4 = d4|d3 # new merge from 3.9
d4 |= d3 # new update from 3.9 
print(d3)
print(d4)