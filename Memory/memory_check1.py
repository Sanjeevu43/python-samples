import tracemalloc
import gc
tracemalloc.start()
# scenario one
values = []
def f1():
    for i in range(1,10000):
        values.append(i)

def f2():
    f1()
    print(values[:10])
f2()
# del values
# gc.collect()
# values = []
print("Memory used : ",tracemalloc.get_traced_memory())
tracemalloc.stop()

# scenario two
# def f1():
#     values = []
#     for i in range(1,10000):
#         values.append(i)
#     print(values[:10])

# f1()
# print("Memory used : ",tracemalloc.get_traced_memory())
# tracemalloc.stop()
