import threading
import time
msg1 = []
def print_cube(num,msg1):
    print("Cube : {}".format(num*num*num))
    msg1 = {}
    msg1[0]= {'ID:':1}

def print_square(num):
    print("Square : {}".format(num*num))   

start_time = time.time()
print_cube(2000,msg1)
print_square(20000)
end_time = time.time()
print("Execution time without thred : ", (end_time-start_time))
print(msg1)

msg = []
def print_cube1(num, msg):
    print("Cube : {}".format(num*num*num))
    msg = {}
    msg[0] = {'ID':3}

def print_square1(num, msg):
    print("Square : {}".format(num*num))
    msg = {}
    msg[1]= {'ID':4}

if __name__ =="__main__":
    # creating thread
    start_time = time.time()
    t1 = threading.Thread(target=print_cube1, args=(2000,msg))
    t2 = threading.Thread(target=print_square1, args=(20000,msg))   
 
    # starting thread 1 & 2
    t1.start()   
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    end_time = time.time()
    print("Execution time with thred : ", (end_time-start_time))
 
    # both threads completely executed
    print("Done!")
    print(msg)




