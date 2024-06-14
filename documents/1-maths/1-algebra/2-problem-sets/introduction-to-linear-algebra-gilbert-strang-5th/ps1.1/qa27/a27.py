import numpy as np
from skspatial.objects import Line, Points

from libs.plots import Plot3D
from utils.misc import clear_terminal

clear_terminal()

cube1 = Points([
    [0, 0, 0],  # 0
    [1, 0, 0],  # 1
    [0, 1, 0],  # 2
    [0, 0, 1],  # 3
    [1, 1, 0],  # 4
    [0, 1, 1],  # 5
    [1, 0, 1],  # 6
    [1, 1, 1],  # 7
])
cube2 = Points(cube1.to_array()*2)
cube1 = Points(cube1.to_array() + np.array([0.5]*3))
print(cube2)


ln_idx = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 6), (2, 4), (2, 5), (3, 5), (3, 6), (4, 7), (5, 7), (6, 7)]
pl = Plot3D(plot_array=False, plot_name=True)
for i0, i1 in ln_idx:
    ln = Line.from_points(cube1[i0], cube1[i1])
    ln.plot_3d(pl.ax, color='blue')
    ln = Line.from_points(cube2[i0], cube2[i1])
    ln.plot_3d(pl.ax, color='green')

cube1.plot_3d(pl.ax, color='blue')
cube2.plot_3d(pl.ax, color='green')

for p1, p2 in zip(cube1, cube2):
    ln = Line.from_points(p1, p2)
    ln.plot_3d(pl.ax, linestyle='dashed')

pl.savefig(__file__.replace('.py', '.svg'))
pl.show()
