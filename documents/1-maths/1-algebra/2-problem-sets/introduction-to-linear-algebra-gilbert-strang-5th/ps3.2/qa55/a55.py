
import sympy as sp
from sympy.abc import I
from libs.linalg.matrix import print_matrix


A = sp.Matrix([[I, I]])
NA = sp.Matrix([[I], [-I]])
print_matrix(A, 'A')
print_matrix(NA, 'N(A)')

B = sp.Matrix([[I, I], [0, 0]])
NB = sp.Matrix([[I], [-I]])
print_matrix(B, 'B')
print_matrix(NB, 'N(B)')