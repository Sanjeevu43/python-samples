
l = []
l.append(10)
#l.append(20) # value should be (iterable) list,tuple,string
l.extend('20')
l.extend([30])
l.extend((40,))

print(l)
