my_dict1 = {"name":"Sanjeevu","age":40,"city":"Blor"}

for value in my_dict1.values():
    print(value)

my_dict1.update({"gender":"male"})

for key in my_dict1.keys():
    print(key)

my_dict1.pop("gender")
for key,value in my_dict1.items():
    print(f'{key} : {value}')

for k in my_dict1:
    print(f'Key:{k}, Value:{my_dict1[k]}')