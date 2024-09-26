t1 = (1,2,3,4)
print(t1)
t2 = (3,)
print(t2*3)
t3 = 1,2,3
print(t3)

t4 = (1,2,3,[4,5,6])
t4[3][0]=44
value = t4[3]
print(value)
'List of tuples'
l1 = [(1,2),(3,4)]
l1[1]=(10,20)
print(l1)
x=2
y=3
x,y=y,x
print(x,y)

#Packing & Unpacking Tuple
t5 = ""
t5 = ('Sanjeevu',42,200000); 
name,_,Sal = t5
print(name,Sal)
