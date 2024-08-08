# break , continue, pass, return are jump statements in python
def f1():
    for i in range(1,6):
        if i==3:
            break
        print(i)
    print('--------------------------------------------------------')
    for i in range(1,6):
        if i==3:
            continue
        print(i)
    
    print('--------------------------------------------------------')
    for i in range(1,6):
        if i==3:
            pass
        print(i)

if __name__ == '__main__':
    f1()