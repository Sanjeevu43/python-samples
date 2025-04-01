import threading
import time

def target_function():
    print(f'Started {threading.current_thread.__name__}')
    print('Hello')
    print('Execution completed')

if __name__ == '__main__':
    
    t1 = threading.Thread(target=target_function)
    print('T1 is alive :',t1.is_alive())
    t2 = threading.Thread(target=target_function)
    print('T2 is alive :',t2.is_alive())

    t1.start()
    t2.start()
    print('********************************************')
    print('T1 is alive :',t1.is_alive())
    print('T2 is alive :',t2.is_alive())
    time.sleep(30)

    print('********************************************')
    print('T1 is alive :',t1.is_alive())
    print('T2 is alive :',t2.is_alive())




