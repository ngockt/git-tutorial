from libs.geometryobjects import Vector
from libs.plots import Plot2D

ans_path = __file__.replace('.py', '.svg')

pl = Plot2D(plot_name=True, plot_array=True)
v = Vector([2, 1], name='v')
w = Vector([1, 2], name='w')
pl.plot_vectors(v, w, 3 * v + w)
pl.savefig(ans_path)
pl.show()
