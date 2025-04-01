import gc  # For explicitly triggering garbage collection

class MyClass:
    def __new__(cls, *args, **kwargs):
        print(f"__new__ called for class: {cls.__name__}")
        instance = super().__new__(cls)  # Crucially call the superclass's __new__
        print(f"__new__ created instance: {instance}")
        return instance

    def __init__(self, name):
        print(f"__init__ called for instance: {self}")
        self.name = name
        print(f"__init__ initialized name to: {self.name}")

    def __del__(self):
        print(f"__del__ called for instance: {self} (name: {self.name}) - object is being destroyed")
    
    def normal_function(self):
        print(f'This is normal Function')

# Example Usage
print("Creating an instance:")
obj = MyClass("Example Object")
print("Instance created:", obj)
print("Accessing instance attribute:", obj.name)

obj.normal_function()

print("\nDeleting the instance (explicitly):")
del obj  # Remove the reference to the object
#obj.normal_function() # This line will not execute get NameError: name 'obj' is not defined
gc.collect()  # Suggest garbage collection (it might not happen immediately)

# print("\nCreating another instance, then letting it go out of scope:")
def create_and_destroy():
    print('***********************************************************************')
    temp_obj = MyClass("Temporary Object")  # Create inside the function
    print("Temporary object created inside function.")
    # temp_obj goes out of scope when the function returns
    temp_obj.normal_function()
create_and_destroy() # call this function
#temp_obj.normal_function() # This line will not work
gc.collect() #collect garbage