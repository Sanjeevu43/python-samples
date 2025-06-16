'''
In Python, a decorator is a function that takes another function as an argument, extends its 
behavior without explicitly modifying it, and returns the modified function. Decorators 
provide a way to add functionality to functions or methods in a reusable and readable manner. 
They are often used for tasks such as logging, access control, instrumentation, and validation. 
'''
# A simple decorator function
def decorator(func):  
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator
def greet():
    print("Hello, World!")

greet()

def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Add functionality before the original function call
        result = func(*args, **kwargs)
        # Add functionality after the original function call
        return result
    return wrapper

@decorator_name
def function_to_decorate():
    # Original function code
    pass

#-----------------------------------------------------------------------------------------------
import functools
from collections import OrderedDict

def cache_decorator(max_size):
    def decorator(func):
        cache = {}  # Stores (key, value) pairs, remembers insertion order
        @functools.wraps(func) # Preserves function metadata (name, docstring, etc.)
        def wrapper():
            # Add functionality before the original function call
            #max_size use this
            for i in range(1,max_size):
                 cache["key"]="value"           
            result = func()            
            return result
        return wrapper
    return decorator

@cache_decorator(max_size=10)
def cache_test(n):
    print(f"  (slow_add called with {a}, {b})")
    import time
    time.sleep(1) # Simulate a slow operation
    return n

cache_test(5)
        