import time
import threading
import multiprocessing

def counter1(num):
    count = 0
    for _ in range(num):
        count += 1
    print('counter1 done!')

def counter2(num):
    count = 0
    for _ in range(0,num,2):
        count += 1
    print('counter2 done!')

if __name__ == "__main__":
    num = 2*10**7
    print(f'num is:  {num}')
    st = time.time()
    counter1(num)
    counter2(num)
    en =  time.time()
    print(f'time taken : {en-st}')  # time taken : 8.922202825546265

    # multithreading
    start_time = time.time()
    t1 = threading.Thread(target=counter1, args=(num,))
    t2 = threading.Thread(target=counter2, args=(num,)) 
    
    t1.start()   
    t2.start()
   
    t1.join()
    t2.join()

    end_time = time.time()
    print("Execution time with thred : ", (end_time-start_time))
    #Execution time with thred :  8.994461297988892

    # multitasking
    # start_time = time.time()
    # p1 = multiprocessing.Process(target=counter1, args=(num,))
    # p2 = multiprocessing.Process(target=counter2, args=(num,)) 
    
    # p1.start()   
    # p2.start()
   
    # p1.join()
    # p2.join()

    # end_time = time.time()
    # print("Execution time with thred : ", (end_time-start_time)) #Execution time with thred :  6.614134788513184
