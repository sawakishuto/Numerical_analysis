# 二分法
import numpy as np   


def f(x):
    return x**2 -5.0

def binarySearch(f, a, b, limit=2.23, max=50):
    num = 0
    print("{} {}<=x<={}".format(num, a, b))
    if(f(a)*f(b) > 0):
        return
    while(True):
        c = (b+a)/2.0
        if (0.0 < f(c)*f(a)):  
            a = c  
        elif(f(b) * f(c) > 0): 
            b = c 
        num += 1
        print("{}回目は a ={}, b = {}より".format(num, a, b))
        if((b-a >= limit) or max <= num):
            break
    print(str(c))

    return c



#メイン実行部
if (__name__ == '__main__'):

    solution = binarySearch(f, 2.0, 3)