import sys

# x  = [1,2,3,4]
# print(x[::])
 

if __name__ == "__main__":
    script_name = sys.argv[0]
    print(script_name)
    arg_list = sys.argv[1:]
    # if len(sys.argv) >1 :
    #     print(sys.argv[1])
    # else:
    #     print('No command line arguments passed')

    for arg in arg_list:
        print(arg)