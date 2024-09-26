import numpy as np
from numpy import loadtxt

print(np.random.randint(1,5))
print(np.random.randn(2,4))
print(np.random.random(5))

l1 = [30,40,50,60]
l2 = [35,45,55,65]
print(l1)
l3 = np.random.shuffle(l1)

print(l1)

