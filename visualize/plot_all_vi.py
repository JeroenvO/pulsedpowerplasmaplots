import matplotlib.pyplot as plt

from visualize.helpers.colors import color_list
from visualize.helpers.helpers import load_pickle, save_file, load_pickles, filter_data, align_lines, get_values
from analyze.scope_parse.c_get_lines import get_vol_cur_dir
import numpy as np
data = load_pickles("G:/Prive/MIJN-Documenten/TU/62-Stage/20180103-1000hz")
# data = filter_data(data, input_l=1)
data = align_lines(data)
# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180103/run2-1us/data.pkl")
data_nocoil_length = 0
lw = 0.4  # linewidth
voltages_unique = np.unique(get_values(data, key='input_v_output'))

colors = color_list(len(voltages_unique) + data_nocoil_length)
fig, ax = plt.subplots(2, 1)

tit = fig.suptitle('Waveforms (1us, 1kHz, 26$\mu$H, avg32)')
for i, line in enumerate(data):
    c = line['output_c']
    v = line['output_v']
    l = str(line['input_v_output'] / 1000) + 'kV'
    co = colors[np.where(voltages_unique == line['input_v_output'])[0][0]]
    ax[0].plot(line['output_t'], c, label=l, color=co, linewidth=lw)
    ax[1].plot(line['output_t'], v, label=l, color=co, linewidth=lw)

if data_nocoil_length:
    lines = get_vol_cur_dir('G:/Prive/MIJN-Documenten/TU/62-Stage/20180103/run9-nocoil/')
    for i, line in enumerate(lines):
        t, v, c, file = line
        l = str(int(file[0:4]) * 15 / 1000) + 'kV (no coil)'  # change filename to expected output v
        co = colors[i + len(data)]
        ax[0].plot(t, c / 1000, label=l, color=co, linewidth=lw)
        ax[1].plot(t, v, label=l, color=co, linewidth=lw)

ax[0].set_ylabel('Current [A]')
ax[1].set_ylabel('Voltage [V]')
plt.xlabel('time [s]')
lgd = ax[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
ax[0].grid(True)
ax[1].grid(True)
save_file(fig, name='all_vi_full_1000hz', bbox_extra_artists=(lgd, tit,))

# crop
ax[0].set_xlim(left=data[0]['output_start'], right=data[0]['output_end'])
ax[1].set_xlim(left=data[0]['output_start'], right=data[0]['output_end'])
plt.show()

save_file(fig, name='all_vi_crop_1000hz', bbox_extra_artists=(lgd, tit,))
