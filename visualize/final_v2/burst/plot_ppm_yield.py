import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickles, load_pickle, get_values
from visualize.helpers.plot import save_file, set_plot


def plot_ppm_yield():
    """
    Plot ppm vs yield for all reactors

    :param data:
    :param reactor:
    :return:
    """
    #TODO

    markers = ['.', 'x', '+']
    marker_legends = []
    fig, ax = plt.subplots()
    for i, (reactor, data) in enumerate(zip(reactors, data_total)):
        y = get_values(data, 'output_yield_gkwh')
        x = get_values(data, 'o3_ppm')
        assert len(y) == len(x)

        m = markers[i]  # marker for each reactor
        c = 'black'

        # scatterplot for each point
        for ix, iy in zip(x, y):
            ax.scatter(ix, iy, c=c, marker=m, s=20)

        label = reactor #str(iw) + " $\mu$s"
        marker_legends.append(mlines.Line2D([], [], color='black', marker=m, label=label, linewidth=0))
    plt.legend(handles=marker_legends, loc='best')
    plt.xlabel('Ozone [ppm]')
    plt.ylabel('Yield [g/kWh]')
    plt.xscale('log')
    plt.xlim([5,5000])
    ax.grid(True)
    set_plot(fig)
    save_file(fig, name='ppm-yield-burst', path='plots_final_v2')
    plt.show()


if __name__ == '__main__':
    print("Nope")