# A^n行列
import numpy as np

def a_n(matrix, n):
    return np.linalg.matrix_power(matrix, n)
# ここにn乗したい行列
matrix_A = np.array([[3, 1],
                    [1, 3]])

n = 2
result = a_n(matrix_A, n)

print(f"Aの{n}乗:")
print(result)
