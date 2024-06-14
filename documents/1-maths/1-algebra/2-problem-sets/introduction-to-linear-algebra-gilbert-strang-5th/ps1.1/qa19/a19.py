import numpy as np

from libs.geometryobjects import Vector
from libs.plots import Plot2D
from utils.misc import clear_terminal

clear_terminal()

pl = Plot2D(plot_array=False, plot_name=False)
v = Vector([5, 1], 'v')
w = Vector([1, 5], 'w')
vecs = [
    v,
    w,
    v + w
]
combs = [((c * v) + (d * w)) for c, d in zip(np.random.randint(0, 1000, 1000).tolist(), np.random.randint(0, 1000, 1000).tolist())]

pl.plot_vectors(vecs + combs)

pl.savefig(__file__.replace('.py', '.svg'))
pl.show()
