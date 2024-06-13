from skspatial.objects import Line

from libs.geometryobjects import Vector
from libs.plots import Plot3D
from utils.misc import clear_terminal

clear_terminal()

pl = Plot3D(plot_array=False, plot_name=True)
u = Vector([1, 5, 9], 'u')
v = Vector([5, 9, 1], 'v')
w = Vector([9, 1, 5], 'w')
vecs = [
    u,
    v,
    w,
    u-w,
    v-w,
    u-v,
    1/3*u+1/3*v+1/3*w,
    1/2*u+1/2*w,
    1/2*u+1/2*v,
    1/2*w+1/2*v,
]
pl.plot_vectors(vecs)

ln = Line.from_points(u, v)
pl.plot_line(ln, linestyle='dashed')
ln = Line.from_points(u, w)
pl.plot_line(ln, linestyle='dashed')
ln = Line.from_points(w, v)
pl.plot_line(ln, linestyle='dashed')
pl.savefig(__file__.replace('.py', '.svg'))
pl.show()
