import tracemalloc
import psutil

from memory_profiler import profile

def app():
    lt = []
    for i in range(0, 100000):
        lt.append(i)

tracemalloc.start()
app()
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
