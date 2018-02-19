import os
import pickle
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import matplotlib.pylab as pl

from analyze.defines import REACTOR_GLASS_LONG, REACTOR_GLASS_SHORT_QUAD
from visualize.helpers.data import load_pickles
from visualize.helpers.plot import save_file, set_plot


def plot_ppm_yield():
    """
    Plot ppm vs yield for all reactors

    :param data:
    :param reactor:
    :return:
    """
    dirs = sorted(os.listdir('G:/Prive/MIJN-Documenten/TU/62-Stage/'))
    start = dirs.index('20180115-def1')
    end = dirs.index('20180130-v-sweep')
    dirs = dirs[start:end+1]
    data = []
    for dir in dirs:
        if dir not in ['20180117-cap'] and 'burst' not in dir:
            data += load_pickles(dir)
    data = [line for line in data if 'output_yield_gkwh' in line.keys()]
    # data = filter_data(data, output_yield_gkwh__gt=20)
    markers = ['.', 'x', '+']
    fig, ax = plt.subplots()
    cm = plt.cm.get_cmap('plasma')
    # scatterplot for each point
    for line in data:
        x = line['o3_ppm']
        y = line['output_yield_gkwh']
        if line['reactor'] == REACTOR_GLASS_LONG:
            m = markers[0]
        elif line['reactor'] == REACTOR_GLASS_SHORT_QUAD:
            if line['inductance'] == 0:
                m = markers[1]
            else:
                m = markers[2]
        else:
            raise Exception('invalid reactor: '+line['reactor'])
        c = line['output_energy_dens']
        plt.scatter(x, y, c=c, marker=m, s=20, cmap=cm, vmin=1.3, vmax=300)


    marker_legends = [
        (mlines.Line2D([], [], color='black', marker=markers[0], label='Long glass, coil', linewidth=0)),
        (mlines.Line2D([], [], color='black', marker=markers[1], label='Short glass, no coil', linewidth=0)),
        (mlines.Line2D([], [], color='black', marker=markers[2], label='Short glass, coil', linewidth=0))
        ]
    plt.legend(handles=marker_legends, loc='lower right')
    plt.text(550, 85, '← Higher airflow')
    plt.xlabel('Concentration [ppm]')
    plt.ylabel('Yield [g/kWh]')
    cb = plt.colorbar(orientation='horizontal', pad=0.2)
    cb.set_label('Energy density [J/l]')
    # cb.ax.set_xticks(rotation=45)
    # cb.ax.set_ylabel('Energy density [J/l]', rotation=90)
    # plt.xscale('log')
    # plt.xlim([5,5000])
    ax.grid(True)
    set_plot(fig, plot_height=1.3)
    save_file(fig, name='ppm-yield-total', path='plots_final_v2/normal')


if __name__ == '__main__':
    plot_ppm_yield()
    plt.show()