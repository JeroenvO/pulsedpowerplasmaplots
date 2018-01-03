import matplotlib.pyplot as plt
from scipy import integrate
from analyze.scope_parse.c_get_lines import get_vol_cur_single
# file='../../20171227 glasstube, spectrometer, plasma/1/800v-full'
# file='../../20171228 glasstube/1/500v-full'
file = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180103/run2-1us/scope/750.csv'

x_axis, vol, cur = get_vol_cur_single(file)
y1=vol
y2=cur
y3=integrate.cumtrapz(y1, x_axis, initial=0)*-50

p = y1*y2
fig, ax1 = plt.subplots()
ax1.plot(x_axis, y1, 'b-')
ax1.set_xlabel('time [s]')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('current [A]', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(x_axis, y2, 'r-') # voltage
# ax2.plot(x_axis, y3, 'g-') # integrated current
ax2.set_ylabel('voltage [V]', color='r')
ax2.tick_params('y', colors='r')
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

plt.show()
print('finish')