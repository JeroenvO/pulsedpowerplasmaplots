import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickles, load_pickle, get_values
from visualize.helpers.plot import save_file, set_plot
from visualize.helpers.burst import calc_burst
from visualize.helpers.colors import color_plasma

def plot_ppm_yield(datas):
    """
    Plot ppm vs yield for all burst modes

    :param data:
    :param reactor:
    :return:
    """
    colors = color_plasma(len(datas))
    marker_legends = []
    fig, ax = plt.subplots()
    for i, data in enumerate(datas):
        d = calc_burst(data)
        m = '.'

        ax.scatter(d['ppm'], d['output_yield_gkwh'], c=colors[i], marker=m, s=20)

        # label = reactor #str(iw) + " $\mu$s"
        # marker_legends.append(mlines.Line2D([], [], color='black', marker=m, label=label, linewidth=0))
    # plt.legend(handles=marker_legends, loc='best')
    plt.xlabel('Ozone [ppm]')
    plt.ylabel('Yield [g/kWh]')
    plt.xscale('log')
    # plt.xlim([5,5000])
    ax.grid(True)
    set_plot(fig)
    save_file(fig, name='ppm-yield-burst', path='plots_final_v2/burst')
    plt.show()


if __name__ == '__main__':
    print("Nope")