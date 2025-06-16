import time

# definition of lru decorator
def lru_decorator(size):    
    lru = {}    
    def decorator(func):        
        def wrapper(num):
            lru.insert(num)
            lru.print()            
            # to check the num pageframe(position)
            # uncomment the below statement
            # print(lur.map)
            print(num, func(num))
        return wrapper
    
    return decorator

# Using LRU Decorator
@lru_decorator(max_size=4)
def cache_test(n):
    print(f'Computing...{n}')
    time.sleep(1)
    return n

res = cache_test(1)