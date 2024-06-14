
from libs.geometryobjects import Vector
from libs.plots import Plot2D
from utils.misc import clear_terminal

clear_terminal()

pl = Plot2D(plot_array=True, plot_name=True)
u = Vector([3, 1], 'v')
v = Vector([-1, 1], 'v')
w = Vector([-2, -2], 'w')

pl.plot_a_vector(v, u)
pl.plot_a_vector(w, v)
pl.plot_a_vector(u, w)

pl.savefig(__file__.replace('.py', '.svg'))
pl.show()
