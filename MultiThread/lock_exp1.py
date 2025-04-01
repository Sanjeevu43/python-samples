import threading

x = 0
def increment():
    global x
    # In theory, the GIL protects this, but let's consider a worst-case scenario
    local_x = x
    local_x += 1
    x = local_x

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(x)  # May or may not be 2, depending on timing

#======================================================================================
# Lock using with 'with Statement'
print('===============================================================================')
x = 0
lock = threading.Lock()
def increment():
    global x
    with lock:
        local_x = x
        local_x += 1
        x = local_x

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(x)  # Will always be 2

#=============================================================================================
# Lock using without 'with Statement'

import threading

x = 0
lock = threading.Lock()

def increment():
    global x
    lock.acquire()  # Acquire the lock
    try:
        local_x = x
        local_x += 1
        x = local_x
    finally:
        lock.release()  # Release the lock (always!)

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(x)  # Will always be 2