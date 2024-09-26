l = [['Mr A','Mr B','Mr C'],[1,2,3],(4,5,5)]
empNames,IDs,deptCode = l
print(empNames)
print(IDs)
print(deptCode)

my_list = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 40, 'city': 'Chicago'}
]

print(my_list)
my_list = [{**ll, 'city':''} for ll in my_list]
print(my_list)

# for ll in my_list:
#     ll['city'] = ''
# print(my_list)