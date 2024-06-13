# Answer 2 code
import numpy as np

from libs.geometryobjects.vectors import Vector

ans_file_path = __file__.replace('.py', '.txt')

u = Vector((-.6, .8), name='u')
v = Vector((4., 3.), name='v')
w = Vector((1., 2.), name='w')

print(f'{np.dot(u, v).round(4)} = |u \u22C5 v| <= ||u|| ||v|| = {np.abs(np.linalg.norm(u)*np.linalg.norm(v))}')
print(f'{np.dot(w, v).round(4)} = |v \u22C5 w| <= ||v|| ||w|| = {np.abs(np.linalg.norm(w)*np.linalg.norm(v)).round(4)}')
