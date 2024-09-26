import collections
# Dupluate keys not allowed
people = {'ID_3': "Jim", 'ID_2': "Jack", 'ID_4': "Jane", 'ID_1': "Jill",'ID_3': "July"}
#print(people)

person = {}
person['ID_1'] = {'name':'Sanjeev', 'age':40}
person['ID_2'] = {'name':'Bittu', 'age':8}

org = {}
org['ID_3'] = {'name':'Unisys', 'loc':'Blr'}
org['ID_4'] = {'name':'HP', 'age':'Blr'}

output = {}
output[0] = {'person':person, 'org':org}

pres= {}
ores = {}
for i in output.values():
    for k1, v1 in i.items():        
        if k1 == "person":
            pres[k1] = v1
        elif k1 == "org":
            ores[k1] = v1

print('Person: ', pres)
print('Ores: ', ores)

pres1 = {k:v for d in output.values() for k, v in d['person'].items()}
ores1 = {k:v for d in output.values() for k, v in d['org'].items()}

#print('Person: ', pres1)
#print('Org: ', ores1)