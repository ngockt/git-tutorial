
from skspatial.objects import Line

from libs.geometryobjects import Vector
from libs.plots import Plot2D

pl = Plot2D(plot_array=False, plot_name=True)
v = Vector([5, 1], 'v')
w = Vector([1, 5], 'w')
vecs = [
    v,
    w,
    *[c*v + (1-c)*w for c in range(-5, 5, 1)]
]
pl.plot_vectors(vecs)
ln = Line.from_points(v, w)
pl.plot_line(ln)
pl.savefig(__file__.replace('.py', '.svg'))
pl.show()
