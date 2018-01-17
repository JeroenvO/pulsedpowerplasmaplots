import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.data import load_pickle, filter_data, get_values
from visualize.helpers.plot import save_file, set_plot

def plot_edens_epulse(data, reactor):
    data = filter_data(data, input_v_output=15e3, input_l=1)

    fig, ax = plt.subplots()

    plotdata = []
    for line in data:
        epuls = np.array(line['output_e_plasma_single'])*1000
        plotdata.append(epuls)

    plt.boxplot(plotdata)
    plt.xticks(list(range(len(data)+1)), ['']+list(get_values(data, 'input_f')))
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Pulse plasma energy [mJ]')
    set_plot(fig)
    save_file(fig, name='epulse-'+reactor, path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final')


if __name__ == '__main__':
    reactors = ['long-glass-46uH', 'long-glass-26uH', 'short-glass-nocoil', 'short-glass-26uH', 'short-glass-8uH']
    reactor = reactors[3]
    print(reactor)
    if reactor == 'long-glass-46uH':
        data = load_pickle("20180115/run6")
    elif reactor == 'long-glass-26uH':
        data = load_pickle("20180115/run5")
    elif reactor == 'short-glass-26uH':
        data = load_pickle("20180115/run2")
    elif reactor == 'short-glass-8uH':
        data = load_pickle("20180115/run3")
    elif reactor == 'short-glass-nocoil':
        data = load_pickle("20180115/run1")
    else:
        raise Exception("No input!")
    plot_edens_epulse(data, reactor)
