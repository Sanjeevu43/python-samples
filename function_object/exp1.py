#Example 1: Treating the functions as objects. 

def f1(text):
    return text.upper()

res1 = f1('welcome')  # function calling
print(res1)

f2 = f1 # This will not call the function instead it takes the function object referenced by a f1 and creates a second name pointing to it, f2.
res2 = f2('to python')
print(res2)

print('f1 ID : ',id(f1))
print('f2 ID : ',id(f2))

# Example 2: Passing the function as an argument 
def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument.")
    print (greeting)
 
greet(shout)
greet(whisper)

def greet(func, value):
    # storing the function in a variable
    greeting = func(value)
    print (greeting)
 
greet(shout,"one")
greet(whisper,"TWO")

# In the above example, the greet function takes another function as a parameter (shout and whisper in this case). 
# The function passed as an argument is then called inside the function greet.

# Example 3: Returning functions from another function.

def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
result = add_15(10) 
print(result)

##############################################################################

#This is a classic Python "gotcha" related to closures and late binding.
#The generate function is a closure
print('*************************************************************************************')
def functions():
    result = []
    for i in range(5):
        def generate(x,i=i):
            return x*i
        result.append(generate)
    return result

function = functions()
for f in function:
    print(f(2))
        

