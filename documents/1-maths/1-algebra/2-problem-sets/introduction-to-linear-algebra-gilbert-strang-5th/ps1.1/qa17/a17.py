
from skspatial.objects import Line

from libs.geometryobjects import Vector
from libs.plots import Plot2D

pl = Plot2D(plot_array=False, plot_name=True)
v = Vector([5, 1], 'v')
w = Vector([1, 5], 'w')
vecs = [
    v,
    w,
    *[c*v + c*w for c in (1/3, 2/3, 1, 2)]
]
pl.plot_vectors(vecs)
ln = Line.from_points((0, 0), v+w)
pl.plot_line(ln)
pl.savefig(__file__.replace('.py', '.svg'))
pl.show()
