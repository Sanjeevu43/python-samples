import threading
import time

result = []
start_time = time.time()
def generate(start: int, end: int, result:list):
    for i in range(start, end):
        result.append(i)

t1 = threading.Thread(target=generate, args=(1,501, result))
t2 = threading.Thread(target=generate, args=(501,1001, result))
t3 = threading.Thread(target=generate, args=(1001,1501, result))

t1.start()
t2.start()
t3.start()
 
t1.join()
t2.join()
t3.join()

print(result)
end_time = time.time()
print('*******************************************************************************************************************')
print("Execution time : ", (end_time-start_time))
print('*******************************************************************************************************************')

def m1():
    result1 = []
    start_time1 = time.time()
    #result1 = [i for i in range(1,1501)]
    for i in range(1,1501):
        result1.append(i)
    end_time1 = time.time()
    print(result1)
    print('*******************************************************************************************************************')
    print("Execution time : ", (end_time1-start_time1))
    print('*******************************************************************************************************************')

    
m1()







# thread_list = []
# results = []
# for x in x_ls:
#  thread = threading.Thread(target=func_thread, args=(x, results))
#  thread_list.append(thread)
# for thread in thread_list:
#  thread.start()
# for thread in thread_list:
#  thread.join()