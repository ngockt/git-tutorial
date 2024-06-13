
from libs.geometryobjects import Vector
from libs.plots import Plot2D

pl = Plot2D(plot_array=False, plot_name=True)
v = Vector([5, 1], 'v')
w = Vector([1, 5], 'w')
vecs = [
    v,
    w,
    0.5 * v + 0.5 * w,
    0.75 * v + 0.25 * w,
    0.25 * v + 0.25 * w,
    v + w
]
pl.plot_vectors(vecs)
pl.savefig(__file__.replace('.py', '.svg'))
pl.show()
