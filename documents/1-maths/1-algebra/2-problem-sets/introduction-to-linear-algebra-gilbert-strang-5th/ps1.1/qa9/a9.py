from libs.geometryobjects import Vector
from libs.plots import Plot2D

ans_path = __file__.replace('.py', '.svg')
pl = Plot2D(plot_name=True, plot_array=True)
v1 = Vector((1, 1), name='v1')
v2 = Vector((4, 2), name='v2')
v3 = Vector((1, 3), name='v3')
v2v1 = v1 - v2
v2v3 = v3 - v2
v4 = v2 + v2v1 + v2v3
v4.set_name('v4')
pl.plot_vectors(v1, v2, v3, v4)
pl.savefig(ans_path)
pl.show()
