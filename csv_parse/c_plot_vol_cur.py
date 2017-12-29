import numpy as np
import matplotlib.pyplot as plt
from b_correct_lines import correct_lines
from a_easyscope_parser import parse_file
from scipy import integrate


file='../../20171227 glasstube, spectrometer, plasma/1/800v-full'
# line_objs = parse_file(file='../../20171228 glasstube/1/500v-full')  # file to parse
line_objs = parse_file(file)  # file to parse
x_axis, y_axes = correct_lines(line_objs)
y1 = y_axes[0]
y2 = y_axes[1]

y3=integrate.cumtrapz(y1, x_axis, initial=0)*-50

p = y1*y2
fig, ax1 = plt.subplots()
ax1.plot(x_axis, y1, 'b-')
ax1.set_xlabel('time [ns]')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('current [A]', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(x_axis, y2, 'r-') # voltage
# ax2.plot(x_axis, y3, 'g-') # integrated current
ax2.set_ylabel('voltage [V]', color='r')
ax2.tick_params('y', colors='r')
# ax2.axis([2000,5000,-9000,9000])
# ax1.axis([2000,5000,-0.5,0.5])

fig.tight_layout()


fig, ax1 = plt.subplots()
ax1.plot(x_axis, p, 'b-') # power
fig.tight_layout()

fig, ax1 = plt.subplots()
ax1.plot(x_axis, integrate.cumtrapz(p, x_axis, initial=0), 'b-') # energy
fig.tight_layout()

plt.show()
print('finish')