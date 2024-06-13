# Answer 1 code
import numpy as np

from libs.geometryobjects.vectors import Vector

ans_file_path = __file__.replace('.py', '.txt')

u = Vector((-.6, .8), name='u')
v = Vector((4, 3), name='v')
w = Vector((1, 2), name='w')

print(f'u \u22C5 v = {np.dot(u, v).round(4)}')
print(f'u \u22C5 w = {np.dot(u, w).round(4)}')
print(f'u \u22C5 (v + w) = {np.dot(u, v+w).round(4)}')
print(f'w \u22C5 v = {np.dot(w, v).round(4)}')
