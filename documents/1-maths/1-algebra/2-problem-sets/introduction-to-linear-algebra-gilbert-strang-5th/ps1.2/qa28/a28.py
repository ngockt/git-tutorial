# Answer 28 code

from skspatial.objects import Line

from libs.geometryobjects.vectors import Vector
from libs.plots import Plot2D

ans_file_path = __file__.replace('.py', '.svg')

vectors = [
    Vector((1, 2), name='v'),
    *[Vector((1-2*c, c+2), 'w') for c in range(-5, 5)]
]

pl = Plot2D(plot_name=True, plot_array=True)
ln = Line.from_points(vectors[1], vectors[-1])
pl.plot_vectors(vectors)
pl.plot_line(ln)
pl.savefig(ans_file_path)
pl.show()
