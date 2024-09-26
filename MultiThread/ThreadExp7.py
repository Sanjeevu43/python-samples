import time
import threading
import multiprocessing

def counter1(start, end):
    count = 0
    for _ in range(start,end):
        count += 1
    print('counter1 done!')
    print('count = ',count)

def counter2(start,end):
    result = 0
    for _ in range(start,end):
        result += 1
    print('Count = ', result)
  
if __name__ == "__main__":
    #num = 2*10**7
    #print(f'num is:  {0, 2000000}')
    st = time.time()
    counter1(0,2000000)
   
    en =  time.time()
    print(f'time taken : {en-st}')  # time taken : 8.922202825546265

    # multithreading
    start_time = time.time()
    t1 = threading.Thread(target=counter2, args=(0,500000))
    t2 = threading.Thread(target=counter2, args=(500000,1000000))
    t3 = threading.Thread(target=counter2, args=(1000000,1500000))
    t4 = threading.Thread(target=counter2, args=(1500000,2000000)) 
    
    t1.start()   
    t2.start()
    t3.start()
    t4.start()
   
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    end_time = time.time()
    print("Execution time with thred : ", (end_time-start_time))
    
    #Execution time with thred :  8.994461297988892

   
