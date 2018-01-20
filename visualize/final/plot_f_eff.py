import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

from visualize.helpers.data import load_pickle, filter_data, get_values
from visualize.helpers.plot import save_file, set_plot
from visualize.helpers.colors import colors


def plot_f_eff(data, reactor):
    """
    Plots capacitive, resistive, plasma and input energy per pulse for various frequencies

    :param data:
    :param reactor:
    :return:
    """
    data = filter_data(data, input_v_output=15e3, input_l=1)

    fig, ax = plt.subplots()
    uf = np.unique(get_values(data, 'input_f'))
    p_out_p = []
    p_out_r = []
    p_in = []

    if reactor[0:10] == 'long-glass':
        c = 2.6 # mJ capacitive losses at 15kV pulses.
    elif reactor[0:11] == 'short-glass':
        c = 2.25
    else:
        raise Exception('Incorrect reactor supplied')

    marker_legends = []
    for f in uf:
        d = filter_data(data, input_f=f)
        p_out_p.append(np.mean(get_values(d, key='output_e_plasma'))*1000)  # average plasma energy
        p_out_r.append(np.mean(get_values(d, key='output_e_res_total'))*1000)  # average resistive energy
        p_in.append(np.mean(get_values(d, key='input_e_pulse'))*1000)

    p_out_p = (np.array(p_out_p))
    p_out_r = (np.array(p_out_r))
    p_in = (np.array(p_in))
    # plot output power and losses
    plt.stackplot(uf, ([c]*len(uf), p_out_r, p_out_p), colors=(colors[0], colors[1], colors[2]))

    # plot input power
    plt.plot(uf, p_in, label='Input power [mJ]', color='black', marker='.')

    # plot efficiency
    # ax2 = ax.twinx()
    # eff = p_out_p / p_in *100
    # ax2.plot(uf, eff, marker='d', color='black')

    # legend
    marker_legends = [
        mlines.Line2D([], [], marker='.', label='Input energy', color='black', markerfacecolor='black',
                      markeredgewidth=0),

        mpatches.Patch(color=colors[2], label='Plasma energy'),
        mpatches.Patch(color=colors[1], label='Resistive energy'),
        mpatches.Patch(color=colors[0], label='Capacitive energy'),
        # mlines.Line2D([], [], marker='d', label='Efficiency (%)', color='black', markerfacecolor='black',
        #               markeredgewidth=0)
    ]

    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Pulse energy [mJ]')
    # ax2.set_ylabel('input to plasma effiency [%]')
    ax.set_ylim([0, 40])
    plt.legend(handles=marker_legends, loc='top right')
    set_plot(fig, plot_height=1.4)
    save_file(fig, name='eff-'+reactor, path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final')


if __name__ == '__main__':
    # reactors = ['long-glass-46uH', 'long-glass-26uH', 'short-glass-nocoil', 'short-glass-26uH', 'short-glass-8uH']
    reactors = ['long-glass-26uH', 'short-glass-nocoil', 'short-glass-26uH']
    reactor = reactors[0]
    print(reactor)
    if reactor == 'long-glass-46uH':
        data = load_pickle("20180115-def1/run6")
    elif reactor == 'long-glass-26uH':
        data = load_pickle("20180115-def1/run5")
        data += load_pickle('20180118-def2/run1')
        data += load_pickle('20180119-def3/run1')
    elif reactor == 'short-glass-26uH':
        data = load_pickle("20180115-def1/run2")
        data += load_pickle('20180118-def2/run3')
    elif reactor == 'short-glass-8uH':
        data = load_pickle("20180115-def1/run3")
    elif reactor == 'short-glass-nocoil':
        data = load_pickle("20180115-def1/run1")
        # data += load_pickle('20180118-def2/run2')
    else:
        raise Exception("No input!")
    plot_f_eff(data, reactor)
