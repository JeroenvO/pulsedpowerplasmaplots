import matplotlib.pyplot as plt
from visualize.helpers.data import get_values, load_pickle, sort_data
from visualize.helpers.plot import set_plot, save_file


def plot_burst_ppm():
    data1 = load_pickle('20180126-burst-3/run1')
    data2 = load_pickle('20180126-burst-3/run2')
    data3 = load_pickle('20180130-burst-4/run1')
    fig, ax = plt.subplots()
    for data in [data1, data2,data3]:
        data = sort_data(data, 'burst_inner_f')
        x = get_values(data, 'burst_inner_f')
        y = get_values(data, 'o3_ppm')
        l = str(data[0]['burst_pulses'])+' pulses of '+str(data[0]['input_l'])+' us'
        plt.plot(x,y, label=l, marker='o')
    plt.text(2, 1070, ' ← 1kHz normal pulses')
    plt.xlabel('Burst inner frequency [kHz]')
    plt.ylabel('Ozone [ppm]')
    ax.legend(loc='center right')
    set_plot(fig, plot_height=1.1)
    save_file(fig, name='burst-ppm', path='plots_final_v2')

if __name__=='__main__':
    plot_burst_ppm()
    plt.show()