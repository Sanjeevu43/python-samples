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

# can't add lists in set, but can add tuple or duplicate tuples
try:
    s1={1,2,2,[3,4,5]}
    print(s1)
except Exception as e:
    print(e) #TypeError: unhashable type: 'list'
s2={1,2,2,(3,4,5),(3,4,5)}
print(s2)

s3={1,2,3}
# print(s3)
# s3.clear()
# print(s3)
s3.add(4)
print(s3)
#s3.pop()
# print(s3)
#s3.remove(5)
#s3.discard(4)
s3.update([4,5,6])
print(s3)
