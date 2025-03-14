
def f1(i,j,k=0):
    print(i+j+k)

f1(10,20,30)

def f2(i,*j,k):
    print(i+k)

f2(10,30,40,k=5)

def f3(i,*j,**k):
    pass

res = lambda i,*j,k: i+k

print(res(10,20,30,k=5))
      