l = [1,2,3,4,5,5,6,7,8,1,2,3,9]

s= {i for i in l}
print('s type : ', type(s))
print('s : ', s)

d= {i:i for i in l}
print('d type : ', type(d))
print('d : ', d)

ll = [1,1,2,2]
tp = (1,1,2,2)
s = set()
s.update(ll)
print(ll)
print(s)

s = {'University'}
print(s)