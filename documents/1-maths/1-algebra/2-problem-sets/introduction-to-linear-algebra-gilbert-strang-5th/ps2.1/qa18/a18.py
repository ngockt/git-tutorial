
import sympy as sp


from libs.linalg.matrix import print_matrix

sp.init_printing(num_columns=500)

A = sp.Matrix([[3],
               [5]])
E1 = sp.Matrix([[1, 0],
                [-1, 1]])
B = sp.Matrix([[3],
               [5],
               [7]])
E2 = sp.Matrix([[1, 0, 0],
                [-1, 1, 0],
                [0, 0, 1]])

print()
sp.pprint(sp.Eq(sp.MatMul(E1, A, evaluate=False), E1*A))
print()
sp.pprint(sp.Eq(sp.MatMul(E2, B, evaluate=False), E2*B))