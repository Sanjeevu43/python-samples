org_list = [1,2,3,4,5,6,7,8,9]

out_dict = {}
# keys even numbers, values even numbers squares
out_dict = {i:i**2 for i in org_list if i%2 == 0}
print('Out_Dcit :', out_dict)

out_dict_1 = {}
for i in org_list:
    if i%2 == 0:
        out_dict_1[i] = i**2

print('Out_dict_1 : ', out_dict_1)

# ***************************************************** #

state = ['Andhra','Telangana','Karnataka','Tamilnadu']
capital = ['Amaravati','Hyd','Blore','Chennai']
out_dict_2 = {}

for k,v in zip(state,capital):
    out_dict_2[k] = v

print(out_dict_2)

mapped = zip(state,capital)
print('mapped type :', type(mapped))
print(dict(mapped))

# comprehension
out_dict_3 = {k:v for k,v in zip(state,capital)}
print(out_dict_3)

# All three gives same result

d = {'Name':'San','Age':45}
print(d)

items = {k:v for k,v in d.items()}
print(items)