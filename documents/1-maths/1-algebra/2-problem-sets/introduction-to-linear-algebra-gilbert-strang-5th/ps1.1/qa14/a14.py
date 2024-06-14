import numpy as np

from libs.geometryobjects import Vector
from libs.plots import Plot2D

ans_path = __file__.replace('.py', '.svg')
pl = Plot2D(plot_name=True, plot_array=False)

vectors = []
vsum = Vector([0, 0], 'zero')
for theta in range(0, 360, 30):
    name = theta
    theta = theta / 360 * 2 * np.pi
    vectors.append(
        Vector(
            [np.cos(theta).round(2), np.sin(theta).round(2)],
            name=str(name)
        ) + Vector([0, 1], 'j')
    )
    vsum = vsum + vectors[-1]

vsum.set_name('sum')
vectors.append(vsum)
pl.plot_vectors(vectors)

pl.savefig(ans_path)
pl.show()
