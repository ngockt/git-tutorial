# Answer 13 code
from contextlib import redirect_stdout

import numpy as np
import sympy as sp

from libs.linalg.matrix import print_matrix, to_sp_matrix

sp.init_printing(num_columns=200)

ans_file_path = __file__.replace('.py', '.txt')


A = np.array([[0, 1, 0, 0, 0],
              [-1, 0, 1, 0, 0],
              [0, -1, 0, 1, 0],
              [0, 0, -1, 0, 1],
              [0, 0, 0, -1, 0]])
A = to_sp_matrix(A)
R = A.rref()[0]
with redirect_stdout(open(ans_file_path, 'w', encoding="utf-8")):
    print_matrix(A, 'A')
    print_matrix(R, 'R')
