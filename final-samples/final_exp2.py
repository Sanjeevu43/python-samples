from typing import Final

def f2():
    age: Final = 30   
    print(age)
    # age = 40
    # assert age == 30
    # print(age)

f2()