import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickles, filter_data, get_values, sort_data
from visualize.helpers.plot import set_plot, interpolate_plot, save_file, markers

def plot_x_ppm(data, reactor, key, freqs=[400]):
    """
    Plot ppm to anything

    :param data: NOT USED
    :param reactor: long or short glass reactor
    :return:
    """
    assert key in ['input_v', 'input_l', 'airflow_lm', 'input_f', 'output_v_pulse']
    data = sort_data(data, key=key)

    fig, ax = plt.subplots()
    c = 'black'
    marker_legends = []
    for i, f in enumerate(freqs):
        m = markers[i]
        d = filter_data(data, input_f=f)
        x = get_values(d, key=key)
        if key == 'output_v_pulse':
            x /= 1000
        y = get_values(d, 'o3_ppm')
        interpolate_plot(ax, x, y)
        for x, y in zip(x, y):
            ax.scatter(x, y, c=c, marker=m)
        marker_legends.append(mlines.Line2D([], [], marker=m, label=str(f)+'Hz', color='grey', markerfacecolor='black', markeredgewidth=0))
    plt.ylabel('Concentration [PPM]')
    plt.legend(handles=marker_legends)
    return fig
