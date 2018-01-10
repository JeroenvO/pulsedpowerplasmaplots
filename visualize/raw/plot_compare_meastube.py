import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.colors import color_list
from visualize.helpers.helpers import load_pickle, get_values, markers

data2 = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run1/data.pkl")
data1 = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run2-longmeas/data.pkl")
# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run1/data.pkl")

# filter all values above 700v input, because below that is no plasma
# data = [d for d in data if d['input_voltage']>700]

# y = get_values(data, 'input_yield_gkwh')
v1 = get_values(data1, 'o3_ppm')
v2 = get_values(data2, 'o3_ppm')
x1 = get_values(data1, 'input_voltage_output')
x2 = get_values(data2, 'input_voltage_output')
# w = get_values(data, 'pulse_duration')

assert len(x1) == len(v1) == len(x2) == len(v2)

fig, ax = plt.subplots()
ax1 = ax.plot(x1, v1, label='Long measure tube')
ax2 = ax.plot(x2, v2, label='Short measure tube')
plt.xlabel('Output voltage')
plt.ylabel('PPM')
plt.title('Comparison of long and short measure tube')
ax.grid(True)

plt.legend()
plt.show()
fig.savefig('compare_meas.png', bbox_inches='tight')
fig.savefig('compare_meas.eps', bbox_inches='tight')
