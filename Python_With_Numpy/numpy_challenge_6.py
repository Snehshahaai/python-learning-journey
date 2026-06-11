import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix Addition (A + B): \n",A + B)
print("Matrix Subtraction (A - B): \n",A - B)
print("Element-wise Multiplication: \n",A * B)
print("Matrix Multiplication: \n",np.matmul(A,B))
print("Transpose of A: \n",np.transpose(A))
