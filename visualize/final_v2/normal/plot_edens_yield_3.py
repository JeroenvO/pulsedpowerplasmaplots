import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.colors import color_plasma_3
from visualize.helpers.data import filter_data, reactor_inducance_index
from visualize.helpers.data import get_values, sort_data
from visualize.helpers.plot import save_file, set_plot, set_unique_legend, markers, interpolate_plot, interpolate
from analyze.defines import *

def plot_edens_yield(data):
    """
    Make various plots to energy density, with regression lines

    :param data:
    :param reactor:
    :return:
    """
    data = filter_data(data, input_v_output=15e3, input_l=1, output_yield_gkwh__gt=25, output_energy_dens__lt=190)
    fig, ax = plt.subplots(5, 1, sharex=True)
    colors = color_plasma_3

    # energy per pulse
    datas = data # save
    for reactor, ind in [(REACTOR_GLASS_LONG, 26), (REACTOR_GLASS_SHORT_QUAD, 0), (REACTOR_GLASS_SHORT_QUAD, 26)]:
        data = filter_data(datas, reactor=reactor, inductance=ind)
        i = reactor_inducance_index(reactor, ind)
        l = reactor + ' ' + (str(ind) + '$\,\mu H$' if ind else 'no coil')
        c = colors[i]
        m = markers[i]
        data = sort_data(data, key='output_energy_dens')
        edens = get_values(data, 'output_energy_dens')


        y = get_values(data, 'o3_ppm')
        ax[0].scatter(edens, y, label=l, c=c, marker=m)
        fit = np.polyfit(edens, y, 3)
        fit_fn = np.poly1d(fit)
        ax[0].plot(edens, fit_fn(edens), '--', c=c, lw=0.9)

        y = get_values(data, 'output_yield_gkwh')
        ax[1].scatter(edens, y, label=l, c=c, marker=m)
        fit = np.polyfit(edens, y, 3)
        fit_fn = np.poly1d(fit)
        ax[1].plot(edens, fit_fn(edens), '--', c=c, lw=0.9)

        y=get_values(data, 'input_f')
        ax[2].scatter(edens, y, label=l, c=c, marker=m)
        fit = np.polyfit(edens, y, 3)
        fit_fn = np.poly1d(fit)
        ax[2].plot(edens, fit_fn(edens), '--', c=c, lw=0.9)

        y= get_values(data, 'output_e_plasma')*1000
        ax[3].scatter(edens, y, c=c, marker=m)
        fit = np.polyfit(edens, y, 3)
        fit_fn = np.poly1d(fit)
        ax[3].plot(edens, fit_fn(edens), '--', c=c, lw=0.9)

        y = get_values(data, 'e_eff')* 100
        ax[4].scatter(edens,  y , label=l, c=c, marker=m)
        fit = np.polyfit(edens, y, 2)
        fit_fn = np.poly1d(fit)
        ax[4].plot(edens, fit_fn(edens), '--', c=c, lw=0.9)

    ax[1].set_ylabel('Yield [g/kWh]')
    # ax[1].set_ylabel('Production [g/h]')
    # ax_dens[1].set_ylim([0, 7e-5])
    # ax_dens[2].set_ylim([0, 2e3])
    # ax[0].set_ylim([0, 120])
    ax[0].set_ylabel('Ozone [ppm]')
    ax[4].set_ylabel('Energy efficiency [%]')
    ax[2].set_ylabel('Frequency [Hz]')
    ax[3].set_ylabel('Pulse plasma energy [mJ]')
    ax[3].set_ylim([1, 15])
    ax[4].set_xlabel('Energy density [J/l]')

    set_unique_legend(ax[0])
    set_plot(fig, plot_height=4)
    save_file(fig, name='edens-all-3', path='plots_final_v2/normal')


if __name__ == '__main__':
    pass