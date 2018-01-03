import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from visualize.helpers.colors import color_list
from visualize.helpers.helpers import load_pickle, get_values, markers

# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20171229/data.pkl")

data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run1/data.pkl")
data += load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run3-800v-width/data.pkl")
# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run1/data.pkl")

# filter all values above 700v input, because below that is no plasma
data = [d for d in data if d['input_voltage']>700]

y = get_values(data, 'input_yield_gkwh')
x = get_values(data, 'o3_ppm')
v = get_values(data, 'input_voltage_output')
w = get_values(data, 'pulse_duration')

assert len(y) == len(x) == len(v)

colors = color_list(len(x))

ws = np.unique(w)
vs = np.unique(v)

fig, ax = plt.subplots()
for ix,iy,iv,w in zip(x,y,v,w):
    m = markers[np.where(ws==w)[0][0]]  # marker for each pulsewidth
    c = colors[np.where(vs==iv)[0][0]] # color for each voltage
    ax.scatter(ix, iy, c=c, label=iv, marker=m)
plt.xlabel('Concentration [PPM]')
plt.ylabel('Yield [g/kWh]')
plt.title('Concentration vs Yield')

# legend for pulsewidth
marker_legends = []
for w,m in zip(ws, markers[0:len(ws)]):
    marker_legends.append(mlines.Line2D([],[],marker=m, label=str(w)+" $\mu$s", linewidth=0))
lgd1 = plt.legend(handles=marker_legends, loc='best')
axleg1 = plt.gca().add_artist(lgd1)  # returns ax

# legend for voltage
lgd2 = plt.legend((np.unique(v)), loc='upper left', bbox_to_anchor=(1,1))
# axleg2 = plt.gca().add_artist(lgd2)  # returns ax

# lgd = plt.legend((v), loc='upper left', bbox_to_anchor=(1,1))
ax.grid(True)
fig.savefig('ppm_yield.png', bbox_extra_artists=(lgd2, lgd1, ), bbox_inches='tight')
plt.show()