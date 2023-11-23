# 冪乗で固有値計算
import numpy as np

def power(matrix, v, limit=0.1, max_iter=100):
    n = 0
    while n < max_iter:
        x = matrix @ v 
        r = x[0, 0] 
        print(f"反復 {n + 1}  固有値: {r}")
        v = x / r 
        n += 1
        if np.linalg.norm(matrix @ v - r * v) < limit:
            print("収束した！")
            return r, v   
    return None
# 対象の行列
matrix_A = np.array([[3, 1], [1, 3]])
# 初期値
initialmat = np.array([[1], [0]])
power(matrix_A, initialmat)
