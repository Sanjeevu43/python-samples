from concurrent.futures import ThreadPoolExecutor
from threading import *
from time import sleep
 
values = [3,4,5,6]
 
def cube(x):
    print(f'Cube of {x}:{x*x*x}')
    print("Child Thread :", current_thread().getName())
 
 
if __name__ == '__main__':
    print("If block executed")
    result =[]
    with ThreadPoolExecutor(max_workers=2) as exe:
        #exe.submit(cube,2)
         
        # Maps the method 'cube' with a list of values.
        result = exe.map(cube,values)
     
    for r in result:
      print(r)
    

print("Done")
print("Control return to ", current_thread().getName())