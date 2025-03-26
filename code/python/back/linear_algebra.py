import numpy as np
vector = np.array([1, 2, 3])  # 向量
matrix = np.array([[1, 2], [3, 4]])  # 矩阵
print(matrix.shape)  # 输出 (2, 2)

zeros_arr = np.zeros((3, 4))
print(zeros_arr)

arange_arr = np.arange(0, 10, 2)
print(arange_arr)

linspace_arr = np.linspace(0, 1, 5)
print(linspace_arr)


import numpy as np

# 创建一个矩阵
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.shape)
