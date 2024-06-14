import numpy as np

s = np.array([4, 5, 6])  # sum
d = np.array([2, 5, 8])  # diff

v = (s+d)/2
w = (s-d)/2

print('v =', tuple(v))
print('w =', tuple(w))
