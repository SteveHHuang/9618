# 9608/21/M/J/18 Q6b

import random

Picture = [[random.randint(0,250)for i in range(8)]for i in range (8)]


def Lighten():
    global Picture
    BurntOut = False
    
    for i in range(8):
        for j in range(8):
            temp = Picture[i][j] * 1.1 # 2D array元素调用方式：arr[i][j] 
            Picture[i][j] = int(temp)
            if temp >= 255:
                BurntOut = True
    
    return BurntOut
            
print(Picture)            
print(Lighten())