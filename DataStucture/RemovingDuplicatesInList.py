# Using for loop and list comrehension
l = [1,2,3,1,3,4] # 1 and 3 dups
new_l = []
for item in l:
    if item not in new_l:
        new_l.append(item)

print(new_l)
l = [1,2,3,1,2,4,5,6,3] # 1,2 and 3 dups
new_l = []
[new_l.append(item) for item in l if item not in new_l]
print(new_l)

# Using set
l = ['San','Bin','Lucky','Bittu','Lucky']
new_l = list(set(l))
print(new_l)
s = {'San','Bin','Lucky','Bittu','Lucky'}
print(s)