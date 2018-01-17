import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickles, filter_data, get_values
from visualize.helpers.plot import set_plot, interpolate_plot, save_file


def plot_v_ppm(data, reactor):
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

    data = filter_data(data, input_l=1) # values with l=0.5us are not correct measured.

    data_100 = filter_data(data, input_f=100)
    data_500 = filter_data(data, input_f=500)

    fig, ax = plt.subplots()

    c = 'black'

    x_100 = get_values(data_100, 'output_v_pulse')/1000
    y_100 = get_values(data_100, 'o3_ppm')
    interpolate_plot(ax, x_100, y_100)
    for x, y in zip(x_100, y_100):
        ax.scatter(x, y, c=c, marker='o', label='100Hz')

    x_500 = get_values(data_500, 'output_v_pulse')/1000
    y_500 = get_values(data_500, 'o3_ppm')
    interpolate_plot(ax, x_500, y_500)
    for x, y in zip(x_500, y_500):
        ax.scatter(x, y, c=c, marker='d', label='500Hz')

    plt.ylabel('Concentration [PPM]')
    plt.xlabel('Pulse voltage [kV]')

    marker_legends = [mlines.Line2D([], [], marker='o', label='100Hz', color='grey', markerfacecolor='black', markeredgewidth=0),
                      mlines.Line2D([], [], marker='D', label='500Hz', color='grey', markerfacecolor='black', markeredgewidth=0)]
    lgd2 = plt.legend(handles=marker_legends, loc='upper left')

    set_plot(fig)
    save_file(fig, name='v-ppm-'+reactor, path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final')


if __name__ == '__main__':
    data = []
    reactor = 'short-glass'
    # reactor = 'long-glass'
    plot_v_ppm(data, reactor)