import numpy as np
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickle, get_values, filter_data
from visualize.helpers.plot import set_plot, save_file
from visualize.helpers.colors import color_viridis
colors = color_viridis(4)
# voltage sweep with two meas.
# data2 = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run1/data.pkl")
# data1 = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run2-longmeas/data.pkl")

# current sweep with two meas.
data2 = load_pickle("20180131-compare/run1") + load_pickle("20180131-compare/run1-2")
data1 = load_pickle("20180131-compare/run2") + load_pickle("20180131-compare/run2-2")

# data2 = filter_data(data2, input_f__le=500)
# data1 = filter_data(data1, input_f__le=500)

# y = get_values(data, 'input_yield_gkwh')
v1 = get_values(data1, 'o3_ppm')
v2 = get_values(data2, 'o3_ppm')
# x1 = get_values(data1, 'output_energy_dens')
x1 = get_values(data1, 'input_f')
# x2 = get_values(data2, 'output_energy_dens')
x2 = get_values(data2, 'input_f')
# w = get_values(data, 'pulse_duration')

# assert len(x1) == len(v1) == len(x2) == len(v2)

fig, ax1= plt.subplots(1,1)
ax1.plot(x1, v1, label='Long measure cell', marker='o', c=colors[1])
ax1.plot(x2, v2, label='Short measure cell', marker='d', c=colors[2])
# ax1.set_xscale('log')
# ax1.set_yscale('log')
# ax2.set_yscale('log')
#
# a = 4
# b = 9
# x = np.linspace(0, 1750, 10)
# y1 = (v1[b]-v1[a])/(x1[b]-x1[a]) * x
# y2 = (v2[b]-v2[a])/(x2[b]-x2[a]) * x
# ax1.plot(x, y1, label='Linear')
# ax2.plot(x, y2, label='Linear')
# ax1.set_ylim(0,1900)
# ax2.set_ylim(0,1900)
plt.xlabel('Output frequency [Hz]')
plt.ylabel('Ozone [ppm]')
plt.legend()
set_plot(fig)
save_file(fig, name='compare-meastube', path='plots_final_v2')

