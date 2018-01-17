import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickle, filter_data, get_values
from visualize.helpers.plot import save_file, set_plot, interpolate_plot


def plot_edens_yield(data, reactor):
    data = filter_data(data, input_v_output=15e3, input_l=1)

    fig, ax = plt.subplots(5, 1, sharex=True)

    x = get_values(data, 'output_energy_dens')

    interpolate_plot(ax[0], x, get_values(data, 'output_yield_gkwh'))
    interpolate_plot(ax[1], x, get_values(data, 'o3_gramsec')*3600)
    interpolate_plot(ax[2], x, get_values(data, 'o3_ppm'))
    interpolate_plot(ax[3], x, get_values(data, 'input_p'))
    interpolate_plot(ax[3], x, get_values(data, 'output_p_avg'))
    interpolate_plot(ax[4], x, get_values(data, 'input_f'))

    m = 'o'
    l = 'output'
    c = 'black'
    for line in data:
        edens = line['output_energy_dens']
        ax[0].scatter(edens, line['output_yield_gkwh'], label=l, c=c, marker=m)
        # ax_freq[0].scatter(freq, line['input_yield_gkwh'])

        ax[1].scatter(edens, line['o3_gramsec']*3600, label=l, c=c, marker=m)
        # ax_freq[1].scatter(freq, line['o3_gramsec'])

        ax[2].scatter(edens, line['o3_ppm'], label=l, c=c, marker=m)

        ax[3].scatter(edens, line['output_p_avg'], label=l, c=c, marker=m)
        ax[3].scatter(edens, line['input_p'], label=l, c=c, marker='D')

        ax[4].scatter(edens, line['input_f'], label=l, c=c, marker=m)

    marker_legends = [
        mlines.Line2D([], [], marker='D', label='input power', color='grey', markerfacecolor='black', markeredgewidth=0),
        mlines.Line2D([], [], marker='o', label='plasma power', color='grey', markerfacecolor='black',markeredgewidth=0),
    ]
    lgd2 = ax[3].legend(handles=marker_legends, loc='upper left')

    ax[0].set_ylabel('Yield [g/kWh]')
    ax[1].set_ylabel('Production [g/h]')
    # ax_dens[1].set_ylim([0, 7e-5])
    # ax_dens[2].set_ylim([0, 2e3])
    ax[0].set_ylim([0, 120])
    ax[2].set_ylabel('Concentration [PPM]')
    ax[3].set_ylabel('Power [W]')
    ax[4].set_ylabel('Frequency [Hz]')
    ax[4].set_xlabel('Energy density [J/l]')
    set_plot(fig, plot_height=5)
    save_file(fig, name='edens-'+reactor, path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final')


if __name__ == '__main__':
    reactors = ['long-glass-46uH', 'long-glass-26uH', 'short-glass-nocoil', 'short-glass-26uH', 'short-glass-8uH']
    reactor = reactors[1]
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
    plot_edens_yield(data, reactor)
