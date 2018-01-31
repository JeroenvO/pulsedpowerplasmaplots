import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.colors import color_viridis
from visualize.helpers.data import filter_data, get_values
from visualize.helpers.plot import save_file, set_plot, set_unique_legend, interpolate_plot


def plot_f_epulse(datas):
    """
    Plots energy per pulse for various frequencies as boxplot

    :param data:
    :param reactor:
    :return:
    """

    fig, ax = plt.subplots()
    ui = np.array([200,150,100,75,50])
    colors = color_viridis(len(ui))

    for i, data in enumerate(datas):
        data = filter_data(data, input_v_output=15e3, input_l=1)
        l = str(data[0]['burst_inner_f']) + ' kHz, ' + str(data[0]['input_l']) + ' $\mu$s'
        c = colors[np.where(data[0]['burst_inner_f'] == ui)[0][0]]
        if data[0]['burst_f'] == 50:
            m = '.'
        elif data[0]['burst_f'] == 100:
            m = '+'
        elif data[0]['burst_f'] == 200:
            m = '*'
        else:
            raise Exception('Invalid burst f')

        interpolate_plot(ax, range(1,1+len(data)), get_values(data, 'output_e_plasma')*1000)
        for j, line in enumerate(data):
            epuls = line['output_e_plasma']*1000  # array of values, to mJ.
            plt.scatter(j+1, epuls, label=l, c=c, marker=m)

    # add x labels
    ax.set_xlabel('Pulse number')
    ax.set_ylabel('Pulse plasma energy [mJ]')
    set_unique_legend(ax, bbox_to_anchor=(0.5, -0.2))
    set_plot(fig, plot_height=2)
    save_file(fig, name='epulse-burst-all', path='plots_final_v2/burst')