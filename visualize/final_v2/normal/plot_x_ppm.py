import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from visualize.helpers.data import filter_data, get_values, sort_data
from visualize.helpers.plot import interpolate_plot, markers


def plot_x_ppm(data, key, freqs=[400]):
    """
    Plot ppm to anything

    :param data: NOT USED
    :param reactor: long or short glass reactor
    :return:
    """
    assert key in ['input_v', 'input_l', 'airflow_lm', 'input_f', 'output_v_pulse']
    data = sort_data(data, key=key)

    # fig, (ax_ppm, ax_yield) = plt.subplots(2,1)
    fig, ax_ppm = plt.subplots()
    c = 'black'
    marker_legends = []
    for i, f in enumerate(freqs):
        m = markers[i]
        d = filter_data(data, input_f=f)
        x = get_values(d, key=key)
        if key == 'output_v_pulse':
            x /= 1000
        y = get_values(d, 'o3_ppm')
        # y2 = get_values(d, 'output_yield_gkwh')
        interpolate_plot(ax_ppm, x, y)
        # interpolate_plot(ax_yield, x, y2)
        for x, y in zip(x, y):
            ax_ppm.scatter(x, y, c=c, marker=m)
            # ax_yield.scatter(x, y2, c=c, marker=m)
        marker_legends.append(mlines.Line2D([], [], marker=m, label=str(f)+'Hz', color='grey', markerfacecolor='black', markeredgewidth=0))
    ax_ppm.set_ylabel('Concentration [ppm]')
    # ax_yield.set_ylabel('Yield [g/kWh]')
    plt.legend(handles=marker_legends)
    return fig
