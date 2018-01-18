import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickle, filter_data
from visualize.helpers.plot import save_file, set_plot


def plot_pe(data, reactor):
    """
    Plot power and energy waveform, in two subplots

    :param data:
    :param reactor:
    :return:
    """
    data = filter_data(data, input_v_output=15e3, input_f=10, input_l=1)[0]
    fig, ax = plt.subplots(2, 1, sharex=True)
    x_axis = data['output_t'][0]*1e6
    p_axis = data['output_p'][0]/1e3
    e_axis = data['output_e'][0]*1e3
    ax[0].plot(x_axis, p_axis, color='black')
    ax[1].plot(x_axis, e_axis, color='black')
    ax[0].set_ylabel('P [kW]')
    ax[1].set_ylabel('E [mJ]')
    set_plot(fig, 2, pulse=True)
    save_file(fig, name='pe-'+reactor, path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final')


if __name__ == '__main__':
    data = load_pickle('20180115/run1')
    plot_pe(data, 'short-glass')