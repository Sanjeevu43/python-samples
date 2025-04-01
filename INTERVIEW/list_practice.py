
l = []
l.append(10)
#l.append(20) # value should be (iterable) list,tuple,string
l.extend('20')
l.extend([30])
l.extend((40,))

print(l)

#reverse,sort, desending
ll = [6,8,7,1,5,4,2,9,3]
print(ll,'#')
ll.reverse()
print(ll,'#')
ll.sort()
print(ll,'#')
ll.sort(reverse=True)
print(ll)

lll = [5,1,3,2,4,3]
lll = sorted(lll) # builtin function
print(lll)
print(lll.count(6))
#==========================================================================================

l1 = [1,2,3]
l2 = [1,3,1]
l3 = [1,2,3]

print(l1==l2)
print(l1==l3)

# print(com(l1,l2))
# print(l1==l3)

print(l1 is l2)
print(l1 is l3)
l1=l3
print(l1 is l3)
print('********************************************************************************************')

newl_ = [1,2,3,4]
#newl_[0]=10 # to modify the value
newl_.append(5)
newl_.insert(5,6)
#newl_.extend(7) # TypeError will get
newl_.extend([7,8,9]) # or newl_.extend((7,8,9)) also ok

print(newl_)
newl_.clear()
print(newl_)








