# 固有値と固有ベクトル
import numpy as np

def eigen(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    diagonal_matrix = np.diag(eigenvalues)

    print("固有値")
    print(eigenvalues)
    print("固有値からなる対角行列:")
    print(diagonal_matrix)
    
    print("固有ベクトル:")
    print(eigenvectors)

A = np.array([[3, 1,0], [1, 3,0], [1,2,0]]) 
eigen(A)
