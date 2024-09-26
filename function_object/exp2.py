
def _add(i,j):
    return (i+j)

def _mult(i,j):
    return (i*j)

def calculate(func,i,j):
    result = func(i,j)
    print(result)

calculate(_add,10,20)
calculate(_mult,5,4)
