
# Global variable
global_var = 10

def outer_function():
    # Outer function variable
    outer_var = 20

    def inner_function():
        # Local variable
        inner_var = 30

        print("Local variable:", inner_var) # 30
        nonlocal outer_var
        outer_var = 40
        print("Nonlocal variable:", outer_var) # 40
        global global_var
        global_var = 50
        print("Global variable:", global_var) # 50

    print("Outer variable-before:", outer_var) # 20
    inner_function()
    print("Outer variable-after:", outer_var) # 20

outer_function()
