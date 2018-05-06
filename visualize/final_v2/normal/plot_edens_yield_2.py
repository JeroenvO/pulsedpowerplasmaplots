import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.colors import color_plasma_3
from visualize.helpers.data import filter_data, reactor_inducance_index
from visualize.helpers.data import get_values
from visualize.helpers.plot import save_file, set_plot, set_unique_legend, markers, interpolate_plot, interpolate
from analyze.defines import *

def plot_edens_yield(data):
    """
    Make various plots to energy density with errorbars

    :param data:
    :param reactor:
    :return:
    """
    data = filter_data(data, input_v_output=15e3, input_l=1, output_yield_gkwh__gt=25, output_energy_dens__lt=190)
    fig, ax = plt.subplots(5, 1, sharex=True)
    colors = color_plasma_3
    # m = 'o'

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
        m = markers[i]
        edens = line['output_energy_dens']
        ax[0].scatter(edens, line['output_yield_gkwh'], label=l, c=c, marker=m)
        # ax_freq[0].scatter(freq, line['input_yield_gkwh'])

        ax[1].scatter(edens, line['o3_ppm'], label=l, c=c, marker=m)


        ax[2].scatter(edens, line['e_eff']*100, label=l, c=c, marker=m)


        ax[3].scatter(edens, line['input_f'], label=l, c=c, marker=m)


    # energy per pulse
    datas = data # save
    for reactor, ind in [(REACTOR_GLASS_LONG, 26), (REACTOR_GLASS_SHORT_QUAD, 0), (REACTOR_GLASS_SHORT_QUAD, 26)]:
        data = filter_data(datas, reactor=reactor, inductance=ind)
        if ind:
            name = reactor + '-' + str(ind) + 'uH'
        else:
            name = reactor + '-nocoil'
        i = reactor_inducance_index(reactor, ind)
        l = reactor + ' ' + (str(ind) + '$\,\mu H$' if ind else 'no coil')
        c = colors[i]
        m = markers[i]

        uf = np.unique(get_values(data, 'input_f'))
        center = []
        # mins = []
        # maxs = []
        std = []
        xs = []
        for f in uf:
            d = filter_data(data, input_f=f)
            l = get_values(d, key='output_e_plasma_single')  # returns list of arrays with values.
            if len(l) == 1:
                continue  # dont use single measurements, only double or triple
            v = np.concatenate(l)  # if multiple measurements, concat
            epuls = np.array(v) * 1000  # array of values
            mn = np.mean(epuls)
            xs.append(np.mean((get_values(d, key='output_energy_dens'))))
            # mins.append(mn - min(epuls))
            # maxs.append(max(epuls) - mn)
            std.append(np.std(epuls))
            center.append(mn)
        ax[4].scatter(xs, center, c=c, marker=m)
        ax[4].errorbar(xs, center, yerr=std, xerr=None, ecolor=c, capsize=3)

    ax[0].set_ylabel('Yield [g/kWh]')
    # ax[1].set_ylabel('Production [g/h]')
    # ax_dens[1].set_ylim([0, 7e-5])
    # ax_dens[2].set_ylim([0, 2e3])
    # ax[0].set_ylim([0, 120])
    ax[1].set_ylabel('Ozone [ppm]')
    ax[2].set_ylabel('Energy efficiency [%]')
    ax[3].set_ylabel('Frequency [Hz]')
    ax[4].set_ylabel('Pulse plasma energy [mJ]')
    ax[4].set_xlabel('Energy density [J/l]')

    set_unique_legend(ax[0])
    set_plot(fig, plot_height=4)
    save_file(fig, name='edens-all', path='plots_final_v2/normal')


if __name__ == '__main__':
    pass
