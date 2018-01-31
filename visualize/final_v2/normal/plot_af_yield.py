import matplotlib.pyplot as plt

from visualize.helpers.colors import color_viridis
from visualize.helpers.data import filter_data, reactor_inducance_index, load_pickles, load_pickle, get_values
from visualize.helpers.plot import save_file, set_plot
import numpy as np

def plot_af_yield(data):

    fig, ax = plt.subplots(4, 1, sharex=True)

    uf = np.unique(get_values(data, 'input_f'))

    colors = color_viridis(len(uf))
    # m = 'o'
    data_f = data
    data_a = load_pickles('20180129-airf')

    # interpolate_plot(ax[0], x, get_values(data, 'output_yield_gkwh'))
    # interpolate_plot(ax[1], x, get_values(data, 'o3_gramsec')*3600)
    # interpolate_plot(ax[2], x, get_values(data, 'o3_ppm'))
    # interpolate_plot(ax[3], x, get_values(data, 'input_p'))
    # interpolate_plot(ax[3], x, get_values(data, 'output_p_avg'))
    # interpolate_plot(ax[4], x, get_values(data, 'input_f'))
    # c = colors[0]
    m = '*'
    for data in [data_a, data_f]:

        for line in data:
            l = ''
            c = colors[np.where(uf==line['input_f'])[0][0]]
            edens = line['output_energy_dens']
            ax[0].scatter(edens, line['output_yield_gkwh'], label=l, c=c, marker=m)
            # ax_freq[0].scatter(freq, line['input_yield_gkwh'])

            ax[1].scatter(edens, line['o3_ppm'], label=l, c=c, marker=m)

            ax[2].scatter(edens, line['e_eff'] * 100, label=l, c=c, marker=m)

            ax[3].scatter(edens, line['input_f'], label=l, c=c, marker=m)
        m = 'o'
    ax[0].set_ylabel('Yield [g/kWh]')
    # ax[1].set_ylabel('Production [g/h]')
    # ax_dens[1].set_ylim([0, 7e-5])
    # ax_dens[2].set_ylim([0, 2e3])
    # ax[0].set_ylim([0, 120])
    ax[1].set_ylabel('Concentration [PPM]')
    ax[2].set_ylabel('Energy efficiency [%]')
    ax[3].set_ylabel('Frequency [Hz]')
    ax[3].set_xlabel('Energy density [J/l]')

    set_plot(fig, plot_height=4)
    save_file(fig, name='edens-yield-short-glass', path='plots_final_v2/normal')


if __name__ == '__main__':
    datas = load_pickle('20180115-def1/run5')
    datas += load_pickle('20180118-def2/run1')
    datas += load_pickle('20180119-def3/run1')
    datas += load_pickle('20180115-def1/run2')
    datas += load_pickle('20180118-def2/run3')
    datas += load_pickle('20180118-def2/run3-2')
    datas += load_pickle('20180115-def1/run1')
    datas += load_pickle('20180118-def2/run2')

    reactor = 'short glass'
    ind =0
    data = filter_data(datas, reactor=reactor, inductance=ind, input_v_output=15e3, input_l=1
                       )
    plot_af_yield(data)
    plt.show()