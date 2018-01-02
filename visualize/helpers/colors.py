import matplotlib.pylab as pl
import numpy as np

def color_list(length):
    colors =  pl.cm.rainbow(np.linspace(1,0, length))*255
    # convert to Hex to prevent legend bug in matplotlib. It won't show legend for line colors as array/tuple/list
    colors = ["#{0:02x}{1:02x}{2:02x}".format(int(color[0]), int(color[1]), int(color[2])) for color in colors]
    return colors