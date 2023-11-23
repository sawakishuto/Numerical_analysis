import numpy as np

def f(x):
  return np.sin(x) - x**2

def df(x):
  return np.cos(x) - 2*x

x=0.5
accuracy=0.01
n=1
# while文でf(x)=0まで繰り返す
while True:
  x = x - f(x)/df(x)
  print("{}回目  x={}  f(x)={}".format(n, x, f(x)))
  n += 1
  if abs(f(x)) < accuracy:
    break 

print(str(x))