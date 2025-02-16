
def m1(*i,**kwargs):
    print(i)
    for key,value in kwargs.items():
        print('OK')
        print(key,value)


m1([10,20],name='Sanjeev')