import matplotlib.pyplot as plt
from visualize.helpers.data import get_values, load_pickle, sort_data
from visualize.helpers.plot import set_plot, save_file, markers
from visualize.helpers.colors import color2


def plot_burst_ppm(datas):
    datas.reverse()
    fig, ax = plt.subplots()
    for i, data in enumerate(datas):
        data = sort_data(data, 'burst_inner_f')
        x = get_values(data, 'burst_inner_f')
        y = get_values(data, 'o3_ppm')
        l = str(data[0]['burst_pulses'])+' pulses'
        plt.plot(x,y, label=l, marker=markers[i], markerfacecolor=color2[i], linewidth=0.9, color='grey', markeredgewidth=0, markersize=5)
    plt.text(2, 1070, ' ← 1kHz normal pulses')
    plt.xlabel('Burst inner frequency [kHz]')
    plt.ylabel('Ozone [ppm]')
    ax.legend(loc=1)
    set_plot(fig, plot_height=1.1)
    save_file(fig, name='burst-ppm', path='plots_final_v2/burst')

if __name__=='__main__':
    datas = [
        load_pickle('20180126-burst-3/run1'),
        load_pickle('20180126-burst-3/run2')
    ]
    # datas += load_pickle('20180130-burst-4/run1')  # burst with 500ns pulses instead of 1us.
    plot_burst_ppm(datas)
    plt.show()
