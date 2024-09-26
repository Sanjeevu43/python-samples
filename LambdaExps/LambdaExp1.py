'''
Python Lambda Functions are anonymous function means that the function is without a name. 
As we already know that the def keyword is used to define a normal function in Python. 
Similarly, the lambda keyword is used to define an anonymous function in Python. 
'''

lambda_add = lambda x,y: x+y

print('2 + 2 =',lambda_add(2,2))


l = [i*10 for i in range(1,5)]
print(l)

b_price = 20
s_price = b_price + 1
b_price = 30

print('Selling Price : ', s_price)
