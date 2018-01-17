import matplotlib.pyplot as plt
from scipy import integrate
from visualize.helpers.data import sort_data

from visualize.helpers.colors import color_list
from visualize.helpers.data import load_pickle, save_file, filter_data

# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180105-freq/run1-1us/data.pkl")
# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-500Hz/run2-1us/data.pkl")
# data = filter_data(data, input_v_output=15e3)
# data = sort_data(data, key='input_f')
data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180115/run5/data.pkl")
data = filter_data(data, input_v_output=15e3)
data = filter_data(data, input_f=10)
lw = 0.4  # linewidth
colors = color_list(len(data))
fig, ax = plt.subplots(6, 1, sharex=True, figsize=(5, 15))

tit = fig.suptitle('Power in pulse (15kV, 1us, 100Hz-1kHz, 26$\mu$H, avg32)')

for i, line in enumerate(data):
    p = line['output_p']
    e_out = line['output_e']
    t = line['output_t']
    e_in = line['input_p'] / line['input_f']
    # l=str(line['input_v_output'] / 1000) + 'kV'
    l = str(line['input_f']) + 'Hz'
    # plot power on reactor
    ax[0].plot(t, p, label=l, color=colors[i], linewidth=lw)

    # plot power loss in resistors
    # ax[1].plot(t, line['output_p_res'], label=l, color=colors[i], linewidth=lw)

    # output reactor energy
    ax[2].plot(t, e_out, label=l, color=colors[i], linewidth=lw)

    # energy loss in resistors
    ax[2].plot(t, line['output_e_res'], label=l, color=colors[i], linewidth=lw)

    # total energy
    # ax[3].axhline(e_in, color=colors[i], linewidth=lw)
    # ax[3].plot(t, line['output_e_res'] + e_out, label=l, color=colors[i], linewidth=lw)

    # voltage and current
    ax[4].plot(t, line['output_v'], label=l, color=colors[i], linewidth=lw)
    ax[5].plot(t, line['output_c'], label=l, color=colors[i], linewidth=lw)

lgd = ax[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
ax[0].set_ylabel('P (react) [W]')
ax[1].set_ylabel('P (resist) [W]')
ax[2].set_ylabel('E gener/react [J]')
ax[3].set_ylabel('E sum [J]')
ax[4].set_ylabel('Voltage [V]')
ax[5].set_ylabel('Current [A]')
# ax[3].set_ylabel('E (res) [J]')
# ax[4].set_ylabel('E (sum) [J]')
plt.xlabel('time [s]')
plt.show()
save_file(fig, name='pe_all_1us_15kV', bbox_extra_artists=(lgd, tit,))
