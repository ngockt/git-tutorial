
import numpy as np
import sympy as sp

from libs.linalg.matrix import print_matrix


A = np.array([[2, -1],
              [3, -2]])

B = np.array([[1, 0, 4],
              [1, 0, 6]])

print_matrix(A @ B, "AB")
print_matrix(A @ A, "AA")
print_matrix(A @ A @ A, "AAA")
