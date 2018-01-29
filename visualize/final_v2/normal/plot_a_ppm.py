import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickles, filter_data, get_values, sort_data
from visualize.helpers.plot import set_plot, interpolate_plot, save_file, markers


def plot_a_ppm():
    """
    Plot ppm to applied pulse voltage

    :param data: NOT USED
    :param reactor: long or short glass reactor
    :return:
    """
    data = []
    if reactor == 'short-glass':
        # add synthetic zero point
        # data = [{'input_f': 100, 'input_l': 1, 'output_v_pulse': 12e3, 'o3_ppm': 0},
        #         {'input_f': 500, 'input_l': 1, 'output_v_pulse': 12e3, 'o3_ppm': 0},]
        data = load_pickles('20180129-airf')
    else:
        raise Exception('invalid reactor')

    freqs = [400, 1000]

    data = filter_data(data, input_l=1) # values with l=0.5us are not correct measured.
    data = sort_data(data, key='airflow_lm')

    fig, (ax, ax2) = plt.subplots(2, 1)
    c = 'black'
    marker_legends = []
    for i, f in enumerate(freqs):
        m = markers[i]
        d = filter_data(data, input_f=f)
        x = get_values(d, 'airflow_lm')
        x2 = get_values(d, 'output_energy_dens')
        y = get_values(d, 'o3_ppm')
        y2 = get_values(d, 'output_yield_gkwh')
        interpolate_plot(ax, x, y)
        interpolate_plot(ax2, x2, y2)
        for x, y, y2, x2 in zip(x, y, y2, x2):
            ax.scatter(x, y, c=c, marker=m)
            ax2.scatter(x2, y2, c=c, marker=m)
        marker_legends.append(mlines.Line2D([], [], marker=m, label=str(f)+' Hz', color='grey', markerfacecolor='black', markeredgewidth=0))

    ax.set_ylabel('Concentration [PPM]')
    ax2.set_ylabel('Yield [g/kWh]')
    ax.set_xlabel('Airflow [l_s/minute]')
    ax2.set_xlabel('Energy density')

    plt.legend(handles=marker_legends)

    set_plot(fig, plot_height=2)

    save_file(fig, name='a-ppm-'+reactor, path='plots_final_v2')


if __name__ == '__main__':
    data = []
    reactor = 'short-glass'
    # reactor = 'long-glass'
    plot_a_ppm()