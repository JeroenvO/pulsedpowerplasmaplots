import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
from analyze.defines import *
from visualize.helpers.data import load_pickle, filter_data, get_values
from visualize.helpers.plot import save_file, set_plot


def plot_f_epulse(data, reactor):
    """
    Plots energy per pulse for various frequencies as errorbar

    :param data:
    :param reactor:
    :return:
    """
    data = filter_data(data, input_v_output=15e3, input_l=1)

    fig, ax = plt.subplots()
    uf = np.unique(get_values(data, 'input_f'))
    center = []
    # mins = []
    # maxs = []
    xs = []
    std = []
    for f in uf:
        d = filter_data(data, input_f=f)
        l = get_values(d, key='output_e_plasma_single')  # returns list of arrays with values.
        if len(l) == 1:
            continue  # dont use single measurements, only double or triple
        v = np.concatenate(l)  # if multiple measurements, concat
        epuls = np.array(v)*1000  # array of values
        mn = np.mean(epuls)
        xs.append(np.mean((get_values(d, key='output_energy_dens'))))
        # mins.append(mn-min(epuls))
        # maxs.append(max(epuls)-mn)
        std.append(np.std(epuls))
        center.append(mn)

    c='black'
    ax.scatter(xs, center, c=c)
    ax.errorbar(xs, center, yerr=std, xerr=None, ecolor=c, fmt='none', capsize=3)

    ax.set_xlabel('Energy density [J/l]')
    # ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Pulse plasma energy [mJ]')
    set_plot(fig, plot_height=1.4)
    save_file(fig, name='epulse2-'+reactor, path='plots_poster/normal')


if __name__ == '__main__':
#     reactors = ['long-glass-46uH', 'long-glass-26uH', 'short-glass-nocoil', 'short-glass-26uH', 'short-glass-8uH']
#     reactor = reactors[3]
#     print(reactor)
#     if reactor == 'long-glass-46uH':
#         data = load_pickle("20180115-def1/run6")
#     elif reactor == 'long-glass-26uH':
#         data = load_pickle("20180115-def1/run5")
#     elif reactor == 'short-glass-26uH':
#         data = load_pickle("20180115-def1/run2")
#     elif reactor == 'short-glass-8uH':
#         data = load_pickle("20180115-def1/run3")
#     elif reactor == 'short-glass-nocoil':
#         data = load_pickle("20180115-def1/run1")
#     else:
#         raise Exception("No input!")
#     plot_f_epulse(data, reactor)
# # # frequency data
    datas = load_pickle('20180115-def1/run5')
    datas += load_pickle('20180118-def2/run1')
    datas += load_pickle('20180119-def3/run1')
    datas += load_pickle('20180115-def1/run2')
    datas += load_pickle('20180118-def2/run3')
    datas += load_pickle('20180118-def2/run3-2')
    datas += load_pickle('20180115-def1/run1')
    datas += load_pickle('20180118-def2/run2')

    for reactor, ind in [(REACTOR_GLASS_LONG, 26), (REACTOR_GLASS_SHORT_QUAD, 0), (REACTOR_GLASS_SHORT_QUAD, 26)]:
        data = filter_data(datas, reactor=reactor, inductance=ind)
        if ind:
            name = reactor + '-' + str(ind) + 'uH'
        else:
            name = reactor + '-nocoil'
        plot_f_epulse(data, name)
