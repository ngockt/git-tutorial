
import numpy as np
import sympy as sp

from libs.linalg.matrix import print_matrix

sp.init_printing(num_columns=500)


for idxs in ([
    [],
    [[0, 1]],
    [[0, 2]],
    [[1, 2]],
    [[0, 1], [0, 2]],
    [[0, 1], [1, 2]],
    [[0, 2], [1, 2]],
    [[0, 1], [0, 2], [1, 2]]
]):
    A = np.array([[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]])
    for i, j in idxs:
        A[i, j] = 1
    print_matrix(A, "")
