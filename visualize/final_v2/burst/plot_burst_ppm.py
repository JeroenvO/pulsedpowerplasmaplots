import matplotlib.pyplot as plt
from visualize.helpers.data import get_values, load_pickle, sort_data
from visualize.helpers.plot import set_plot, save_file


def plot_burst_ppm(datas):
    fig, ax = plt.subplots()
    for data in datas:
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
    save_file(fig, name='burst-ppm', path='plots_final_v2/burst')

if __name__=='__main__':
    plot_burst_ppm()
    plt.show()