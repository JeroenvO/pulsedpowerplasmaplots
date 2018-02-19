import numpy as np
import matplotlib.pyplot as plt

from visualize.helpers.data import load_pickle, get_values, filter_data
from visualize.helpers.plot import set_plot, save_file
from visualize.helpers.colors import color2
colors = color2
# voltage sweep with two meas.
# data2 = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run1/data.pkl")
# data1 = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run2-longmeas/data.pkl")

# current sweep with two meas.
data2 = load_pickle("20180131-compare/run1") + load_pickle("20180131-compare/run1-2")
data1 = load_pickle("20180131-compare/run2") + load_pickle("20180131-compare/run2-2")

v1 = get_values(data1, 'o3_ppm')
v2 = get_values(data2, 'o3_ppm')
x1 = get_values(data1, 'input_f')
x2 = get_values(data2, 'input_f')
fig, ax1= plt.subplots()
ax1.plot(x1, v1, label='Long measure cell', marker='o', c=colors[0])
ax1.plot(x2, v2, label='Short measure cell', marker='d', c=colors[1])
plt.xlabel('Output frequency [Hz]')
plt.ylabel('Ozone [ppm]')
plt.legend()
set_plot(fig)
save_file(fig, name='compare-meascell', path='plots_final_v2')