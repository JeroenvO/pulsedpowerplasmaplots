import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.data import load_pickle, filter_data, get_values
from visualize.helpers.plot import save_file, set_plot


def plot_f_epulse(data, reactor):
    """
    Plots energy per pulse for various frequencies as boxplot

    :param data:
    :param reactor:
    :return:
    """
    data = filter_data(data, input_v_output=15e3, input_l=1)

    fig, ax = plt.subplots()
    uf = np.unique(get_values(data, 'input_f'))
    plotdata = []
    for f in uf:
        d = filter_data(data, input_f=f)
        l = get_values(d, key='output_e_plasma_single')  # returns list of arrays with values.
        v = np.concatenate(l)
        epuls = np.array(v)*1000  # array of values
        plotdata.append(epuls)

    plt.boxplot(plotdata)
    # add x labels
    num_boxes = len(uf)
    plt.xticks(range(num_boxes+1), ['']+list(uf), rotation=45)

    # add top x-labels with number of sample points
    upperLabels = [''] + [str(len(s)) for s in plotdata]
    ax2 = ax.twiny()
    ax2.set_xlim(ax.get_xlim())
    ax2.set_xticks(ax.get_xticks())
    ax2.set_xticklabels(upperLabels)
    ax2.set_xlabel("Number of samples")


    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Pulse plasma energy [mJ]')
    set_plot(fig, plot_height=1.4)
    save_file(fig, name='epulse-'+reactor, path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final_v1')


if __name__ == '__main__':
    reactors = ['long-glass-46uH', 'long-glass-26uH', 'short-glass-nocoil', 'short-glass-26uH', 'short-glass-8uH']
    reactor = reactors[3]
    print(reactor)
    if reactor == 'long-glass-46uH':
        data = load_pickle("20180115-def1/run6")
    elif reactor == 'long-glass-26uH':
        data = load_pickle("20180115-def1/run5")
    elif reactor == 'short-glass-26uH':
        data = load_pickle("20180115-def1/run2")
    elif reactor == 'short-glass-8uH':
        data = load_pickle("20180115-def1/run3")
    elif reactor == 'short-glass-nocoil':
        data = load_pickle("20180115-def1/run1")
    else:
        raise Exception("No input!")
    plot_f_epulse(data, reactor)
