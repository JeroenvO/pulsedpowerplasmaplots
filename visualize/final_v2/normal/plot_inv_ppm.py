import matplotlib.lines as mlines
import matplotlib.pyplot as plt

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
        y = get_values(d, 'o3_ppm')
        y2 = get_values(d, 'output_yield_gkwh')
        # interpolate_plot(ax_yield, x, y2)
        # interpolate_plot(ax_ppm, x, y)
        for x, y, y2 in zip(x, y, y2):
            ax_ppm.scatter(x, y, c=c, marker=m)
            ax_yield.scatter(x, y2, c=c, marker=m)
    marker_legends = [
        (mlines.Line2D([], [], marker=markers[0], label='Normal', linewidth=0, markerfacecolor=color2[0], markeredgewidth=0)),
        (mlines.Line2D([], [], marker=markers[1], label='Inverted', linewidth=0, markerfacecolor=color2[1], markeredgewidth=0)),
    ]
    ax_ppm.set_ylabel('Concentration [ppm]')
    ax_yield.set_ylabel('Yield [g/kWh]')
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