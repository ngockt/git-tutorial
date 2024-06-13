from contextlib import redirect_stdout

import ipdb
import numpy as np
import sympy as sp

from libs.linalg.matrix import print_matrix, to_sp_matrix

sp.init_printing(num_columns=200)

ans_file_path = __file__.replace('.py', '.txt')

u = np.array([1, 3])
v = np.array([2, 7])
w = np.array([1, 5])
b = np.array([0, 1])

A = np.array([u, v, w, b]).T
A = to_sp_matrix(A)
R = A.rref()[0]

with redirect_stdout(open(ans_file_path, 'w', encoding="utf-8")):
    print_matrix(A, 'A')
    print_matrix(A.rref()[0], 'R')


ipdb.set_trace()
