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
    fig = plot_x_ppm(data, 'output_v_pulse', freqs, plt_yield=False)
    # fig.axes[1].set_xlabel('Pulse voltage [kV]')
    set_plot(fig, plot_height=0.8)
    save_file(fig, name='v-ppm-'+reactor, path='plots_poster/normal')
