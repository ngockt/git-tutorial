from contextlib import redirect_stdout

import sympy as sp

from libs.linalg.matrix import print_matrix

sp.init_printing(num_columns=200)

ans_file_path = __file__.replace('.py', '.txt')


A = sp.Matrix([
    [2, -1, 1, 1],
    [-1, 2, -3, 0],
    [0, -1, 2, 0]
])

with redirect_stdout(open(ans_file_path, 'w', encoding="utf-8")):
    print_matrix(A, 'A')
    print_matrix(A.rref()[0], 'R')


# import ipdb; ipdb.set_trace()
