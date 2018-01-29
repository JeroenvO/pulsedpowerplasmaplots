import matplotlib.pyplot as plt
import numpy as np
from visualize.helpers.colors import color_viridis
from visualize.helpers.data import filter_data, reactor_inducance_index
from visualize.helpers.plot import save_file, set_plot, set_unique_legend
from visualize.helpers.burst import calc_burst


def plot_edens_yield(datas):
    """
    Make various plots to energy density

    :param data:
    :param reactor:
    :return:
    """

    fig, ax = plt.subplots(3, 1, sharex=True)
    m = 'o'

    # interpolate_plot(ax[0], x, get_values(data, 'output_yield_gkwh'))
    # interpolate_plot(ax[1], x, get_values(data, 'o3_gramsec')*3600)
    # interpolate_plot(ax[2], x, get_values(data, 'o3_ppm'))
    # interpolate_plot(ax[3], x, get_values(data, 'input_p'))
    # interpolate_plot(ax[3], x, get_values(data, 'output_p_avg'))
    # interpolate_plot(ax[4], x, get_values(data, 'input_f'))

    ui = np.array([200, 150, 100, 75, 50])
    colors = color_viridis(len(ui))

    # sort data, to keep the legend in the right order.
    datas = sorted(datas, key=lambda x:x[0]['burst_inner_f'])

    for i, data in enumerate(datas):
        l = str(data[0]['burst_inner_f']) + ' kHz'
        data = filter_data(data, input_v_output=15e3, input_l=1, output_yield_gkwh__gt=25)
        c = colors[np.where(data[0]['burst_inner_f'] == ui)[0][0]]
        burstdata = calc_burst(data)
        line = data[0] # because all data is the same in one burst run

        edens = burstdata['output_energy_dens']
        ax[0].scatter(edens, burstdata['output_yield_gkwh'], label=l, c=c, marker=m)
        # ax_freq[0].scatter(freq, line['input_yield_gkwh'])

        ax[1].scatter(edens, line['o3_ppm'], label=l, c=c, marker=m)

        ax[2].scatter(edens, burstdata['e_eff']*100, label=l, c=c, marker=m)

        # ax[3].scatter(edens, line['input_f'], label=l, c=c, marker=m)

    ax[0].set_ylabel('Yield [g/kWh]')
    # ax[1].set_ylabel('Production [g/h]')
    # ax_dens[1].set_ylim([0, 7e-5])
    # ax_dens[2].set_ylim([0, 2e3])
    # ax[0].set_ylim([0, 120])
    ax[1].set_ylabel('Concentration [PPM]')
    ax[2].set_ylabel('Energy efficiency [%]')
    # ax[3].set_ylabel('Frequency [Hz]')
    ax[2].set_xlabel('Energy density [J/l]')
    ax[1].text(20, 220, '50 Hz')
    ax[1].text(45, 250, '100 Hz')
    ax[1].text(85, 550, '200 Hz')
    set_unique_legend(ax[1])
    set_plot(fig, plot_height=3)
    save_file(fig, name='edens-all-burst', path='plots_final_v2')


if __name__ == '__main__':
    pass