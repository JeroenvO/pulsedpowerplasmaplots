import matplotlib.pyplot as plt

from visualize.helpers.data import filter_data
from visualize.helpers.plot import save_file, set_plot
from visualize.helpers.colors import color2

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
    ax1.plot(x_axis, i_axis, color=color2[0])
    ax1.set_ylabel('Current [A]', color=color2[0])
    ax1.tick_params('y', colors=color2[0])

    ax2 = ax1.twinx()
    ax2.plot(x_axis, v_axis, color=color2[1])  # voltage
    ax2.set_ylabel('Voltage [kV]', color=color2[1])
    ax2.tick_params('y', colors=color2[1])
    ax2.xaxis.set_label_coords(-0.05, -0.07)
    ax1.xaxis.set_label_coords(-0.05, -0.07)
    set_plot(fig, pulse=True, subplot=False, plot_height=0.8)
    return fig


def plot_vi(data, reactor):
    """
    Plot voltage and current waveform, full pulse.

    :param data:
    :param reactor:
    :return:
    """
    fig = plot_vi_all(data, reactor)
    save_file(fig, name='vi-'+reactor, path='plots_poster/normal')


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
    save_file(fig, name='vi-zoom-' + reactor, path='plots_poster/normal')


if __name__ == '__main__':
    from visualize.helpers.data import load_pickle
    for reactor in ['long-glass', 'short-glass']:
        data = []
        if reactor == 'long-glass':  # 26uH, long glass,
            data = load_pickle('20180115-def1/run5')
        elif reactor == 'short-glass':
            data = load_pickle('20180115-def1/run1')
        plot_vi_zoom(data, reactor)
        plot_vi(data, reactor)
