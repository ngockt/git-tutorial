from itertools import product

from libs.geometryobjects import Vector
from libs.plots import Plot2D

ans_path = __file__.replace('.py', '.svg')

pl = Plot2D(plot_name=True, plot_array=True)
u = Vector([2, 1], name='u')
v = Vector([0, 1], name='v')
vectors = []
for c, d in product(range(3), range(3)):
    vectors.append(c * u + d * v)

pl.plot_vectors(vectors)
pl.savefig(ans_path)
pl.show()
