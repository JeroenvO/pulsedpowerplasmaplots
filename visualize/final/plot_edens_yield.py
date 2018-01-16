import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.colors import color_list
from visualize.helpers.helpers import load_pickle, save_file, filter_data, get_values, set_plot

# reactor = 'long-glass-46uH'
reactor = 'long-glass-26uH'
# reactor = 'short-glass-nocoil'
# reactor = 'short-glass-26uH'
# reactor = 'short-glass-8uH'
if reactor == 'long-glass-46uH':
    data = load_pickle("20180115/run6")
elif reactor == 'long-glass-26uH':
    data = load_pickle("20180115/run5")
elif reactor == 'short-glass-26uH':
    data = load_pickle("20180115/run2")
elif reactor == 'short-glass-8uH':
    data = load_pickle("20180115/run3")
elif reactor == 'short-glass-nocoil':
    data = load_pickle("20180115/run1")
else:
    raise Exception("No input!")

data = filter_data(data, input_v_output=15e3)
data = filter_data(data, input_l=1)

fig, ax_dens = plt.subplots(5, 1, sharex=True)

w = get_values(data, 'input_l')
ws = np.unique(w)
# colors = color_list(len(ws))
m = 'o'
for power in ['output']:
    for line in data:
        edens = line['output_energy_dens']
        # freq = line['input_f']
        l = power
        c = 'black'
        iw = line['input_l']
        ax_dens[0].scatter(edens, line[power + '_yield_gkwh'], label=l, c=c, marker=m)
        # ax_freq[0].scatter(freq, line['input_yield_gkwh'])
        ax_dens[1].scatter(edens, line['o3_gramsec'], label=l, c=c, marker=m)
        # ax_freq[1].scatter(freq, line['o3_gramsec'])
        ax_dens[2].scatter(edens, line['o3_ppm'], label=l, c=c, marker=m)
        # ax_freq[2].scatter(freq, line['o3_ppm'])
        # if power == 'output':
        #     key = 'output_p_avg'
        # else:
        #     key = 'input_p'
        ax_dens[3].scatter(edens, line['output_p_avg'], label=l, c=c, marker=m)
        ax_dens[3].scatter(edens, line['input_p'], label=l, c=c, marker='x')

        ax_dens[4].scatter(edens, line['input_f'], label=l, c=c, marker=m)
    # m = 'o'
#
# marker_legends = []
# for iw, c in zip(ws, colors):
#     label = str(iw) + " $\mu$s"
#     marker_legends.append(mlines.Line2D([], [], color=c, marker='.', label=label+' no coil'))
# marker_legends.append(mlines.Line2D([], [], color='black', marker='.', label='1 $\mu$s, 26uH'))
# marker_legends.append(mlines.Line2D([], [], color='black', marker='x', label='Power input'))
# lgd = ax_dens[0].legend(handles=marker_legends, loc='upper left', bbox_to_anchor=(1, 1))
# # lgd = plt.legend()

ax_dens[0].set_ylabel('Yield [g/kWh]')
ax_dens[1].set_ylabel('Production [g/s]')
ax_dens[1].set_ylim([0, 7e-5])
# ax_dens[2].set_ylim([0, 2e3])
# ax_dens[0].set_ylim([0, 100])
ax_dens[2].set_ylabel('Concentration [PPM]')
ax_dens[3].set_ylabel('Power [W]')
ax_dens[4].set_ylabel('Frequency [Hz]')
ax_dens[4].set_xlabel('Energy density [J/l]')
set_plot(fig, plot_height=5)
save_file(fig, name='edens-'+reactor, path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final')