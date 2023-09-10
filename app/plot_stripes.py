from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection

from utils import FIRST,LAST

def get_stripes_collection(
        data_array,
        cmap,
        clim_min,
        clim_max,
        y0 = 0, height = 1,
        ):

    col = PatchCollection([
        Rectangle((x, y0), 1, height)
        for x in range(FIRST, LAST + 1)
        ])

    # set data, colormap and color limits
    col.set_array(data_array)
    col.set_cmap(cmap)
    col.set_clim(clim_min, clim_max)

    return col