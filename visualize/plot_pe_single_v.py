from scipy import integrate
import matplotlib.pyplot as plt

from visualize.helpers.colors import color_list
from visualize.helpers.helpers import load_pickle, save_file
from analyze.scope_parse.c_get_lines import get_vol_cur_dir
from visualize.helpers.helpers import filter_data
data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-500Hz/run9-20us/data.pkl")
data = filter_data(data, input_v_output=15e3)
lw = 0.4 # linewidth
# colors = color_list(len(data))
fig, ax = plt.subplots(3,1, sharex=True, figsize=(5,15))

tit = fig.suptitle('Power in pulse (20us, 500Hz, 26$\mu$H, avg32, 15kV)')
for i, line in enumerate(data):
    p = line['output_p']
    e_out = line['output_e']
    t = line['output_t']
    pr = line['output_c'] ** 2 * 225
    e_res = integrate.cumtrapz(pr, t, initial=0)
    e_in = line['input_p'] / line['input_f']
    # l=str(line['input_v_output'] / 1000) + 'kV'
    # plot power on reactor
    c = None

    ax[0].plot(t, p, color=c, linewidth=lw)

    # plot power loss in resistors
    ax[1].plot(t, pr, color=c, linewidth=lw)

    # output reactor energy
    ax[2].plot(t, e_out, label='reactor', color=c, linewidth=lw)

    # energy loss in resistors
    ax[2].plot(t, e_res, label='generator', color=c, linewidth=lw)

    # total energy
    ax[2].plot(t, [e_in]*len(t), label='input', color=c, linewidth=lw)
    ax[2].plot(t, e_res+e_out, label='sum', color=c, linewidth=lw)

# lgd = ax[0].legend(loc='upper left', bbox_to_anchor=(1,1))
ax[2].legend()
ax[0].set_title('Power on reactor')
ax[1].set_title('Power lost in generator')
ax[2].set_title('Energy generator, reactor, sum and input')
ax[0].set_ylabel('P (react) [W]')
ax[1].set_ylabel('P (resist) [W]')
ax[2].set_ylabel('E [J]')
# ax[3].set_ylabel('E (res) [J]')
# ax[4].set_ylabel('E (sum) [J]')
plt.xlabel('time [s]')
plt.show()
save_file(fig, name='pe_20us_15kV', bbox_extra_artists=(tit,))
