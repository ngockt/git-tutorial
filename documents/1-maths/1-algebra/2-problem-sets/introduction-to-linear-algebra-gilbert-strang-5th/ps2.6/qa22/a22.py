# Answer 22 code

import numpy as np
import sympy as sp

from libs.linalg.matrix import to_sp_matrix, print_matrix

sp.init_printing(num_columns=500)


A = np.array([[5, 3, 1],
              [3, 3, 1],
              [1, 1, 1]])

E1 = np.array([[1, 0, -1],
               [0, 1, -1],
               [0, 0, 1]])

E2 = np.array([[1, -1, 0],
               [0, 1, 0],
               [0, 0, 1]])

L = E2 @ E1 @ A
U = np.linalg.inv(E1@E2).astype(int)
A = sp.Matrix(A.T)
print_matrix(L, 'L = E2@E1@A = ')
print_matrix(U, 'L = inv(E1@E@)')
