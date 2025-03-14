import concurrent.futures
from threading import *
import time
import os

def cube(num):
    result = num*num*num*num*num
    print("Child Thread :", current_thread().getName())
    print(result)
    return True

if __name__ == "__main__":
    print(f'CPU count: {os.cpu_count()}')
    cpu_s = (os.cpu_count() or 1)
    print(f'CPU s: {cpu_s}')
    l = [2000,3000,4000,5000,6000,7000]
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
       features =  [executor.submit(cube,num) for num in l]
       #concurrent.futures.wait(features)
       print('All completed')

       for feature in features:
           print(feature.result())

    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executer:
    #     for num in l:
    #         feature = executer.submit(cube,num)
    #         res = feature.result()
    #         if res:
    #             print(f'Ok for {num}')
    #         else:
    #             print('Not Ok')


    end_time = time.time()
    print('***************************'*3)
    print('Execution Time:', (end_time-start_time))
