from collections import OrderedDict,defaultdict,UserDict,ChainMap

inventory = {'Banana':200,'Apple':100}
print(inventory.get('Papaya','key does not exit'))
inventory['Papaya'] = 150
inventory['Mango'] = 250
print(inventory)

inventory1 = OrderedDict(inventory)
print(inventory1)

x=25

if x > 30 or x < 25:
    print('OK')


