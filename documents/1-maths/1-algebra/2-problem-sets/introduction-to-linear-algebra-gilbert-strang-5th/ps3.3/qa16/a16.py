import sympy as sp

from libs.linalg.matrix import print_matrix

sp.init_printing(num_columns=500)

A = sp.Matrix([[1, 2, 1, 0, 1], [1, 2, 4, 4, 8], [1, 4, 8, 6, 8]])


print_matrix(A, "A")
print_matrix(A.echelon_form(), "U")
print_matrix(A.rref()[0], "R")