# レイリー商
# 最大固有値を求めたい
import ast
import numpy as np
def reily(A, x, limit = 3.88):
        x_d = A @ x
        print("x_dは\n{}".format(x_d))
        r = (np.array(x) @ x_d)/(np.array(x) @ x)
        print("レイリー商は\n{}".format(r))
        abs_x_d = np.sqrt(x_d[0]** 2 + x_d[1] ** 2)
        print(abs_x_d)
        x_d = [x_d[0] / abs_x_d, x_d[1] / abs_x_d]
     
        print((x_d))
        if r <= limit:
            reily(A, x_d)
        else:
              print("結果は{}です。".format(r))
# 二次元配列で入力
# 対象の行列
print("対象となる行列を入力:")
matrix_A_input = input() 
A = np.array(ast.literal_eval(matrix_A_input))
# 1次元配列で入力
# 初期
print("初期:")
matrix_A_input = input() 
x = np.array(ast.literal_eval(matrix_A_input))
reily(A, x)
