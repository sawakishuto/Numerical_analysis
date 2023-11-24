# 冪乗で固有値計算
import numpy as np

def power(matrix, v, limit=0.001, max_iter=100):
    n = 0
    while n < max_iter:
        x = matrix @ v 
        r = x[0,0]
        print(f"反復 {n + 1}  固有値r: {r}")
        v = x / r 
        n += 1
        print("x{}の値は\n{}".format(n,v))
        if np.linalg.norm(matrix @ v - r * v) < limit:
            print("収束した！")
            return r, v   
    return None
# 対象の行列
matrix_A = np.array([[4, 1], [1, 0]])
# 初期値
initialmat = np.array([[1], [0]])
power(matrix_A, initialmat)
