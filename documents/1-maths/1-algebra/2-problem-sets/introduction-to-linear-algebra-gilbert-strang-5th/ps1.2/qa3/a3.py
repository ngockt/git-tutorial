# Answer 3 code

import numpy as np
from skspatial.objects import Vector

ans_file_path = __file__.replace('.py', '.txt')

v = Vector((4., 3.))
w = Vector((1., 2.))

print(f'Unit vector of v: {v.unit()}')
print(f'Unit vector of w: {w.unit()}')
print(f'Angle between u and v: {np.degrees(v.angle_between(w)).round(4)}')

a = Vector((2, 4))
print(f'a = {a}, angle between a and w {np.degrees(w.angle_between(a)).round(4)}')
b = Vector((-2, 1))
print(f'b = {b}, angle between a and w {np.degrees(w.angle_between(b)).round(4)}')
c = Vector((-1, -2))
print(f'c = {c}, angle between a and w {np.degrees(w.angle_between(c)).round(4)}')
