import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.colors import color_list
from visualize.helpers.data import load_pickles, load_pickle, get_values, save_file, sort_data, filter_data

# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20171229/data.pkl")

# huge losses in these measurements. Maybe conductive sheet below coil...
# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run1/data.pkl")
# data += load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run3-800v-width/data.pkl")

# very good measurements with different voltages and pulsewidths
data = []
reactor = 'short-glass'
if reactor == 'long-glass':
    # data += load_pickle('G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run1')
    data += load_pickles('G:/Prive/MIJN-Documenten/TU/62-Stage/20180103-1000hz')
    data += load_pickles('G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-100hz')
    data += load_pickles('G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-500hz')
    data += load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180105-freq/run1-1us/data.pkl")
    # data += load_pickles()
elif reactor == 'short-glass':
    data += load_pickle('G:/Prive/MIJN-Documenten/TU/62-Stage/20180111/run1')
# data += load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180105-freq/run2-1us-q/data.pkl")

# data = load_pickles("G:/Prive/MIJN-Documenten/TU/62-Stage/20180110/")

# filter all values above 700v input, because below that is no plasma


data = filter_data(data, input_l__ge=1) # values with l=0.5us are not correct measured.
# data = filter_data(data, input_l=40) # values with l=0.5us are not correct measured.

data = sort_data(data, key='input_v_output')
data = sort_data(data, key='input_f')

v = get_values(data, 'input_f')
w = get_values(data, 'input_l')

ws = np.unique(w)
fs = np.unique(v)
colors = color_list(len(ws))

fig, ax = plt.subplots()

# scatterplot for each point
for d in data:
    c = colors[np.where(ws == d['input_l'])[0][0]]  # color for each pulsewidth
    i = np.where(fs == d['input_f'])[0][0]
    # m = (i + 2, 2, 0)  # marker for each voltage
    m = 'o'
    x = d['output_v_pulse'] / 1000
    y = d['o3_ppm']
    ax.scatter(x, y, c=c, marker=m)
    if d['input_v_output'] == 15e3 and d['input_l'] == 1:
        # labels for the rightmost points
        ax.annotate(d['input_f'], (x, y))

plt.ylabel('Concentration [PPM]')
plt.xlabel('Pulse voltage [kV]')
plt.title('Concentration vs voltage (2ls/min, ' + reactor + ', 26$\mu$H coil.)')

# legend for pulsewidth, colors
marker_legends = []
for iw, c in zip(ws, colors):
    label = str(iw) + " $\mu$s"
    marker_legends.append(mlines.Line2D([], [], color=c, marker='.', label=label))

lgd1 = plt.legend(handles=marker_legends, loc='best')
axleg1 = plt.gca().add_artist(lgd1)

# legend for voltage, markers
marker_legends = []
# for i, iv in enumerate(fs):
#     label = str((iv)) + 'Hz'
#     m = (i + 2, 2, 0)
#     marker_legends.append(mlines.Line2D([], [], marker=m, label=label, linewidth=0, color='black'))

# lgd2 = plt.legend(handles=marker_legends, loc='best')

# connect voltages with lines
# for iv in vs:
#     d = [d for d in data if d['input_v_output'] == iv]
#     y = get_values(d, 'input_yield_gkwh')
#     x = get_values(d, 'o3_ppm')
#     plt.plot(x,y, linewidth=0.2, c='black')

# connect frequency with lines
for iv in fs:
    d = [d for d in data if d['input_f'] == iv]
    x = get_values(d, 'output_v_pulse')/1000
    y = get_values(d, 'o3_ppm')
    plt.plot(x,y, linewidth=0.2, c='black')
ax.grid(True)
save_file(fig, name='v_ppm_'+reactor)
plt.show()
