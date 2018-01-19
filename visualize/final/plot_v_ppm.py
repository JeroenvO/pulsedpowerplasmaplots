import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickles, filter_data, get_values, sort_data
from visualize.helpers.plot import set_plot, interpolate_plot, save_file, markers


def plot_v_ppm(data, reactor):
    """
    Plot ppm to applied pulse voltage

    :param data: NOT USED
    :param reactor: long or short glass reactor
    :return:
    """
    data = []
    if reactor == 'long-glass':
        # data += load_pickles('20180103-1000hz')
        data += load_pickles('20180104-100hz')
        data += load_pickles('20180104-500hz')
        # data += load_pickle("20180105-freq/run1-1us/data.pkl")
        # data += load_pickle('20180115/run5/data.pkl')
    elif reactor == 'short-glass':
        # add synthetic zero point
        data = [{'input_f': 100, 'input_l': 1, 'output_v_pulse': 12e3, 'o3_ppm': 0},
                {'input_f': 500, 'input_l': 1, 'output_v_pulse': 12e3, 'o3_ppm': 0},]
        data += load_pickles('20180111')

    freqs = [100, 500]

    data = filter_data(data, input_l=1) # values with l=0.5us are not correct measured.
    data = sort_data(data, key='output_v_pulse')

    fig, ax = plt.subplots()
    c = 'black'
    marker_legends = []
    for i, f in enumerate(freqs):
        m = markers[i]
        d = filter_data(data, input_f=f)
        x = get_values(d, 'output_v_pulse')/1000
        y = get_values(d, 'o3_ppm')
        interpolate_plot(ax, x, y) #, kind='linear'
        for x, y in zip(x, y):
            ax.scatter(x, y, c=c, marker=m)
        marker_legends.append(mlines.Line2D([], [], marker=m, label=str(f)+'Hz', color='grey', markerfacecolor='black', markeredgewidth=0))

    plt.ylabel('Concentration [PPM]')
    plt.xlabel('Pulse voltage [kV]')

    plt.legend(handles=marker_legends, loc='upper left')

    set_plot(fig)

    save_file(fig, name='v-ppm-'+reactor, path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final')


if __name__ == '__main__':
    data = []
    reactor = 'short-glass'
    # reactor = 'long-glass'
    plot_v_ppm(data, reactor)