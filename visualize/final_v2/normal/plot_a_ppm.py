from visualize.final_v2.normal.plot_x_ppm import plot_x_ppm
from visualize.helpers.data import filter_data, sort_data
from visualize.helpers.plot import set_plot, save_file


def plot_a_ppm(data, reactor, freqs):
    """
    Plot ppm to airflow

    :param data:
    :param reactor: long or short glass reactor
    :return:
    """
    data = filter_data(data, input_l=1) # values with l=0.5us are not correct measured.
    data = sort_data(data, key='airflow_lm')
    fig = plot_x_ppm(data, 'airflow_lm', freqs, plt_yield=True)
    fig.axes[1].set_xlabel('Airflow [$\mathrm{l_s/min.}$]')
    fig.axes[1].set_xlim(left=0)

    set_plot(fig, plot_height=1.9)
    save_file(fig, name='a-ppm-'+reactor, path='plots_final_v2/normal')
