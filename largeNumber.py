# ２番目の固有値
import numpy as np

def eigen(A):
        eigenvalues, eigenvectors = np.linalg.eig(A)
        sorted_pairs = sorted(zip(eigenvalues, eigenvectors.T), key=lambda x: x[0], reverse=True)
        max_eigenvalue, max_eigenvector = sorted_pairs[0]
        max_eigenvector_transposed = [[max_eigenvector[0]], [max_eigenvector[1]]]
        # Aから最大固有ベクトルによる影響を取り除いた行列を計算
        A_dash = A - np.multiply(max_eigenvalue * np.array(max_eigenvector) , np.array(max_eigenvector_transposed))
        return A_dash
def eigenValue(result):
        eigenvalues, eigenvectors = np.linalg.eig(result)
        return max(eigenvalues)

A = np.array([[3, 1], [1, 3]]) 
   
result = eigen(A)
print("Aダッシュは\n{}".format(result))
result2 = eigenValue(result)
print("2番目の固有値は{}".format(result2))
