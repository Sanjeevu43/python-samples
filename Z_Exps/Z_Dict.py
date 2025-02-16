my_dict1 = {"name":"Sanjeevu","age":40,"city":"Blor"}

for value in my_dict1.values():
    print(value)

my_dict1.update({"gender":"male"})

for key in my_dict1.keys():
    print(key)

my_dict1.pop("gender")
for key,value in my_dict1.items():
    print(f'{key} : {value}')

results = []
errors = []   
errors.append('Invalid data in http body')
results.append('OK')
response_data = {
    'errors': errors,
    'results': results            
}

print(response_data)

if 'errors' in response_data:
    print('YES')
    err = response_data['errors']

print(type(err))
print(err)
err.append('Invalid data2')
print(err)
response_data['errors']=err
print(response_data)