
import sys

# x = 10;
# print(sys.getsizeof(x))

y = []
print(sys.getsizeof(y))
y = [i for i in range(1,10000)]
print(sys.getsizeof(y))

# z = ''
# print(sys.getsizeof(z))

# a = []
# print(sys.getsizeof(a))