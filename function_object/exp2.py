
def _add(i,j):
    return (i+j)

def _mult(i,j):
    'this function will multiple given two numbers and return result'
    return (i*j)

def calculate(func,i,j):
    result = func(i,j)
    print(result)

calculate(_add,10,20)
calculate(_mult,5,4)

print(_mult.__doc__)

name = "Sanjeevu Peikalapati"
e_name = name.encode('utf-8')
print(e_name)
d_name = e_name.decode('utf-8')
print(d_name)
