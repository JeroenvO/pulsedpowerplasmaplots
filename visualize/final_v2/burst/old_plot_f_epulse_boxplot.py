import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.data import load_pickle, filter_data, get_values
from visualize.helpers.plot import save_file, set_plot
from visualize.helpers.colors import color_viridis
from visualize.helpers.burst import calc_burst

def plot_f_epulse(data, label):
    """
    Plots energy per pulse for various frequencies as boxplot

    :param data:
    :param reactor:
    :return:
    """
    fig, ax = plt.subplots()
    plotdata = []
    data = filter_data(data, input_v_output=15e3, input_l=1)
    for i, line in enumerate(data):
        l = line['output_e_plasma_single']  # returns list of arrays with values.
        epuls = np.array(l)*1000  # array of values, to mJ.
        plotdata.append(epuls)

    plt.boxplot(plotdata)
    # add x labels
    num_boxes = data[0]['burst_pulses']
    plt.xticks(range(num_boxes+1), ['']+list(range(1, num_boxes+1)))

    ax.set_xlabel('Pulse number')
    ax.set_ylabel('Pulse plasma energy [mJ]')
    set_plot(fig, plot_height=1.4)
    save_file(fig, name='epulse-burst-'+label, path='plots_final_v2')