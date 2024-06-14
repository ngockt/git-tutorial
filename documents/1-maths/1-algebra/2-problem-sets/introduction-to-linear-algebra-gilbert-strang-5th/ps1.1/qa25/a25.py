from skspatial.objects import Line, Plane

from libs.geometryobjects import Vector
from libs.plots import Plot3D
from utils.misc import clear_terminal

clear_terminal()

pl = Plot3D(plot_array=False, plot_name=True)
u = Vector([1, 5, 3], 'u')
v = Vector([2, 10, 6], 'v')
w = Vector([-1, -5, -3], 'w')
t = Vector([1, 1, 1], 't')
vecs = [
    u,
    v,
    w,
    t
]
pl.plot_vectors(vecs, alpha=0.5)
ln = Line(u, v)
pl.plot_line(ln)

pl.ax.view_init(elev=45, azim=-60, roll=0)
pl.savefig(__file__.replace('.py', '.svg'))
pl.show(block=False)

pl = Plot3D(plot_array=False, plot_name=True)
u = Vector([1, 5, 3], 'u')
v = Vector([1, 3, 5], 'v')
w = Vector([1, 4, 4], 'w')
t = Vector([1, 1, 1], 't')

vecs = [
    u,
    v,
    w,
    t
]
pl.plot_vectors(vecs)
plane = Plane.from_points([0, 0, 0], u, v)
pl.plot_plane(plane, alpha=0.3)
pl.ax.view_init(elev=-30, azim=100, roll=0)
pl.savefig(__file__.replace('.py', '_1.svg'))
pl.show()
