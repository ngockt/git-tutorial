from libs.geometryobjects import Vector
from libs.plots import Plot2D

ans_path = __file__.replace('.py', '.svg')
pl = Plot2D(plot_name=True, plot_array=True)
v1 = Vector([4, 1], name='v')
v2 = Vector([2, -2], name='w')
pl.plot_vectors(v1, v2, [v1 + v2, v1 - v2])
pl.savefig(ans_path)
pl.show()
