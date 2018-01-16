import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

from visualize.helpers.helpers import load_pickles, load_pickle, save_file, filter_data, get_values, set_plot

data = []
# reactor = 'short-glass'
reactor = 'long-glass'
if reactor == 'long-glass':
    # data += load_pickles('20180103-1000hz')
    data += load_pickles('20180104-100hz')
    data += load_pickles('20180104-500hz')
    # data += load_pickle("20180105-freq/run1-1us/data.pkl")
    # data += load_pickle('20180115/run5/data.pkl')
elif reactor == 'short-glass':
    data += load_pickles('20180111')

data = filter_data(data, input_l=1) # values with l=0.5us are not correct measured.

data_100 = filter_data(data, input_f=100)
data_500 = filter_data(data, input_f=500)

fig, ax = plt.subplots()

c = 'black'
m = 'o'

x_100 = get_values(data_100, 'output_v_pulse')/1000
y_100 = get_values(data_100, 'o3_ppm')
x_i_100 = np.linspace(min(x_100), max(x_100), 100)

f = interp1d(x_100, y_100, kind='cubic')
ax.plot(x_i_100, f(x_i_100), c='grey')
for x, y in zip(x_100, y_100):
    ax.scatter(x, y, c=c, marker=m)

x_500 = get_values(data_500, 'output_v_pulse')/1000
y_500 = get_values(data_500, 'o3_ppm')
x_i_500 = np.linspace(min(x_500), max(x_500), 100)
f = interp1d(x_500, y_500, kind='quadratic')
ax.plot(x_i_500, f(x_i_500), c='grey')
for x, y in zip(x_500, y_500):
    ax.scatter(x, y, c=c, marker=m)

plt.ylabel('Concentration [PPM]')
plt.xlabel('Pulse voltage [kV]')
set_plot(fig)
save_file(fig, name='v_ppm_'+reactor, path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final')