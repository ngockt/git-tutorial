from skspatial.objects import Plane

from libs.geometryobjects import Vector, Vectors
from libs.plots import Plot3D

ans_path = __file__.replace('.py', '.svg')
pl = Plot3D(plot_array=True, plot_name=True)

v = Vector((1, -2, 1), name='v')
w = Vector((0, 1, -1), name='w')
u = Vector((3, 3, 6), name='u')
vectors = Vectors(u, v, w)
pl.plot_vectors(vectors)
plane = Plane.from_points([0, 0, 0], w, v)
pl.plot_plane(plane, alpha=0.5)
pl.ax.view_init(elev=0, azim=-20, roll=0)
pl.savefig(ans_path)
pl.show()
