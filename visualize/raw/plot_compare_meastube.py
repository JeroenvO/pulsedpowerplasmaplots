import numpy as np
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickle, get_values, filter_data

# voltage sweep with two meas.
# data2 = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run1/data.pkl")
# data1 = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run2-longmeas/data.pkl")

# current sweep with two meas.
data2 = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180115-def1/run1/data.pkl")
data1 = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180115-def1/run4/data.pkl")

data2 = filter_data(data2, input_f__le=500)
data1 = filter_data(data1, input_f__le=500)

# y = get_values(data, 'input_yield_gkwh')
v1 = get_values(data1, 'o3_ppm')
v2 = get_values(data2, 'o3_ppm')
x1 = get_values(data1, 'output_energy_dens')
# x1 = get_values(data1, 'input_f')
x2 = get_values(data2, 'output_energy_dens')
# x2 = get_values(data2, 'input_f')
# w = get_values(data, 'pulse_duration')

assert len(x1) == len(v1) == len(x2) == len(v2)

fig, ax = plt.subplots()
ax1 = ax.plot(x1, v1, label='Long measure tube', marker='o')
ax2 = ax.plot(x2, v2, label='Short measure tube', marker='o')

#
# x = np.linspace(0, 500, 1000)
# y = (v1[2]-v1[0])/(x1[2]-x1[0]) * x
# ax.plot(x, y, label='Long meas linear')
#
# x = np.linspace(0, 500, 1000)
# y = (v2[2]-v2[0])/(x2[2]-x2[0]) * x
# ax.plot(x, y, label='Short meas linear')

plt.xlabel('Output frequency [Hz]')
plt.ylabel('ppm')
# plt.title('Comparison of long and short measure tube')
ax.grid(True)
# plt.xscale('log')
plt.legend()
plt.show()