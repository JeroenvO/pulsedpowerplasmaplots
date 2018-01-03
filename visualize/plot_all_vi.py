import matplotlib.pyplot as plt

from visualize.helpers.colors import color_list
from visualize.helpers.helpers import load_pickle, save_file
from analyze.scope_parse.c_get_lines import get_vol_cur_dir
data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180103/run2-1us/data.pkl")
data_nocoil_length = 3
lw = 0.4 # linewidth
colors = color_list(len(data)+data_nocoil_length)
fig, ax = plt.subplots(2,1)
tit = fig.suptitle('Waveforms (1us, 1kHz, 26$\mu$H, avg32)')
for i, line in enumerate(data):
    c = line['output_current']
    v = line['output_voltage']
    l=str(line['input_voltage_output'] / 1000) + 'kV'
    ax[0].plot(line['output_time'], c, label=l, color=colors[i], linewidth=lw)
    ax[1].plot(line['output_time'], v, label=l, color=colors[i], linewidth=lw)

if data_nocoil_length:
    lines = get_vol_cur_dir('G:/Prive/MIJN-Documenten/TU/62-Stage/20180103/run9-nocoil/')
    for i, line in enumerate(lines):
        t, v, c, file = line
        l = str(int(file[0:3])*15/1000) + 'kV (no coil)'  # change filename to expected output v
        co = colors[i+len(data)]
        ax[0].plot(t, c/1000, label=l, color=co, linewidth=lw)
        ax[1].plot(t, v, label=l, color=co, linewidth=lw)

ax[0].set_ylabel('Current [A]')
ax[1].set_ylabel('Voltage [V]')
plt.xlabel('time [s]')
lgd = ax[0].legend(loc='upper left', bbox_to_anchor=(1,1))
ax[0].grid(True)
ax[1].grid(True)
save_file(fig, name='all_vi_full_nocoil', bbox_extra_artists=(lgd,tit,))


# crop
ax[0].set_xlim(left=data[0]['output_start'], right=data[0]['output_end'])
ax[1].set_xlim(left=data[0]['output_start'], right=data[0]['output_end'])
plt.show()

save_file(fig, name='all_vi_crop_nocoil', bbox_extra_artists=(lgd,tit,))