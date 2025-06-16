import functools # Important for preserving function metadata

def simple_print_decorator(func_to_decorate):
    """
    This is a simple decorator that prints messages before and after
    the decorated function is called.
    """

    @functools.wraps(func_to_decorate) # This helps preserve the original function's name, docstring, etc.
    def wrapper_function(*args, **kwargs):
        # 1. Code to execute BEFORE calling the original function
        print(f"Calling function: {func_to_decorate.__name__} with arguments: args={args}, kwargs={kwargs}")

        # 2. Call the original function
        # We pass along any arguments it received
        result = func_to_decorate(*args, **kwargs)

        # 3. Code to execute AFTER calling the original function
        print(f"Function {func_to_decorate.__name__} finished. Result: {result}")

        # 4. Return the result of the original function
        return result

    return wrapper_function # The decorator returns the wrapper function

# --- How to use the decorator ---
@simple_print_decorator
def say_hello(name):
    """Greets the person passed in as a parameter."""
    message = f"Hello, {name}!"
    print(message)
    return f"Greeting for {name} complete."

if __name__ == "__main__":
    print("--- Calling say_hello ---")
    returned_value_hello = say_hello("Alice")
    print(f"Main script received from say_hello: {returned_value_hello}\n")