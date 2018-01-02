import functools
import operator
import pickle

import matplotlib.pylab as pl
import matplotlib.pyplot as plt
import numpy as np


def get_values(key):
    return functools.partial(map, operator.itemgetter(key))

picle = "G:/Prive/MIJN-Documenten/TU/62-Stage/20171229/data.pkl"
with open(picle, 'rb') as f:
    data = pickle.load(f)
colors =  pl.cm.rainbow(np.linspace(1,0, len(data)))*255
# convert to Hex to prevent legend bug in matplotlib. It won't show legend for line colors as array/tuple/list
colors = ["#{0:02x}{1:02x}{2:02x}".format(int(color[0]), int(color[1]), int(color[2])) for color in colors]
# normalize

fig, ax = plt.subplots(2,1)
ax[0].set_title('normalized waveforms for various pulse voltages [kV]')
for i, line in enumerate(data):
    c = line['output_current']
    v = line['output_voltage']
    try:
        c = c/max(c)
        ax[0].plot(line['output_time'], c, label=line['input_voltage_output']/1000, color=colors[i])
        v = v/max(v)
        ax[1].plot(line['output_time'], v, label=line['input_voltage_output']/1000, color=colors[i])
    except:
        pass

ax[0].set_ylabel('normalized current')
ax[1].set_ylabel('normalized voltage')
plt.xlabel('time [s]')
lgd = ax[0].legend(loc='upper left', bbox_to_anchor=(1,1))
plt.show()
fig.savefig('plot.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
print("finish")