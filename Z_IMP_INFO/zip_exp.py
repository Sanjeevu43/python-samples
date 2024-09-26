emp_ids = [1,2,3,4,5]
emap_names= ['A','B','C','D']

new_emp_ids= []
new_emp_names = []
emp_ids_names = {}
for id,name in zip(emp_ids,emap_names):
    new_emp_ids.append(id+100)
    new_emp_names.append(name+'*')
    emp_ids_names[id+100] = name+'*'
    
print(new_emp_ids)
print(new_emp_names)
print(emp_ids_names)

for i in range(1,4):
    print(i)


