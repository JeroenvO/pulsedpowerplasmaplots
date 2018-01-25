import matplotlib.pyplot as plt

from visualize.helpers.colors import color_viridis
from visualize.helpers.data import filter_data, reactor_inducance_index
from visualize.helpers.plot import save_file, set_plot


def plot_edens_yield(data):
    """
    Make various plots to energy density

    :param data:
    :param reactor:
    :return:
    """
    data = filter_data(data, input_v_output=15e3, input_l=1, output_yield_gkwh__gt=25)
    fig, ax = plt.subplots(4, 1, sharex=True)
    colors = color_viridis(3)
    m = 'o'

    # interpolate_plot(ax[0], x, get_values(data, 'output_yield_gkwh'))
    # interpolate_plot(ax[1], x, get_values(data, 'o3_gramsec')*3600)
    # interpolate_plot(ax[2], x, get_values(data, 'o3_ppm'))
    # interpolate_plot(ax[3], x, get_values(data, 'input_p'))
    # interpolate_plot(ax[3], x, get_values(data, 'output_p_avg'))
    # interpolate_plot(ax[4], x, get_values(data, 'input_f'))

    for line in data:
        reactor = line['reactor']
        inductance = line['inductance']
        i = reactor_inducance_index(reactor, inductance)
        l = reactor + ' ' + (str(inductance)+'$\,\mu H$' if inductance else 'no coil')
        c = colors[i]
        edens = line['output_energy_dens']
        ax[0].scatter(edens, line['output_yield_gkwh'], label=l, c=c, marker=m)
        # ax_freq[0].scatter(freq, line['input_yield_gkwh'])

        ax[1].scatter(edens, line['o3_ppm'], label=l, c=c, marker=m)

        ax[2].scatter(edens, line['e_eff']*100, label=l, c=c, marker=m)

        ax[3].scatter(edens, line['input_f'], label=l, c=c, marker=m)

    ax[0].set_ylabel('Yield [g/kWh]')
    # ax[1].set_ylabel('Production [g/h]')
    # ax_dens[1].set_ylim([0, 7e-5])
    # ax_dens[2].set_ylim([0, 2e3])
    # ax[0].set_ylim([0, 120])
    ax[1].set_ylabel('Concentration [PPM]')
    ax[2].set_ylabel('Energy efficiency [%]')
    ax[3].set_ylabel('Frequency [Hz]')
    ax[3].set_xlabel('Energy density [J/l]')

    from collections import OrderedDict

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    ax[1].legend(by_label.values(), by_label.keys())

    set_plot(fig, plot_height=3)
    save_file(fig, name='edens-all', path='plots_final_v2')


if __name__ == '__main__':
    pass