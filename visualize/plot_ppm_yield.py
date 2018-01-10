import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.colors import color_list
from visualize.helpers.helpers import load_pickles, load_pickle, get_values, save_file

# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20171229/data.pkl")

# huge losses in these measurements. Maybe conductive sheet below coil...
# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run1/data.pkl")
# data += load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run3-800v-width/data.pkl")

# very good measurements with different voltages and pulsewidths
# data = load_pickles('G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-500hz')

# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180105-freq/run1-1us/data.pkl")
# data += load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180105-freq/run2-1us-q/data.pkl")

data = load_pickles("G:/Prive/MIJN-Documenten/TU/62-Stage/20180110/")

# filter all values above 700v input, because below that is no plasma
data = [d for d in data if d['input_yield_gkwh'] > 2]

y = get_values(data, 'output_yield_gkwh')
x = get_values(data, 'o3_ppm')
v = get_values(data, 'input_v_output')
w = get_values(data, 'input_l')
ind = get_values(data, 'inductance')
assert len(y) == len(x) == len(v)

ws = np.unique(w)
vs = np.unique(v)
colors = color_list(len(ws))

fig, ax = plt.subplots()

# scatterplot for each point
for ix, iy, iw, iv, iind in zip(x, y, w, v, ind):
    if iind == 0:
        c = colors[np.where(ws == iw)[0][0]]  # color for each pulsewidth
    else:
        c = 'black'
    i = np.where(vs == iv)[0][0]
    m = (i + 2, 2, 0)  # marker for each voltage
    ax.scatter(ix, iy, c=c, marker=m)

plt.xlabel('Concentration [PPM]')
plt.ylabel('Yield [g/kWh]')
plt.title('Concentration vs Yield (5Hz-500Hz, 2ls/min, short glass 4 electr.)')

# legend for pulsewidth, colors
marker_legends = []
for iw, c in zip(ws, colors):
    label = str(iw) + " $\mu$s"
    marker_legends.append(mlines.Line2D([], [], color=c, marker='.', label=label))
marker_legends.append(mlines.Line2D([], [], color='black', marker='.', label='1 $\mu$s, 26uH'))

lgd1 = plt.legend(handles=marker_legends, loc='best')
axleg1 = plt.gca().add_artist(lgd1)

# legend for voltage, markers
marker_legends = []
for i, iv in enumerate(vs):
    label = str((iv / 1000)) + 'kV'
    m = (i + 2, 2, 0)
    marker_legends.append(mlines.Line2D([], [], marker=m, label=label, linewidth=0, color='black'))

lgd2 = plt.legend(handles=marker_legends, loc='lower center')

# connect voltages with lines
# for iv in vs:
#     d = [d for d in data if d['input_v_output'] == iv]
#     y = get_values(d, 'input_yield_gkwh')
#     x = get_values(d, 'o3_ppm')
#     plt.plot(x,y, linewidth=0.2, c='black')
ax.grid(True)
save_file(fig, name='ppm_yield_freq')
plt.show()
