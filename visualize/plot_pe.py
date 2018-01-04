import matplotlib.pyplot as plt

from visualize.helpers.colors import color_list
from visualize.helpers.helpers import load_pickle, save_file
from analyze.scope_parse.c_get_lines import get_vol_cur_dir
data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180103-1000Hz/run2-1us/data.pkl")

lw = 0.4 # linewidth
colors = color_list(len(data))
fig, ax = plt.subplots(2,1)

tit = fig.suptitle('Power in pulse (6us, 1kHz, 26$\mu$H, avg32)')
for i, line in enumerate(data):
    p = line['output_p']
    e = line['output_e']
    l=str(line['input_voltage_output'] / 1000) + 'kV'
    ax[0].plot(line['output_t'], p, label=l, color=colors[i], linewidth=lw)
    ax[1].plot(line['output_t'], e, label=l, color=colors[i], linewidth=lw)
lgd = ax[0].legend(loc='upper left', bbox_to_anchor=(1,1))
ax[0].set_ylabel('Power [W]')
ax[1].set_ylabel('Energy [J]')
plt.xlabel('time [s]')
plt.show()
save_file(fig, name='pe_6us', bbox_extra_artists=(lgd,tit,))
