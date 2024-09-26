

def test():
    rule_info={}
    condition_info={}
    r_c = []
    outer_index = 0
    inner_index = 0
    for i in range(2):
        rule_info[outer_index]=[
                {"rule_name":"Student Rule"+str(i)},
            ]
        for j in range(2):
            print("Innner for")
            condition_info[inner_index]=[
                    { "value":"Student "+str(j)+" OuterIndex "+str(i)},
                ]
            inner_index+=1
        outer_index+=1 
    r_c.append(rule_info)
    r_c.append(condition_info)
    return r_c   
rclist = test()
rules = rclist[0].values()
print(type(rules))
conditions = rclist[1].values()

for r in rules:
    for ru in r:
        print(ru['rule_name'])
        for c in conditions:
            for v in c:
                print(v['value'])

    print('*****************')


d1 = {'A':'Apple','B':'Banana','C':'Cat'}
d1['D']='Dog'

# we can check key is presant in dict by using in operator
if 'D' in d1:
    print(d1['A'])
    print(d1.get('A'))

# we can check value is presant in dict by using values() function and in operator
if 'Dog' in d1.values():
    print(d1['A'])
    print(d1.get('A'))
        


  


    
