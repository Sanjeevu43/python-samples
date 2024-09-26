
strings = ["first", "", "second"]
print(strings)
print(len(strings))

str_list = list(filter(None, strings))
print(len(str_list))
print(str_list)

names = ["San","Bin","Lucky","Bittu"]

def get_names(name: str) -> str:
    print(name)
    return name

result =  map(get_names, names)
print(result)
