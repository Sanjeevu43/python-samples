import numpy as np
class Iterator_Exp():
    def __init__(self):
        pass
    def interate_3d_values(self, x_c: list, y_c: list, z_c:list):
        for x,y,z in zip(x_c,y_c,z_c):
            #zip_longest
            print(f"X={x}, Y={y}, Z={z}") #x1,y1,z1

        np_array = np.array([x_c,y_c,z_c])
        for x,y,z in np_array:
            print(f"Point: X={x}, Y={y}, Z={z}")
        
    

X_C = [10,20,30] # x1,x2,x3
Y_C = [100,200,300]
Z_C = [500,600,700]

# 10 101 102

point1 = {10,20,30} # x1,y1,z1
point2 = {101,201,301}
point3 = {102,202,302}

obj = Iterator_Exp()
obj.interate_3d_values(X_C,Y_C,Z_C)




