import matplotlib.pyplot as plt

from visualize.final_v2.normal.plot_x_ppm import plot_x_ppm
from visualize.helpers.data import load_pickles, filter_data, sort_data
from visualize.helpers.plot import set_plot, save_file


def plot_l_ppm(data, reactor, voltage=1000, freqs=[400]):
    """
    Plot ppm to pulse length

    :param data: NOT USED
    :param reactor: long-glass or short-glass
    :param voltage: voltage to plot pulsewidth
    :return:
    """

    data = filter_data(data, input_v=voltage, reactor=reactor)
    data = sort_data(data, key='input_l')
    if voltage != 1000:
        data = filter_data(data, input_l__le=20)  # don't plot 40us point
    fig = plot_x_ppm(data, 'input_l', freqs) #, plt_yield=True)
    fig.axes[0].set_xlabel('Pulse length [$\mathrm{\mu}$s]')
    fig.axes[0].set_xscale('log')
    set_plot(fig, plot_height=1)
    if voltage != 1000:
        reactor += '-'+str(voltage)

    save_file(fig, name='l-ppm-'+reactor, path='plots_poster/normal')


if __name__ == '__main__':
    data = []
    reactor = 'short-glass'
    # reactor = 'long-glass'
    data = []
    if reactor == 'long-glass':
        data += load_pickles('20180103-1000hz')
        data += load_pickles('20180104-100hz')
        data += load_pickles('20180104-500hz')
        # data += load_pickle("20180105-freq/run1-1us/data.pkl")
        # data += load_pickle('20180115/run5/data.pkl')
        freqs = [100, 500, 1000]

    elif reactor == 'short-glass':
        # add synthetic zero point
        # data = [{'input_f': 100, 'input_l': 1, 'output_v_pulse': 12e3, 'o3_ppm': 0},
        #         {'input_f': 500, 'input_l': 1, 'output_v_pulse': 12e3, 'o3_ppm': 0},]
        # data += load_pickle('20180110-lf-sweep/run2')
        # data += load_pickle('20180110-lf-sweep/run3')
        # data += load_pickle('20180110-lf-sweep/run4')
        data = load_pickles('20180130-l')
        freqs = [1000, 400]
    plot_l_ppm(data, reactor, 1000, freqs)
    plt.show()
