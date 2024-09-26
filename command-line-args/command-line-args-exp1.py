import sys

# x  = [1,2,3,4]
# print(x[::])
 

if __name__ == "__main__":
    script_name = sys.argv[0]
    print(script_name)
    if len(sys.argv) >1 :
        print(sys.argv[1])
    else:
        print('No command line arguments passed')