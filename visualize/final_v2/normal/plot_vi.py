import matplotlib.pyplot as plt

from visualize.helpers.data import filter_data
from visualize.helpers.plot import save_file, set_plot


def plot_vi_all(data, reactor):
    """
    Plot voltage and current waveform. General function for plot_vi() and plot_vi_zoom()

    :param data:
    :param reactor:
    :return:
    """
    data = filter_data(data, input_f=10, input_l=1)[0]
    x_axis = data['output_t'][0]*1e6
    v_axis = data['output_v'][0]/1e3
    i_axis = data['output_c'][0]

    fig, ax1 = plt.subplots()

    ax1.plot(x_axis, i_axis, 'b-')

    ax1.set_ylabel('current [A]', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(x_axis, v_axis, 'r-')  # voltage

    ax2.set_ylabel('voltage [kV]', color='r')

    ax2.tick_params('y', colors='r')
    set_plot(fig, pulse=True, subplot=False)
    return fig


def plot_vi(data, reactor):
    """
    Plot voltage and current waveform, full pulse.

    :param data:
    :param reactor:
    :return:
    """
    fig = plot_vi_all(data, reactor)
    save_file(fig, name='vi-'+reactor, path='plots_final_v2/normal')


def plot_vi_zoom(data, reactor):
    """
    Plot voltage and current waveform, zoomed to the rising edge.

    :param data:
    :param reactor:
    :return:
    """
    fig = plot_vi_all(data, reactor)
    ax1 = fig.axes[0]
    ax1.set_xlim([-0.02, 0.25])
    ax1.set_ylim(-1, 12)
    # ax2.set_ylim(0,20)
    # align_y_axis(ax1, ax2, 1, 1)
    save_file(fig, name='vi-zoom-' + reactor, path='plots_final_v2/normal')