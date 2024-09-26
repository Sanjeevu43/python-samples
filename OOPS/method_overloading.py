from multipledispatch import dispatch

@dispatch(int,int)
def m1(a,b):
    res = a*b
    print(res)

@dispatch(float,int,int)
def m1(a,b,c):
    res = a*b*c
    print(res)
m1(30,40)
m1(10.0,20,30)