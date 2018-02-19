import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from visualize.helpers.data import filter_data, get_values, sort_data
from visualize.helpers.plot import interpolate_plot, markers
from visualize.helpers.colors import color2

def plot_x_ppm(data, key, freqs=[400], plt_yield=False):
    """
    Plot ppm to anything

    :param data: NOT USED
    :param reactor: long or short glass reactor
    :return:
    """
    assert key in ['input_v', 'input_l', 'airflow_lm', 'input_f', 'output_v_pulse']
    data = sort_data(data, key=key)
    if plt_yield:
        fig, (ax_ppm, ax_yield) = plt.subplots(2, 1, sharex=True)
    else:
        fig, ax_ppm = plt.subplots()
    marker_legends = []
    for i, f in enumerate(freqs):
        m = markers[i]
        c=color2[i]
        d = filter_data(data, input_f=f)
        x = get_values(d, key=key)
        if key == 'output_v_pulse':
            x /= 1000
        y = get_values(d, 'o3_ppm')
        interpolate_plot(ax_ppm, x, y)

        for xa, ya in zip(x, y):
            ax_ppm.scatter(xa, ya, c=c, marker=m)
        marker_legends.append(
            mlines.Line2D([], [], marker=m, label=str(f) + 'Hz', color='grey', markerfacecolor=c, markeredgewidth=0))

        if plt_yield:
            d = [x for x in d if 'output_yield_gkwh' in x]  # only values that have waveform data
            y2 = get_values(d, 'output_yield_gkwh')
            x2 = get_values(d, key=key)
            interpolate_plot(ax_yield, x2, y2)
            for x2a, y2a in zip(x2, y2):
                ax_yield.scatter(x2a, y2a, c=c, marker=m)
    ax_ppm.set_ylabel('Concentration [ppm]')
    if plt_yield:
        ax_yield.set_ylabel('Yield [g/kWh]')
    plt.legend(handles=marker_legends)
    return fig
