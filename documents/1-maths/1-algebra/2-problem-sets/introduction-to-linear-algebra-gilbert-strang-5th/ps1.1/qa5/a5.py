from skspatial.objects import Plane

from libs.geometryobjects import Vector, Vectors
from libs.plots import Plot3D

ans_path = __file__.replace('.py', '.svg')

pl = Plot3D(plot_array=True, plot_name=True)
u = Vector([1, 2, 3], name='u')
v = Vector([-3, 1, -2], name='v')
w = Vector([2, -3, -1], name='w')
vectors = Vectors(u, v, w)
ax = pl.plot_vectors(vectors)
plane = Plane.from_points([0, 0, 0], u, v)
pl.plot_plane(plane, alpha=0.5)
pl.ax.view_init(elev=-150, azim=-10, roll=0)
pl.savefig(ans_path)
pl.show()
