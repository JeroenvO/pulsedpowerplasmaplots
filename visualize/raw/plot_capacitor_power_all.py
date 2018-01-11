from analyze.scope_parse.c_get_lines import get_vol_cur_single, get_vol_cur_multiple
from analyze.scope_parse.d_calc import calc_output
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib.pyplot import plot as pl
from matplotlib.pyplot import show as s

REACTOR_GLASS_LONG = 14E-12  # long glass reactor capacitance
REACTOR_GLASS_SHORT = 6.2E-12  # short glass reactor capacitance
REACTOR_GLASS_SHORT_QUAD = 9e-12  # short glass reactor capacitance with four small electrodes parallel
REACTOR_CERAMIC = 391E-12
REACTOR_ALIXPRESS = 161E-12

fig, ax = plt.subplots(3,1, sharex=True)
lines = get_vol_cur_multiple('G:/Prive/MIJN-Documenten/TU/62-Stage/20180110/run4/scope/400')
for i,line in enumerate(lines):
    output = calc_output(line, react_cap=REACTOR_GLASS_SHORT_QUAD)
    v = output['v']
    c = output['c']
    e_cap_expected = 0.5 * REACTOR_GLASS_SHORT_QUAD * output['v_pulse'] ** 2
    t = output['t']
    p = (v * c)  # for this to be correct, make sure lines are aligned in b_correct_lines using offset 'v_div'
    e = integrate.cumtrapz(p, t, initial=0)
    # ax[0].plot(t, output['e'], label='abs(v*i)')
    ax[0].plot(t, e, label='v*i', color='red')
    ax[0].plot(t, [e_cap_expected]*len(t), label='$1/2 c v^2$', color='blue')
    ax[1].plot(t, v, label='v', color='black')
    ax[2].plot(t, c, label='i', color='black')

ax[0].set_ylabel('E [Joule]')
ax[1].set_ylabel('V [V]')
ax[2].set_ylabel('I [A]')
for a in ax:
    a.grid(True, which='major')
    a.legend()
# plt.xlim([-0.1e-6, 1.4e-6])
plt.xlabel('Time [s]')
plt.show()

#
# e_cap_output = output['e_rise'][-1]
# e_cap_input = e_in_pulse / 2
# gen_loss = e_cap_input - e_cap_output  # energy loss per pulse in generator
# gen_res = 15 * 15 + 50  # series resistance in generator [Ohm]
# res_losses = i ** 2 * gen_res
# half = int(len(res_losses) / 2)
# res_losses = res_losses[0:half]  # only rising half
# res_los = integrate.cumtrapz(res_losses, time[0:half])
# e_cap_res = res_los[-1]
# # gen_loss_expected =
