l1 = [1,2,3]
l2 = [4,5,6]
l3 = [1,2,3]

print('l1 == l2', l1==l2)
print('l1 == l3', l1==l3)

print('l1 is l3', l1 is l3)

def get_rules(i):
    rul = []
    rul.append({
        "name":"Sanjeevu",
        "Id":i,
        "Score": i+1,
        "Operator": "And"
        })
    
    return rul

rules_list = []
rules = []
for i in range(1,4):
    rules+= get_rules(i)
    rules_list.append(rules)
    
print(rules)
print(rules_list)