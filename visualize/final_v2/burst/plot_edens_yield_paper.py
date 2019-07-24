import matplotlib.pyplot as plt
import numpy as np
from visualize.helpers.colors import color_plasma
from visualize.helpers.data import filter_data, reactor_inducance_index
from visualize.helpers.plot import save_file, set_plot, set_unique_legend
from visualize.helpers.burst import calc_burst


def plot_edens_yield(datas):
    """
    Make various plots to energy density

    :param datas:
    :return:
    """
    fig, ax = plt.subplots(2, 1, sharex=True)
    m = 'o'

    ui = np.array([200, 150, 100, 75, 50])
    offset = 1 # skip bright yellow color

    colors = color_plasma(len(ui)+offset)
    # sort data, to keep the legend in the right order.
    datas = sorted(datas, key=lambda x:x[0]['burst_inner_f'])

    for i, data in enumerate(datas):
        l = str(data[0]['burst_inner_f']) + ' kHz'
        data = filter_data(data, input_v_output=15e3, output_yield_gkwh__gt=25)
        c = colors[np.where(data[0]['burst_inner_f'] == ui)[0][0]+offset]
        burstdata = calc_burst(data)
        line = data[0] # because all data is the same in one burst run

        edens = burstdata['output_energy_dens']
        ax[1].scatter(edens, burstdata['output_yield_gkwh'], label=l, c=c, marker=m)

        ax[0].scatter(edens, line['o3_ppm'], label=l, c=c, marker=m)

    ax[1].set_ylabel('Yield [g/kWh]')
    # ax[1].set_ylabel('Production [g/h]')
    # ax_dens[1].set_ylim([0, 7e-5])
    # ax_dens[2].set_ylim([0, 2e3])
    # ax[0].set_ylim([0, 120])
    ax[0].set_ylabel('Ozone [ppm]')
    ax[0].text(20, 220, '50 Hz')
    ax[0].text(45, 250, '100 Hz')
    ax[0].text(85, 550, '200 Hz')
    ax[1].set_xlabel('Energy density [J/l]')
    set_unique_legend(ax[0])
    set_plot(fig, plot_height=2, from_zero=False)
    save_file(fig, name='edens-all-burst-paper', path='plots_final_v2/burst')


if __name__ == '__main__':
    pass
