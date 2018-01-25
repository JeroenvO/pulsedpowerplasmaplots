import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.data import load_pickle, filter_data, get_values
from visualize.helpers.plot import save_file, set_plot, set_unique_legend, interpolate_plot
from visualize.helpers.colors import color_viridis
from visualize.helpers.burst import calc_burst

def plot_f_epulse(datas):
    """
    Plots energy per pulse for various frequencies as boxplot

    :param data:
    :param reactor:
    :return:
    """
    colors = color_viridis(len(datas))
    fig, ax = plt.subplots()
    for i, data in enumerate(datas):
        data = filter_data(data, input_v_output=15e3, input_l=1)
        l = str(data[0]['burst_inner_f']) + ' kHz, ' + str(data[0]['burst_pulses']) + ' pulses'
        c = colors[i]
        interpolate_plot(ax, range(1,1+len(data)), get_values(data, 'output_e_plasma')*1000)
        for j, line in enumerate(data):
            epuls = line['output_e_plasma']*1000  # array of values, to mJ.
            plt.scatter(j+1, epuls, label=l, c=c)

    # add x labels
    ax.set_xlabel('Pulse number')
    ax.set_ylabel('Pulse plasma energy [mJ]')
    set_unique_legend(ax)
    set_plot(fig, plot_height=1.5)
    save_file(fig, name='epulse-burst-all', path='plots_final_v2')