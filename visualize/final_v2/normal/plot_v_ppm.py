import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickles, filter_data, get_values, sort_data
from visualize.helpers.plot import set_plot, interpolate_plot, save_file, markers
from visualize.final_v2.normal.plot_x_ppm import plot_x_ppm


def plot_v_ppm(data, reactor, freqs):
    """
    Plot ppm to applied pulse voltage

    :param data: NOT USED
    :param reactor: long or short glass reactor
    :return:
    """
    data = filter_data(data, input_l=1) # values with l=0.5us are not correct measured.
    fig = plot_x_ppm(data, 'output_v_pulse', freqs)
    fig.axes[0].set_xlabel('Pulse voltage [kV]')
    set_plot(fig)
    save_file(fig, name='v-ppm-'+reactor, path='plots_final_v2/normal')


if __name__ == '__main__':
    reactor = 'long-glass'
    data = filter_data(load_pickles('20180126-v-sweep'), input_f=400)
    data += filter_data(load_pickles('20180111-v-sweep'), input_f=100)
    data += filter_data(load_pickles('20180130-v-sweep'), input_f=100)
    data = filter_data(data, reactor=reactor, inductance=0, input_l=1)
    freqs = [100, 400]
    plot_v_ppm(data, reactor, freqs)
    plt.show()