
def calculator(func, value1,value2):
    result = func(value1,value2)
    return result

def mult(x,y):
    return x*y

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

result = calculator(add,10,5)
print(result)

    

