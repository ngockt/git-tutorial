from skspatial.objects import Plane

from libs.geometryobjects import Vector, Vectors
from libs.plots import Plot3D

ans_path = __file__.replace('.py', '.svg')

pl = Plot3D(plot_array=False, plot_name=True)

i = Vector([1, 0, 0], name='i')
j = Vector([0, 1, 0], name='j')
k = Vector([0, 0, 1], name='k')
vectors = Vectors(i, j, k, i + j, i + k, j + k, i + j + k)
ax = pl.plot_vectors(vectors)
xyplane = Plane.from_points([0, 0, 0], [1, 0, 0], [0, 1, 0])
xzplane = Plane.from_points([0, 0, 0], [1, 0, 0], [0, 0, 1])
yzplane = Plane.from_points([0, 0, 0], [0, 1, 0], [0, 0, 1])
xyplane.plot_3d(ax, lims_x=[0, 1], lims_y=[0, 1], alpha=0.5)
xzplane.plot_3d(ax, lims_x=[0, 1], lims_y=[0, 1], alpha=0.5)
yzplane.plot_3d(ax, lims_x=[0, 1], lims_y=[0, 1], alpha=0.5)
pl.ax.view_init(elev=35, azim=-10, roll=0)

pl.savefig(ans_path)
pl.show()
