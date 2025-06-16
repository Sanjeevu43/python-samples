from itertools import zip_longest,product
import numpy as np

X_c = [101,102,103]
Y_c = [501,500,503]
Z_c = [1,2]

def parallelIterare(X: list, Y: list,Z: list):

    for x,y,z in zip(X,Y,Z):
        print(f"X coordinates : {x}, Y coordinates : {y}, Z coordinates : {z}")

parallelIterare(X_c,Y_c,Z_c)

print("=========================================="*2)

def parallelIterare(X: list, Y: list,Z: list):

    for x,y,z in zip_longest(X,Y,Z):
        print(f"X coordinates : {x}, Y coordinates : {y}, Z coordinates : {z}")

parallelIterare(X_c,Y_c,Z_c)


print("=========================================="*2)

X_c = [101,102,103]
Y_c = [501,500,503]
Z_c = [1,2,3]

np_array = np.array([X_c,Y_c,Z_c])
for x,y,z in np_array:
        print(f"Point: X={x}, Y={y}, Z={z}")