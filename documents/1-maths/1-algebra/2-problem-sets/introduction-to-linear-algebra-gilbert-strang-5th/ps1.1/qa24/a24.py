from skspatial.objects import Plane

from libs.geometryobjects import Vector
from libs.plots import Plot3D
from utils.misc import clear_terminal

clear_terminal()

pl = Plot3D(plot_array=False, plot_name=True)
u = Vector([-1, 3, 5], 'u')
v = Vector([3, 5, -1], 'v')
w = Vector([5, -1, 3], 'w')
vecs = [
    u,
    v,
    w,
]
pl.plot_vectors(vecs)

plane = Plane.from_points([0, 0, 0], u, v)
pl.plot_plane(plane, alpha=0.3)

plane = Plane.from_points([0, 0, 0], v, w)
pl.plot_plane(plane, alpha=0.3)
pl.ax.view_init(elev=9, azim=90, roll=0)

pl.savefig(__file__.replace('.py', '.svg'))
pl.show()
