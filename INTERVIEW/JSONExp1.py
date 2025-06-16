import json

# Sample Python dictionary
data_to_write = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "isStudent": False,
    "courses": [
        {"title": "History", "credits": 3},
        {"title": "Math", "credits": 4}
    ],
    "address": None
}

with open('./myjson1','w') as file_obj:
    json.dump(data_to_write,file_obj,indent=2)

with open('./myjson1','r') as read_file:
    loaded_data = json.load(read_file)

print(loaded_data)
print('----------------------------------------------------------------------')   

message = '''
{
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "isStudent": false,
    "courses": [
        {
            "title": "History",
            "credits": 3
        },
        {
            "title": "Math",
            "credits": 4
        }
    ],
    "address": null
}
'''

json_obj = json.loads(message)
print(json_obj)