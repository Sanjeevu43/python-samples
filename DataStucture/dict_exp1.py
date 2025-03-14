

# def test():
#     rule_info={}
#     condition_info={}
#     r_c = []
#     outer_index = 0
#     inner_index = 0
#     for i in range(2):
#         rule_info[outer_index]=[
#                 {"rule_name":"Student Rule"+str(i)},
#             ]
#         for j in range(2):
#             print("Innner for")
#             condition_info[inner_index]=[
#                     { "value":"Student "+str(j)+" OuterIndex "+str(i)},
#                 ]
#             inner_index+=1
#         outer_index+=1 
#     r_c.append(rule_info)
#     r_c.append(condition_info)
#     return r_c   
# rclist = test()
# rules = rclist[0].values()
# print(type(rules))
# conditions = rclist[1].values()

# for r in rules:
#     for ru in r:
#         print(ru['rule_name'])
#         for c in conditions:
#             for v in c:
#                 print(v['value'])

#     print('*****************')


d1 = {'A':'Apple','B':'Banana','C':'Cat'}
d1['D']='Dog'
'''
IMP Info: 
d1['A'] --- direct access the value which is associated to key, but it will throw KeyError if key not found
d1.get('A') - The get() method is a safer way to access a value in a dictionary. If the key 'A' exists, it returns the 
             associated value. However, if the key 'A' does not exist, it returns None by default (or a specified default value, 
             if you provide one as a second argument to the get() method). It avoids raising a KeyError.
'''
# we can check key is presant in dict by using in operator
if 'D' in d1:
    print(d1['A'])
    print(d1.get('A','Orange')) # d1.get('B','Orange')

# we can check value is presant in dict by using values() function and in operator
if 'Dog' in d1.values():
    print(d1['A'])
    print(d1.get('A'))
_keys = d1.keys()
print(_keys)
print(type(_keys))

_values = d1.values()
print(_values)
print(type(_values))

items = d1.items()
print(items)
print(type(items))


        


  


    
