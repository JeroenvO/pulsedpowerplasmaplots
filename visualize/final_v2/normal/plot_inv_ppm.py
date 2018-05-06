import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
from visualize.helpers.data import filter_data, get_values, sort_data, load_pickles, load_pickle
from visualize.helpers.plot import interpolate_plot, markers, save_file, set_plot
from visualize.helpers.colors import color2
from analyze.defines import REACTOR_GLASS_SHORT_QUAD

def plot_inv_ppm(data_nor, data_inv):
    """
    Plot ppm to inverted reactor

    :param data: NOT USED
    :param reactor: long or short glass reactor
    :return:
    """
    fig, (ax_ppm, ax_yield) = plt.subplots(2, 1, sharex=True)
    for i, d in enumerate([data_nor, data_inv]):
        m = markers[i]
        c=color2[i]
        x = get_values(d, key='input_f')
        ux = sorted(np.unique(x))
        y = get_values(d, 'o3_ppm')
        y2 = get_values(d, 'output_yield_gkwh')
        z2 = get_values(d, 'output_yield_gkwh_single')
        uz2 = [] # combined version of z2
        uy2 = []
        uy = []
        for uxa in ux:
            ind = [True if a==uxa else False for a in x ]
            d = z2[ind]  # list of lists of all single data points for 'uxa'
            uz2a = ([item for sublist in d for item in sublist])  # flattened version of d, list of all single data.
            uy2a = np.mean(uz2a)
            uya = np.mean(y[ind])
            # average should be equal to average of averages:
            print(uy2/np.mean(y2[ind]))
            uy2.append(uy2a)
            uz2.append(uz2a)
            uy.append(uya)

        interpolate_plot(ax_yield, ux, uy2)
        interpolate_plot(ax_ppm, ux, uy)
        for xa, ya, y2a in zip(ux, uy, uy2):
            ax_ppm.scatter(xa, ya, c=c, marker=m)
            ax_yield.scatter(xa, y2a, c=c, marker=m)

        # mi = [y2a - min(z2a) for z2a, y2a in zip(uz2, uy2)]
        # ma = [max(z2a) - y2a for z2a, y2a in zip(uz2, uy2)]
        std = []
        for z2a in uz2:
            std.append(np.std(z2a))
        # std = np.std(z2, 1)  # list of minima of y
        ax_yield.errorbar(ux, uy2, yerr=std, xerr=None, ecolor=c, fmt='none', capsize=3)

    marker_legends = [
        (mlines.Line2D([], [], marker=markers[0], label='Normal', color='grey', markerfacecolor=color2[0], markeredgewidth=0)),
        (mlines.Line2D([], [], marker=markers[1], label='Inverted', color='grey', markerfacecolor=color2[1], markeredgewidth=0)),
    ]

    ax_ppm.set_ylabel('Ozone [ppm]')
    ax_yield.set_ylabel('Yield [g/kWh]')
    ax_yield.set_xlabel('Frequency [Hz]')
    plt.legend(handles=marker_legends)
    set_plot(fig, plot_height=1.9)
    save_file(fig, name='inv-ppm', path='plots_final_v2/normal')


if __name__ == '__main__':
    datas = load_pickle('20180115-def1/run5')
    datas += load_pickle('20180118-def2/run1')
    datas += load_pickle('20180119-def3/run1')
    datas += load_pickle('20180115-def1/run2')
    datas += load_pickle('20180118-def2/run3')
    datas += load_pickle('20180118-def2/run3-2')
    datas += load_pickle('20180115-def1/run1')
    datas += load_pickle('20180118-def2/run2')
    data_nor = filter_data(datas, reactor=REACTOR_GLASS_SHORT_QUAD, inductance=0)
    data_inv = load_pickle('20180201-inv/run1')
    plot_inv_ppm(data_nor, data_inv)
    plt.show()
