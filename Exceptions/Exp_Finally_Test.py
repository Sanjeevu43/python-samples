import time
import datetime

def test():
    try:
        start_time = time.time()
        print("Try block time :  ",  datetime.datetime.now())
        for i in range(20):
            print('I = ',i)
        end_time = time.time()
       
    
    except:
        print('Will not execute')

    finally:
         start_time = time.time()
         print("Finally block time : ",  datetime.datetime.now())

test()