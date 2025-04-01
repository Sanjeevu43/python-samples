
l = []
def m1():
    for i in range(5):
        l.append(i)
        yield i     # generator type
        # return i   # int type

result = m1()
print(type(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(l)

ll1 = [1,2,3,4,5,6]
ll2 = [i for i in ll1 if i%2==0]

print(ll1)
print(ll2)

def print_even(test_string):
    for i in test_string:
        if i == "geeks":
            yield i
 
 
# initializing string
test_string = " There are many geeks around you, \
              geeks are known for teaching other geeks"
 

res =  print_even(test_string.split())
print(next(res))
print(next(res))
print(next(res))

# we can iterate generator only once

# below for loop can't print item, bcoz  generator already iterated

# for item in res:
#     print('********** :', item)

# count numbers of geeks used in string
count = 0
print("The number of geeks in string is : ", end="")
test_string = test_string.split()
 
for j in print_even(test_string):
    count = count + 1
   
 
print('Count :',count)

test_string = " There are many geeks around you geeks are known for teaching other geeks"
test_string = test_string.split()
print(test_string)

a=b=c = 0
print(a)
print(b)
print(c)

# Keyword args
def add_function(n1:int, n2:int):
    print(n1)
    print(n2)
    return (n1+n2)

res = add_function(n2=10,n1=5)
print(res)

def gen_(n):
    print('function called')
    while n>0:
        print('Inside while')
        yield n
        n-=1
gen_res = gen_(5)
print(type(gen_res))
for n in gen_res:
    print(n)
# print(next(gen_res))
# for n in gen_res:
#     print('*********')
#     print(n)