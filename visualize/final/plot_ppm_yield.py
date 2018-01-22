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
    reactors = ['long-glass-26uH', 'short-glass-nocoil', 'short-glass-26uH']
    # reactors = ['long-glass-46uH', 'long-glass-26uH', 'short-glass-nocoil', 'short-glass-26uH', 'short-glass-8uH']
    data_long_46 = load_pickle('20180115-def1/run6')
    data_long_26 = load_pickle('20180115-def1/run5') + load_pickle('20180118-def2/run1') + load_pickle('20180119-def3/run1')
    data_short_26 = load_pickle('20180115-def1/run2') + load_pickle('20180118-def2/run3') + load_pickle('20180118-def2/run3-2')
    data_short_8 = load_pickle('20180115-def1/run3')
    data_short_0 = load_pickle('20180115-def1/run1') + load_pickle('20180118-def2/run2')
    # data_total = [data_long_46, data_long_26, data_short_0, data_short_26, data_short_8]
    data_total = [data_long_26, data_short_0, data_short_26]

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
    plt.xlabel('Concentration [PPM]')
    plt.ylabel('Yield [g/kWh]')
    plt.xscale('log')
    plt.xlim([5,5000])
    ax.grid(True)
    set_plot(fig)
    save_file(fig, name='ppm-yield', path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final')
    plt.show()

plot_ppm_yield()