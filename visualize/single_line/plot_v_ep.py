import matplotlib.pyplot as plt

from visualize.helpers.colors import color_rainbow
from visualize.helpers.data import load_pickles, save_file, get_values, filter_data
from analyze.scope_parse.c_get_lines import get_vol_cur_dir
import numpy as np

# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180103/run2-1us/data.pkl")
# data = load_pickles('G:/Prive/MIJN-Documenten/TU/62-Stage/20180111')
data = load_pickles('20180104-500hz')
data = filter_data(data, input_v__gt=600)

lw = 0.4  # linewidth

w = np.unique(get_values(data, 'input_l'))
colors = color_rainbow(len(w))

fig, ax = plt.subplots(2, 1)
tit = fig.suptitle('Waveforms (1kHz, 26$\mu$H, avg32)')
for i, iw in enumerate(w):
    l = str(iw) + '$\mu$s'
    d = [d for d in data if d['input_l'] == iw]
    v = get_values(d, 'output_v_pulse')
    y = get_values(d, 'o3_gramsec')
    ei = get_values(d, 'input_p')
    eo = get_values(d, 'output_e_rise') * get_values(d, 'input_f')
    # l=str(line['input_voltage_output'] / 1000) + 'kV'
    ax[0].plot(v, y, label=l, color=colors[i], linewidth=lw)
    ax[1].plot(v, ei, label=l + ' Pin', color=colors[i], linewidth=lw)
    ax[1].plot(v, eo, label=l + 'Pout', color=colors[i], linewidth=lw)

ax[0].set_ylabel('Concentration [gram/s]')

ax[1].set_ylabel('Power [W]')
plt.xlabel('Voltage [V]')
ax[0].grid(True)
ax[1].grid(True)
lgd = ax[0].legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()
save_file(fig, name='v_ep', bbox_extra_artists=(lgd, tit,))
