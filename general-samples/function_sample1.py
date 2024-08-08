# define fucntion
def test_function():
    print(f'This is test function implementation')

test_function() # calling function, out put is : This is test function implementation

test_function1 = test_function # copy referance

test_function1() #out put is : This is test function implementation

def add(x1: int,x2: int) -> int:
    return x1+x2

def mult(x1: int,x2: int) -> int:
    return x1*x2

def math_operations(operation, x1,x2):
    result = operation(x1,x2)
    return result

add_res = math_operations(add,10,20)
print(add_res)

mult_res = math_operations(mult,10,20)
print(mult_res)