# If we know which exception will raise then we use that eception in except block
# otherwise we can use it direct super or base class or Exception class
# If  we use other than these exception then exception is not handled
# In below commented except block only handle raised exception, other blocks won't handled,
# so last print statement not execute

def m1():
    try:
        i = 10
        j = i/0
        print(j)
    except (FloatingPointError,OverflowError): #ArithmeticError #FloatingPointError # OverflowError #ZeroDivisionError
        print('Exception handled 1')
    except (TypeError):
        print('Exception handled 2')
    except (NameError):
        print('Exception handled 3')
    # except (ZeroDivisionError):
    #     print('Exception handled 4')
    else:
        print('Executes else block')

    print('Last statement...')

m1()