# 1) Merging using ** (Dictionary Unpacking):
# {**d2, **d1}: A new dictionary is constructed using the unpacked key-value pairs.

# 2) Merging using the |= Operator (In-Place Update):
#    |=: This operator is equivalent to d4 = d4 | d3, where the | is the "union" operator that merges 
#   dictionaries. The |= updates d4 directly, rather than creating a new dictionary.

# In-Place vs. New Dictionary:

# ** unpacking creates a new dictionary. The original dictionaries remain unchanged 
# (unless you explicitly reassign one of them to the new dictionary, as was done with d2).

# |= performs an in-place update. It modifies the dictionary on the left-hand 
# side (in this case, d4) directly. If you need to keep the original d4 intact, 
# you should use d4 = d4 | d3 (which creates a new dictionary) or make a copy of d4 first.

# 1) {**d1, **d2} (Older Technique): Unpacks the dictionaries and creates a new dictionary containing the 
# merged key-value pairs.

# 2) d1 |= d2 (Python 3.9+): Updates d1 in-place with the key-value pairs from d2.

# Performance: For large dictionaries, the in-place update (|=) can be slightly more efficient because it 
# avoids creating a completely new dictionary.


# Merge dicts
d1 = {'name':'Sany','age':40,'dept':'Admin'}
d2 = {'dept':'Payroll','sal':40000}
d2 = {**d2, **d1} # old technique to merge
print(d1)
print(d2)
print('*******************************************************************8')
d3 = {'name':'Jhony','age':45,'dept':'Admin'}
d4 = {'dept':'Payroll','sal':30000}

#d4 = d4|d3 # new merge from 3.9, this will also work
d4 |= d3 # new update from 3.9 
print(d3)
print(d4)