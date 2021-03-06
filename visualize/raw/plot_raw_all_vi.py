import matplotlib.pyplot as plt

from analyze.defines import *
from analyze.scope_parse.c_get_lines import get_vol_cur_single
from analyze.scope_parse.d_calc import calc_output

# file='../../20171227 glasstube, spectrometer, plasma/1/800v-full'
# file='../../20171228 glasstube/1/500v-full'
# file = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-100hz/run2-1us/scope/600.csv'
# file = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180111-v-sweep/run2/scope/850_'
# file = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180126-v-sweep/run2/scope/650_'
file = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180126-burst-3/run8/scope/3_'
lines = []
calcs = []
for i in range(0,10):
    # line = get_vol_cur_single(file+str(i), current_scaling=-0.5, cur)
    line = get_vol_cur_single(file+str(i), current_scaling=0.5, delay=-5, voltage_offset=28)
    lines.append(line)
    calcs.append(calc_output(line, REACTOR_GLASS_LONG))
# lines = get_vol_cur_multiple(file, voltage_offset=30)
# lines = get_vol_cur_multiple(file, current_scaling=-0.5)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax3 = ax1.twinx()
fig4,ax4 = plt.subplots()

for line, calc in zip(lines, calcs):
    ax1.plot(line[0], line[1], 'b-')
    ax2.plot(line[0], line[2], 'r-')
    ax4.plot(calc['t'], calc['e'])

ax1.set_xlabel('time [s]')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('voltage [V]', color='b')
ax2.set_ylabel('current [A]', color='r')
ax3.set_ylabel('power [W]', color='g')
ax1.tick_params('y', colors='b')
ax2.tick_params('y', colors='r')
plt.title('V and I for 1us, 15kV pulse, small_glass')
plt.show()



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
