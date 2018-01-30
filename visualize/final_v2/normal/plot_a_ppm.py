import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickles, filter_data, get_values, sort_data
from visualize.helpers.plot import set_plot, interpolate_plot, save_file, markers
from visualize.final_v2.normal.plot_x_ppm import plot_x_ppm


def plot_a_ppm(data, reactor, freqs):
    """
    Plot ppm to airflow

    :param data:
    :param reactor: long or short glass reactor
    :return:
    """
    data = filter_data(data, input_l=1) # values with l=0.5us are not correct measured.
    data = sort_data(data, key='airflow_lm')
    fig = plot_x_ppm(data, reactor, 'airflow_lm', freqs)
    fig.axes[0].set_xlabel('Airflow [$l_s/minute$]')
    set_plot(fig)
    save_file(fig, name='a-ppm-'+reactor, path='plots_final_v2')


if __name__ == '__main__':
    data = []
    reactor = 'short-glass'
    # reactor = 'long-glass'
    plot_a_ppm()
    plt.show()