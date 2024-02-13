
def person_info(name: str, age: int) -> None:
    return f'Name: {name} Age: {age}'

res = person_info('Sanjeev','XYZ') # this is not correct, because age should be int, 
#python is dynamically typed so here age accept str value. To solve this type issue we can use pydantic
print(res) # res is Name: Sanjeev Age: XYZ

