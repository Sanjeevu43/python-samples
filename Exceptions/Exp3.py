# In below code syntax is correct but exception is not handled,so last statement will not execte
#but finally block will execute

def m1():
    try:
        i = 10
        j = i/0
        print(j)
    finally:
        print('Always executes')
    
    print('Last statement')

m1()