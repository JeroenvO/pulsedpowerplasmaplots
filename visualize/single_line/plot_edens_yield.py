import matplotlib.lines as mlines

import matplotlib.pyplot as plt
import numpy as np
from visualize.helpers.data import load_pickle, load_pickles, filter_data, get_values
from visualize.helpers.plot import save_file
from visualize.helpers.colors import color_rainbow

# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-500Hz/run2-1us/data.pkl")
# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180105-freq/run2-1us-q/data.pkl")
# data = load_pickles("G:/Prive/MIJN-Documenten/TU/62-Stage/20180110/")
data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180115/run6")
# data2 = load_pickles("G:/Prive/MIJN-Documenten/TU/62-Stage/20180110-test")
## To show long glass reactor:
# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180105-freq/run1-1us/data.pkl")
# data += load_pickles("G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-100hz")
# data += load_pickles("G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-500hz")
# data = filter_data(data, input_v_output=15e3)
# data = [d for d in data if d['input_l'] <=4 ]


fig, ax_dens = plt.subplots(5, 1, figsize=(5, 15))
# data = filter_data(data, input_v_output=15e3)
# data = filter_data(data, inductance=26)

tit=plt.suptitle('Energy density (short glass 4 electr., 5Hz-500Hz, 2ls/min) ')
             # '\n (o) output energy. (x) input energy')
# plt.suptitle('Energy density (26$\mu$H, long glass, 100Hz-1kHz, 2ls/min, ) \n (o) output energy. (x) input energy')
#
w = get_values(data, 'input_l')

ws = np.unique(w)
colors = color_rainbow(len(ws))
# ax_freq = [ax.twiny() for ax in ax_dens]
# m = 'x'
m = 'o'
for power in ['output']:
    for line in data:
        edens = line['output_energy_dens']
        # freq = line['input_f']
        l = power
        iw = line['input_l']
        if line['inductance'] == 0:
            c = colors[np.where(ws == iw)[0][0]]  # color for each pulsewidth
        else:
            c = 'black'
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

marker_legends = []
for iw, c in zip(ws, colors):
    label = str(iw) + " $\mu$s"
    marker_legends.append(mlines.Line2D([], [], color=c, marker='.', label=label+' no coil'))
marker_legends.append(mlines.Line2D([], [], color='black', marker='.', label='1 $\mu$s, 26uH'))
marker_legends.append(mlines.Line2D([], [], color='black', marker='x', label='Power input'))
lgd = ax_dens[0].legend(handles=marker_legends, loc='upper left', bbox_to_anchor=(1, 1))
# lgd = plt.legend()

ax_dens[0].set_ylabel('Yield [g/kWh]')
ax_dens[1].set_ylabel('Production [g/s]')
ax_dens[1].set_ylim([0, 7e-5])
# ax_dens[2].set_ylim([0, 2e3])
# ax_dens[0].set_ylim([0, 100])
ax_dens[2].set_ylabel('Ozone [ppm]')
ax_dens[3].set_ylabel('Power [W]')
ax_dens[4].set_ylabel('Frequency [Hz]')
ax_dens[3].set_xlabel('Energy density [J/l]')
for a in ax_dens:
    a.grid(True)
# ax_freq[2].set_xlabel('Frequenty [Hz]')
plt.xlabel('Energy density [J/l]')
save_file(fig, name='edens_yield_shortglass', bbox_extra_artists=(lgd,tit,))
plt.show()
