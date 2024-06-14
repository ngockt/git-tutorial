
import numpy as np
from skspatial.objects import Line, Points

from libs.geometryobjects import Vector
from libs.plots import Plot2D
from utils.misc import clear_terminal

clear_terminal()

pl = Plot2D(plot_array=False, plot_name=True)
v = Vector([5, 1], 'v')
w = Vector([1, 5], 'w')
vecs = [
    v,
    w,
    v + w
]
pl.plot_vectors(vecs)
points = Points([((c * v) + (d * w)).to_array() for c, d in np.random.rand(10000, 2).tolist()])
ln = Line.from_points((0, 0), v + w)
pl.plot_line(ln)
pl.plot_points(points)

pl.savefig(__file__.replace('.py', '.svg'))
pl.show()
