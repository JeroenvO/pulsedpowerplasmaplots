import matplotlib.pylab as pl
import matplotlib.pyplot as plt
import numpy as np

#
# def color_rainbow(length):
#     """
#     List of colors, in rainbow format.
#
#     :param length: length of list
#     :return: list of colors
#     """
#     colors = pl.cm.rainbow(np.linspace(1, 0, length)) * 255
#     # convert to Hex to prevent legend bug in matplotlib. It won't show legend for line colors as array/tuple/list
#     colors = ["#{0:02x}{1:02x}{2:02x}".format(int(color[0]), int(color[1]), int(color[2])) for color in colors]
#     return colors
#
#
# def color_viridis(length):
#     """
#     List of colors, in rainbow format.
#
#     :param length: length of list
#     :return: list of colors
#     """
#     colors = pl.cm.viridis(np.linspace(1, 0, length)) * 255
#     # convert to Hex to prevent legend bug in matplotlib. It won't show legend for line colors as array/tuple/list
#     colors = ["#{0:02x}{1:02x}{2:02x}".format(int(color[0]), int(color[1]), int(color[2])) for color in colors]
#     return colors

def color_plasma(length):
    """
    List of colors, in plasma format.

    :param length: length of list
    :return: list of colors
    """
    colors = pl.cm.plasma(np.linspace(1, 0, length)) * 255
    # convert to Hex to prevent legend bug in matplotlib. It won't show legend for line colors as array/tuple/list
    colors = ["#{0:02x}{1:02x}{2:02x}".format(int(color[0]), int(color[1]), int(color[2])) for color in colors]
    return colors
#
# prop_cycle = plt.rcParams['axes.prop_cycle']
# colors = prop_cycle.by_key()['color']
c8 = color_plasma(9)
# color2 = [c8[2], c8[8]]
color2 = ['xkcd:sky blue', 'xkcd:red']
color_plasma_3 = [c8[2], c8[5], c8[8]]