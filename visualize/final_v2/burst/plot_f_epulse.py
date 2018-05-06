import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.colors import color2
from visualize.helpers.data import filter_data, get_values
from visualize.helpers.plot import markers
from visualize.helpers.plot import save_file, set_plot, interpolate_plot


def plot_f_epulse(datas):
    """
    Plots energy per pulse for various frequencies
    5 pulses, 100hz

    :param data:
    :param reactor:
    :return:
    """
    fig, ax = plt.subplots()
    marker_legends = []

    for i, data in enumerate(datas):
        data = filter_data(data, input_v_output=15e3, input_l=1)
        # l = str(data[0]['burst_inner_f']) + ' kHz, ' + str(data[0]['burst_pulses'])
        c = color2[i]
        center = get_values(data, 'output_e_plasma')*1000
        all = [np.array(list)*1000 for list in get_values(data, 'output_e_plasma_single')]
        x = range(1,1+len(data))
        interpolate_plot(ax, x, center)
        m = markers[i]

        for j, line in enumerate(data):
            epuls = line['output_e_plasma']*1000  # array of values, to mJ.
            plt.scatter(j+1, epuls, c=c, marker=m)

        marker_legends.append(
            mlines.Line2D([], [], marker=m, label=str(len(data))+' pulses', color='grey', markerfacecolor=c, markeredgewidth=0))

        # mi = [y2a - min(z2a) for z2a, y2a in zip(all, center)]  # list of minima of y
        # ma = [max(z2a) - y2a for z2a, y2a in zip(all, center)]  # list of maxima of y
        std = [np.std(z2a) for z2a in all]
        ax.errorbar(x, center, yerr=std, xerr=None, ecolor=c, fmt='none', capsize=3)

    # add x labels
    ax.set_xlabel('Pulse number')
    ax.set_ylabel('Pulse plasma energy [mJ]')
    ax.legend(handles=marker_legends)
    ax.set_xlim(left=0)
    set_plot(fig)
    save_file(fig, name='epulse-burst', path='plots_final_v2/burst')
