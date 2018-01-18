import matplotlib.pyplot as plt

from analyze.defines import *
from analyze.scope_parse.c_get_lines import get_vol_cur_single
from analyze.scope_parse.d_calc import calc_output

# file='../../20171227 glasstube, spectrometer, plasma/1/800v-full'
# file='../../20171228 glasstube/1/500v-full'
# file = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-100hz/run2-1us/scope/600.csv'
# file = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180111/run2/scope/850'
file = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180118-def2/run3-2/scope/400_4'

# for i in range(10,15):
lines = [(get_vol_cur_single(file, current_scaling=0.5))]
calc = calc_output(lines[0], REACTOR_GLASS_LONG)
# lines = get_vol_cur_multiple(file, voltage_offset=30)
# lines = get_vol_cur_multiple(file, current_scaling=-0.5)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax3 = ax1.twinx()
for line in lines:
    ax1.plot(line[0], line[1], 'b-')
    ax2.plot(line[0], line[2], 'r-')
    ax3.plot(line[0], line[1]*line[2], 'g-')

ax1.set_xlabel('time [s]')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('voltage [V]', color='b')
ax2.set_ylabel('current [A]', color='r')
ax3.set_ylabel('power [W]', color='g')
ax1.tick_params('y', colors='b')
ax2.tick_params('y', colors='r')
plt.title('V and I for 1us, 15kV pulse, small_glass')
plt.show()

fig4,ax4 = plt.subplots()
ax4.plot(calc['t'], calc['e'])

# ax2.axis([2000,5000,-9000,9000])
# ax1.axis([2000,5000,-0.5,0.5])
# fig.tight_layout()
# ax1.axis('tight')
#
# fig, ax1 = plt.subplots()
# ax1.plot(x_axis, p/1e3, 'b-', label='Power [kW]') # power
# fig.legend()
# fig.tight_layout()
#
# fig, ax1 = plt.subplots()
# ax1.plot(x_axis, integrate.cumtrapz(p, x_axis, initial=0), 'b-', label='Energy [J]') # energy
# fig.tight_layout()
#

# plt.show()
# save_file(fig, name='')
print('finish')
